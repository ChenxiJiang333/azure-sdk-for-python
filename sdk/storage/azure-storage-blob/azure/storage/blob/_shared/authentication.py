# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import logging
import re
from typing import List, Tuple
from urllib.parse import unquote, urlparse
from functools import cmp_to_key

try:
    from yarl import URL
except ImportError:
    pass

try:
    from azure.core.pipeline.transport import AioHttpTransport  # pylint: disable=non-abstract-transport-import
except ImportError:
    AioHttpTransport = None

from azure.core.exceptions import ClientAuthenticationError
from azure.core.pipeline.policies import SansIOHTTPPolicy

from . import sign_string

logger = logging.getLogger(__name__)


# fmt: off
table_lv0 = [
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x71c, 0x0, 0x71f, 0x721, 0x723, 0x725,
    0x0, 0x0, 0x0, 0x72d, 0x803, 0x0, 0x0, 0x733, 0x0, 0xd03, 0xd1a, 0xd1c, 0xd1e,
    0xd20, 0xd22, 0xd24, 0xd26, 0xd28, 0xd2a, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0xe02, 0xe09, 0xe0a, 0xe1a, 0xe21, 0xe23, 0xe25, 0xe2c, 0xe32, 0xe35, 0xe36, 0xe48, 0xe51,
    0xe70, 0xe7c, 0xe7e, 0xe89, 0xe8a, 0xe91, 0xe99, 0xe9f, 0xea2, 0xea4, 0xea6, 0xea7, 0xea9,
    0x0, 0x0, 0x0, 0x743, 0x744, 0x748, 0xe02, 0xe09, 0xe0a, 0xe1a, 0xe21, 0xe23, 0xe25,
    0xe2c, 0xe32, 0xe35, 0xe36, 0xe48, 0xe51, 0xe70, 0xe7c, 0xe7e, 0xe89, 0xe8a, 0xe91, 0xe99,
    0xe9f, 0xea2, 0xea4, 0xea6, 0xea7, 0xea9, 0x0, 0x74c, 0x0, 0x750, 0x0,
]

table_lv4 = [
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x8012, 0x0, 0x0, 0x0, 0x0, 0x0, 0x8212, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
    0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
]
# fmt: on


def compare(lhs: str, rhs: str) -> int:  # pylint:disable=too-many-return-statements
    tables = [table_lv0, table_lv4]
    curr_level, i, j, n = 0, 0, 0, len(tables)
    lhs_len = len(lhs)
    rhs_len = len(rhs)
    while curr_level < n:
        if curr_level == (n - 1) and i != j:
            if i > j:
                return -1
            if i < j:
                return 1
            return 0

        w1 = tables[curr_level][ord(lhs[i])] if i < lhs_len else 0x1
        w2 = tables[curr_level][ord(rhs[j])] if j < rhs_len else 0x1

        if w1 == 0x1 and w2 == 0x1:
            i = 0
            j = 0
            curr_level += 1
        elif w1 == w2:
            i += 1
            j += 1
        elif w1 == 0:
            i += 1
        elif w2 == 0:
            j += 1
        else:
            if w1 < w2:
                return -1
            if w1 > w2:
                return 1
            return 0
    return 0


# wraps a given exception with the desired exception type
def _wrap_exception(ex, desired_type):
    msg = ""
    if ex.args:
        msg = ex.args[0]
    return desired_type(msg)


# This method attempts to emulate the sorting done by the service
def _storage_header_sort(input_headers: List[Tuple[str, str]]) -> List[Tuple[str, str]]:

    # Build dict of tuples and list of keys
    header_dict = {}
    header_keys = []
    for k, v in input_headers:
        header_dict[k] = v
        header_keys.append(k)

    try:
        header_keys = sorted(header_keys, key=cmp_to_key(compare))
    except ValueError as exc:
        raise ValueError("Illegal character encountered when sorting headers.") from exc

    # Build list of sorted tuples
    sorted_headers = []
    for key in header_keys:
        sorted_headers.append((key, header_dict.pop(key)))
    return sorted_headers


class AzureSigningError(ClientAuthenticationError):
    """
    Represents a fatal error when attempting to sign a request.
    In general, the cause of this exception is user error. For example, the given account key is not valid.
    Please visit https://learn.microsoft.com/azure/storage/common/storage-create-storage-account for more info.
    """


class SharedKeyCredentialPolicy(SansIOHTTPPolicy):

    def __init__(self, account_name, account_key):
        self.account_name = account_name
        self.account_key = account_key
        super(SharedKeyCredentialPolicy, self).__init__()

    @staticmethod
    def _get_headers(request, headers_to_sign):
        headers = dict((name.lower(), value) for name, value in request.http_request.headers.items() if value)
        if "content-length" in headers and headers["content-length"] == "0":
            del headers["content-length"]
        return "\n".join(headers.get(x, "") for x in headers_to_sign) + "\n"

    @staticmethod
    def _get_verb(request):
        return request.http_request.method + "\n"

    def _get_canonicalized_resource(self, request):
        uri_path = urlparse(request.http_request.url).path
        try:
            if (
                isinstance(request.context.transport, AioHttpTransport)
                or isinstance(getattr(request.context.transport, "_transport", None), AioHttpTransport)
                or isinstance(
                    getattr(getattr(request.context.transport, "_transport", None), "_transport", None),
                    AioHttpTransport,
                )
            ):
                uri_path = URL(uri_path)
                return "/" + self.account_name + str(uri_path)
        except TypeError:
            pass
        return "/" + self.account_name + uri_path

    @staticmethod
    def _get_canonicalized_headers(request):
        string_to_sign = ""
        x_ms_headers = []
        for name, value in request.http_request.headers.items():
            if name.startswith("x-ms-"):
                x_ms_headers.append((name.lower(), value))
        x_ms_headers = _storage_header_sort(x_ms_headers)
        for name, value in x_ms_headers:
            if value is not None:
                string_to_sign += "".join([name, ":", value, "\n"])
        return string_to_sign

    @staticmethod
    def _get_canonicalized_resource_query(request):
        sorted_queries = list(request.http_request.query.items())
        sorted_queries.sort()

        string_to_sign = ""
        for name, value in sorted_queries:
            if value is not None:
                string_to_sign += "\n" + name.lower() + ":" + unquote(value)

        return string_to_sign

    def _add_authorization_header(self, request, string_to_sign):
        try:
            signature = sign_string(self.account_key, string_to_sign)
            auth_string = "SharedKey " + self.account_name + ":" + signature
            request.http_request.headers["Authorization"] = auth_string
        except Exception as ex:
            # Wrap any error that occurred as signing error
            # Doing so will clarify/locate the source of problem
            raise _wrap_exception(ex, AzureSigningError) from ex

    def on_request(self, request):
        string_to_sign = (
            self._get_verb(request)
            + self._get_headers(
                request,
                [
                    "content-encoding",
                    "content-language",
                    "content-length",
                    "content-md5",
                    "content-type",
                    "date",
                    "if-modified-since",
                    "if-match",
                    "if-none-match",
                    "if-unmodified-since",
                    "byte_range",
                ],
            )
            + self._get_canonicalized_headers(request)
            + self._get_canonicalized_resource(request)
            + self._get_canonicalized_resource_query(request)
        )

        self._add_authorization_header(request, string_to_sign)
        # logger.debug("String_to_sign=%s", string_to_sign)


class StorageHttpChallenge(object):
    def __init__(self, challenge):
        """Parses an HTTP WWW-Authentication Bearer challenge from the Storage service."""
        if not challenge:
            raise ValueError("Challenge cannot be empty")

        self._parameters = {}
        self.scheme, trimmed_challenge = challenge.strip().split(" ", 1)

        # name=value pairs either comma or space separated with values possibly being
        # enclosed in quotes
        for item in re.split("[, ]", trimmed_challenge):
            comps = item.split("=")
            if len(comps) == 2:
                key = comps[0].strip(' "')
                value = comps[1].strip(' "')
                if key:
                    self._parameters[key] = value

        # Extract and verify required parameters
        self.authorization_uri = self._parameters.get("authorization_uri")
        if not self.authorization_uri:
            raise ValueError("Authorization Uri not found")

        self.resource_id = self._parameters.get("resource_id")
        if not self.resource_id:
            raise ValueError("Resource id not found")

        uri_path = urlparse(self.authorization_uri).path.lstrip("/")
        self.tenant_id = uri_path.split("/")[0]

    def get_value(self, key):
        return self._parameters.get(key)
