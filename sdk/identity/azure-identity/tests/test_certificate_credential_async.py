# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from unittest.mock import Mock, patch
from urllib.parse import urlparse

from azure.core.pipeline.policies import ContentDecodePolicy, SansIOHTTPPolicy
from azure.identity import TokenCachePersistenceOptions
from azure.identity._constants import EnvironmentVariables
from azure.identity._internal.user_agent import USER_AGENT
from azure.identity.aio import CertificateCredential

from msal import TokenCache
import pytest

from helpers import build_aad_response, mock_response, Request, GET_TOKEN_METHODS
from helpers_async import async_validating_transport, AsyncMockTransport
from test_certificate_credential import ALL_CERTS, EC_CERT_PATH, PEM_CERT_PATH, validate_jwt, validate_jwt_ps256


def test_non_rsa_key():
    """The credential should raise ValueError when given a cert without an RSA private key"""
    with pytest.raises(ValueError, match=".*RS256.*"):
        CertificateCredential("tenant-id", "client-id", EC_CERT_PATH)
    with pytest.raises(ValueError, match=".*RS256.*"):
        CertificateCredential("tenant-id", "client-id", certificate_data=open(EC_CERT_PATH, "rb").read())


def test_tenant_id_validation():
    """The credential should raise ValueError when given an invalid tenant_id"""

    valid_ids = {"c878a2ab-8ef4-413b-83a0-199afb84d7fb", "contoso.onmicrosoft.com", "organizations", "common"}
    for tenant in valid_ids:
        CertificateCredential(tenant, "client-id", PEM_CERT_PATH)

    invalid_ids = {"", "my tenant", "my_tenant", "/", "\\", '"', "'"}
    for tenant in invalid_ids:
        with pytest.raises(ValueError):
            CertificateCredential(tenant, "client-id", PEM_CERT_PATH)


@pytest.mark.asyncio
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_no_scopes(get_token_method):
    """The credential should raise ValueError when get_token is called with no scopes"""

    credential = CertificateCredential("tenant-id", "client-id", PEM_CERT_PATH)
    with pytest.raises(ValueError):
        await getattr(credential, get_token_method)()


@pytest.mark.asyncio
async def test_close():
    transport = AsyncMockTransport()
    credential = CertificateCredential("tenant-id", "client-id", PEM_CERT_PATH, transport=transport)

    await credential.close()

    assert transport.__aexit__.call_count == 1


@pytest.mark.asyncio
async def test_context_manager():
    transport = AsyncMockTransport()
    credential = CertificateCredential("tenant-id", "client-id", PEM_CERT_PATH, transport=transport)

    async with credential:
        assert transport.__aenter__.call_count == 1

    assert transport.__aenter__.call_count == 1
    assert transport.__aexit__.call_count == 1


@pytest.mark.asyncio
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_policies_configurable(get_token_method):
    policy = Mock(spec_set=SansIOHTTPPolicy, on_request=Mock())

    async def send(*_, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        return mock_response(json_payload=build_aad_response(access_token="**"))

    credential = CertificateCredential(
        "tenant-id", "client-id", PEM_CERT_PATH, policies=[ContentDecodePolicy(), policy], transport=Mock(send=send)
    )

    await getattr(credential, get_token_method)("scope")

    assert policy.on_request.called


@pytest.mark.asyncio
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_user_agent(get_token_method):
    transport = async_validating_transport(
        requests=[Request(required_headers={"User-Agent": USER_AGENT})],
        responses=[mock_response(json_payload=build_aad_response(access_token="**"))],
    )

    credential = CertificateCredential("tenant-id", "client-id", PEM_CERT_PATH, transport=transport)

    await getattr(credential, get_token_method)("scope")


@pytest.mark.asyncio
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_tenant_id(get_token_method):
    transport = async_validating_transport(
        requests=[Request(required_headers={"User-Agent": USER_AGENT})],
        responses=[mock_response(json_payload=build_aad_response(access_token="**"))],
    )

    credential = CertificateCredential(
        "tenant-id", "client-id", PEM_CERT_PATH, transport=transport, additionally_allowed_tenants=["*"]
    )
    kwargs = {"tenant_id": "tenant_id"}
    if get_token_method == "get_token_info":
        kwargs = {"options": kwargs}
    await getattr(credential, get_token_method)("scope", **kwargs)


@pytest.mark.asyncio
@pytest.mark.parametrize("authority", ("localhost", "https://localhost"))
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_request_url(cert_path, cert_password, authority, get_token_method):
    """the credential should accept an authority, with or without scheme, as an argument or environment variable"""

    tenant_id = "expected-tenant"
    access_token = "***"
    parsed_authority = urlparse(authority)
    expected_netloc = parsed_authority.netloc or authority  # "localhost" parses to netloc "", path "localhost"

    async def mock_send(request, **kwargs):
        actual = urlparse(request.url)
        assert actual.scheme == "https"
        assert actual.netloc == expected_netloc
        assert actual.path.startswith("/" + tenant_id)
        return mock_response(json_payload={"token_type": "Bearer", "expires_in": 42, "access_token": access_token})

    cred = CertificateCredential(
        tenant_id, "client-id", cert_path, password=cert_password, transport=Mock(send=mock_send), authority=authority
    )
    token = await getattr(cred, get_token_method)("scope")
    assert token.token == access_token

    # authority can be configured via environment variable
    with patch.dict("os.environ", {EnvironmentVariables.AZURE_AUTHORITY_HOST: authority}, clear=True):
        credential = CertificateCredential(
            tenant_id, "client-id", cert_path, password=cert_password, transport=Mock(send=mock_send)
        )
        await getattr(credential, get_token_method)("scope")
    assert token.token == access_token


def test_requires_certificate():
    """the credential should raise ValueError when not given a certificate"""

    with pytest.raises(ValueError):
        CertificateCredential("tenant", "client-id")
    with pytest.raises(ValueError):
        CertificateCredential("tenant", "client-id", certificate_path=None)
    with pytest.raises(ValueError):
        CertificateCredential("tenant", "client-id", certificate_path="")
    with pytest.raises(ValueError):
        CertificateCredential("tenant", "client-id", certificate_data=None)
    with pytest.raises(ValueError):
        CertificateCredential("tenant", "client-id", certificate_path="", certificate_data=None)


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
@pytest.mark.parametrize("tenant_id", ("adfs", "tenant"))
async def test_request_body(cert_path, cert_password, get_token_method, tenant_id):
    access_token = "***"
    authority = "authority.com"
    client_id = "client-id"
    expected_scope = "scope"

    async def mock_send(request, **kwargs):
        assert request.body["grant_type"] == "client_credentials"
        assert request.body["scope"] == expected_scope

        with open(cert_path, "rb") as cert_file:
            if tenant_id == "adfs":
                validate_jwt(request, client_id, cert_file.read(), cert_password)
            else:
                validate_jwt_ps256(request, client_id, cert_file.read(), cert_password)

        return mock_response(json_payload={"token_type": "Bearer", "expires_in": 42, "access_token": access_token})

    cred = CertificateCredential(
        tenant_id, client_id, cert_path, password=cert_password, transport=Mock(send=mock_send), authority=authority
    )
    token = await getattr(cred, get_token_method)(expected_scope)
    assert token.token == access_token

    # credential should also accept the certificate as bytes
    with open(cert_path, "rb") as f:
        cert_bytes = f.read()

    cred = CertificateCredential(
        tenant_id,
        client_id,
        certificate_data=cert_bytes,
        password=cert_password,
        transport=Mock(send=mock_send),
        authority=authority,
    )
    token = await getattr(cred, get_token_method)(expected_scope)
    assert token.token == access_token


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_token_cache_memory(cert_path, cert_password, get_token_method):
    """the credential should optionally use a persistent cache, and default to an in memory cache"""

    access_token = "token"
    transport = async_validating_transport(
        requests=[Request(), Request()],
        responses=[
            mock_response(json_payload=build_aad_response(access_token=access_token)),
            mock_response(json_payload=build_aad_response(access_token=access_token)),
        ],
    )

    with patch("azure.identity._internal.aad_client_base._load_persistent_cache") as load_persistent_cache:
        with patch("azure.identity._internal.aad_client_base.TokenCache") as mock_token_cache:
            credential = CertificateCredential(
                "tenant", "client-id", cert_path, password=cert_password, transport=transport
            )
            assert not mock_token_cache.called
            assert not load_persistent_cache.called

            await getattr(credential, get_token_method)("scope")
            assert mock_token_cache.call_count == 1
            assert load_persistent_cache.call_count == 0
            assert credential._client._cache is not None
            assert credential._client._cae_cache is None

            kwargs = {"enable_cae": True}
            if get_token_method == "get_token_info":
                kwargs = {"options": kwargs}
            await getattr(credential, get_token_method)("scope", **kwargs)
            assert mock_token_cache.call_count == 2
            assert load_persistent_cache.call_count == 0
            assert credential._client._cae_cache is not None


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_token_cache_persistent(cert_path, cert_password, get_token_method):
    """the credential should optionally use a persistent cache, and default to an in memory cache"""

    access_token = "token"
    transport = async_validating_transport(
        requests=[Request(), Request()],
        responses=[
            mock_response(json_payload=build_aad_response(access_token=access_token)),
            mock_response(json_payload=build_aad_response(access_token=access_token)),
        ],
    )

    with patch("azure.identity._internal.aad_client_base._load_persistent_cache") as load_persistent_cache:
        with patch("azure.identity._internal.aad_client_base.TokenCache") as mock_token_cache:

            credential = CertificateCredential(
                "tenant",
                "client-id",
                cert_path,
                password=cert_password,
                cache_persistence_options=TokenCachePersistenceOptions(),
                transport=transport,
            )
            assert not mock_token_cache.called
            assert not load_persistent_cache.called

            await getattr(credential, get_token_method)("scope")
            assert load_persistent_cache.call_count == 1
            assert credential._client._cache is not None
            assert credential._client._cae_cache is None
            args, _ = load_persistent_cache.call_args
            assert args[1] is False

            kwargs = {"enable_cae": True}
            if get_token_method == "get_token_info":
                kwargs = {"options": kwargs}
            await getattr(credential, get_token_method)("scope", **kwargs)
            assert load_persistent_cache.call_count == 2
            assert credential._client._cae_cache is not None
            args, _ = load_persistent_cache.call_args
            assert args[1] == True
            assert not mock_token_cache.called


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_persistent_cache_multiple_clients(cert_path, cert_password, get_token_method):
    """the credential shouldn't use tokens issued to other service principals"""

    access_token_a = "token a"
    access_token_b = "not " + access_token_a
    transport_a = async_validating_transport(
        requests=[Request()], responses=[mock_response(json_payload=build_aad_response(access_token=access_token_a))]
    )
    transport_b = async_validating_transport(
        requests=[Request()], responses=[mock_response(json_payload=build_aad_response(access_token=access_token_b))]
    )

    cache = TokenCache()
    with patch("azure.identity._internal.aad_client_base._load_persistent_cache") as mock_cache_loader:
        mock_cache_loader.return_value = Mock(wraps=cache)
        credential_a = CertificateCredential(
            "tenant",
            "client-a",
            cert_path,
            password=cert_password,
            transport=transport_a,
            cache_persistence_options=TokenCachePersistenceOptions(),
        )
        assert mock_cache_loader.call_count == 0

        credential_b = CertificateCredential(
            "tenant",
            "client-b",
            cert_path,
            password=cert_password,
            transport=transport_b,
            cache_persistence_options=TokenCachePersistenceOptions(),
        )
        assert mock_cache_loader.call_count == 0

        # A caches a token
        scope = "scope"
        token_a = await getattr(credential_a, get_token_method)(scope)
        assert token_a.token == access_token_a
        assert transport_a.send.call_count == 1
        assert mock_cache_loader.call_count == 1
        args, _ = mock_cache_loader.call_args
        assert args[1] is False  # not CAE

        # B should get a different token for the same scope
        token_b = await getattr(credential_b, get_token_method)(scope)
        assert token_b.token == access_token_b
        assert transport_b.send.call_count == 1
        assert mock_cache_loader.call_count == 2

        assert len(list(cache.search(TokenCache.CredentialType.ACCESS_TOKEN))) == 2


def test_certificate_arguments():
    """The credential should raise ValueError for mutually exclusive arguments"""

    with pytest.raises(ValueError) as ex:
        CertificateCredential("tenant-id", "client-id", certificate_path="...", certificate_data="...")
    message = str(ex.value)
    assert "certificate_data" in message and "certificate_path" in message


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_multitenant_authentication(cert_path, cert_password, get_token_method):
    first_tenant = "first-tenant"
    first_token = "***"
    second_tenant = "second-tenant"
    second_token = first_token * 2

    async def send(request, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        parsed = urlparse(request.url)
        tenant = parsed.path.split("/")[1]
        assert tenant in (first_tenant, second_tenant), 'unexpected tenant "{}"'.format(tenant)
        token = first_token if tenant == first_tenant else second_token
        return mock_response(json_payload=build_aad_response(access_token=token))

    credential = CertificateCredential(
        first_tenant,
        "client-id",
        cert_path,
        password=cert_password,
        transport=Mock(send=send),
        additionally_allowed_tenants=["*"],
    )
    token = await getattr(credential, get_token_method)("scope")
    assert token.token == first_token

    kwargs = {"tenant_id": first_tenant}
    if get_token_method == "get_token_info":
        kwargs = {"options": kwargs}
    token = await getattr(credential, get_token_method)("scope", **kwargs)
    assert token.token == first_token

    kwargs = {"tenant_id": second_tenant}
    if get_token_method == "get_token_info":
        kwargs = {"options": kwargs}
    token = await getattr(credential, get_token_method)("scope", **kwargs)
    assert token.token == second_token

    # should still default to the first tenant
    token = await getattr(credential, get_token_method)("scope")
    assert token.token == first_token


@pytest.mark.asyncio
@pytest.mark.parametrize("cert_path,cert_password", ALL_CERTS)
@pytest.mark.parametrize("get_token_method", GET_TOKEN_METHODS)
async def test_multitenant_authentication_backcompat(cert_path, cert_password, get_token_method):
    expected_tenant = "expected-tenant"
    expected_token = "***"

    async def send(request, **kwargs):
        # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to transport
        assert "claims" not in kwargs
        assert "tenant_id" not in kwargs
        parsed = urlparse(request.url)
        tenant = parsed.path.split("/")[1]
        token = expected_token if tenant == expected_tenant else expected_token * 2
        return mock_response(json_payload=build_aad_response(access_token=token))

    credential = CertificateCredential(
        expected_tenant,
        "client-id",
        cert_path,
        password=cert_password,
        transport=Mock(send=send),
        additionally_allowed_tenants=["*"],
    )

    token = await getattr(credential, get_token_method)("scope")
    assert token.token == expected_token

    kwargs = {"tenant_id": expected_tenant}
    if get_token_method == "get_token_info":
        kwargs = {"options": kwargs}
    # explicitly specifying the configured tenant is okay
    token = await getattr(credential, get_token_method)("scope", **kwargs)
    assert token.token == expected_token

    kwargs = {"tenant_id": "un" + expected_tenant}
    if get_token_method == "get_token_info":
        kwargs = {"options": kwargs}
    token = await getattr(credential, get_token_method)("scope", **kwargs)
    assert token.token == expected_token * 2
