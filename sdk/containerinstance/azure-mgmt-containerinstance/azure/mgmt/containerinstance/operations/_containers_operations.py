# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_logs_request(
    resource_group_name: str,
    container_group_name: str,
    container_name: str,
    subscription_id: str,
    *,
    tail: Optional[int] = None,
    timestamps: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if tail is not None:
        _params["tail"] = _SERIALIZER.query("tail", tail, "int")
    if timestamps is not None:
        _params["timestamps"] = _SERIALIZER.query("timestamps", timestamps, "bool")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_execute_command_request(
    resource_group_name: str, container_group_name: str, container_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/exec",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_attach_request(
    resource_group_name: str, container_group_name: str, container_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/attach",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ContainersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.containerinstance.ContainerInstanceManagementClient`'s
        :attr:`containers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_logs(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        tail: Optional[int] = None,
        timestamps: Optional[bool] = None,
        **kwargs: Any
    ) -> _models.Logs:
        """Get the logs for a specified container instance.

        Get the logs for a specified container instance in a specified resource group and container
        group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param container_group_name: The name of the container group. Required.
        :type container_group_name: str
        :param container_name: The name of the container instance. Required.
        :type container_name: str
        :param tail: The number of lines to show from the tail of the container instance log. If not
         provided, all available logs are shown up to 4mb. Default value is None.
        :type tail: int
        :param timestamps: If true, adds a timestamp at the beginning of every line of log output. If
         not provided, defaults to false. Default value is None.
        :type timestamps: bool
        :return: Logs or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.Logs
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Logs] = kwargs.pop("cls", None)

        _request = build_list_logs_request(
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            subscription_id=self._config.subscription_id,
            tail=tail,
            timestamps=timestamps,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Logs", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def execute_command(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        container_exec_request: _models.ContainerExecRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContainerExecResponse:
        """Executes a command in a specific container instance.

        Executes a command for a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param container_group_name: The name of the container group. Required.
        :type container_group_name: str
        :param container_name: The name of the container instance. Required.
        :type container_name: str
        :param container_exec_request: The request for the exec command. Required.
        :type container_exec_request: ~azure.mgmt.containerinstance.models.ContainerExecRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ContainerExecResponse or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerExecResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def execute_command(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        container_exec_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContainerExecResponse:
        """Executes a command in a specific container instance.

        Executes a command for a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param container_group_name: The name of the container group. Required.
        :type container_group_name: str
        :param container_name: The name of the container instance. Required.
        :type container_name: str
        :param container_exec_request: The request for the exec command. Required.
        :type container_exec_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ContainerExecResponse or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerExecResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def execute_command(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        container_exec_request: Union[_models.ContainerExecRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.ContainerExecResponse:
        """Executes a command in a specific container instance.

        Executes a command for a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param container_group_name: The name of the container group. Required.
        :type container_group_name: str
        :param container_name: The name of the container instance. Required.
        :type container_name: str
        :param container_exec_request: The request for the exec command. Is either a
         ContainerExecRequest type or a IO[bytes] type. Required.
        :type container_exec_request: ~azure.mgmt.containerinstance.models.ContainerExecRequest or
         IO[bytes]
        :return: ContainerExecResponse or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerExecResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ContainerExecResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(container_exec_request, (IOBase, bytes)):
            _content = container_exec_request
        else:
            _json = self._serialize.body(container_exec_request, "ContainerExecRequest")

        _request = build_execute_command_request(
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ContainerExecResponse", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def attach(
        self, resource_group_name: str, container_group_name: str, container_name: str, **kwargs: Any
    ) -> _models.ContainerAttachResponse:
        """Attach to the output of a specific container instance.

        Attach to the output stream of a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param container_group_name: The name of the container group. Required.
        :type container_group_name: str
        :param container_name: The name of the container instance. Required.
        :type container_name: str
        :return: ContainerAttachResponse or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerAttachResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ContainerAttachResponse] = kwargs.pop("cls", None)

        _request = build_attach_request(
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ContainerAttachResponse", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
