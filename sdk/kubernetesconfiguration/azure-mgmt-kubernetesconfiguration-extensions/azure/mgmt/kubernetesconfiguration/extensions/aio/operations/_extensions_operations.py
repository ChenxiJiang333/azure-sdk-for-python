# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, AsyncIterable, AsyncIterator, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core import AsyncPipelineClient
from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._utils.serialization import Deserializer, Serializer
from ...operations._extensions_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)
from .._configuration import KubernetesConfigurationExtensionsMgmtClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ExtensionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.kubernetesconfiguration.extensions.aio.KubernetesConfigurationExtensionsMgmtClient`'s
        :attr:`extensions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: KubernetesConfigurationExtensionsMgmtClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_initial(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        extension: Union[_models.Extension, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(extension, (IOBase, bytes)):
            _content = extension
        else:
            _json = self._serialize.body(extension, "Extension")

        _request = build_create_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_name=extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        extension: _models.Extension,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Create a new Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param extension: Properties necessary to Create an Extension. Required.
        :type extension: ~azure.mgmt.kubernetesconfiguration.extensions.models.Extension
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        extension: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Create a new Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param extension: Properties necessary to Create an Extension. Required.
        :type extension: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        extension: Union[_models.Extension, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Create a new Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param extension: Properties necessary to Create an Extension. Is either a Extension type or a
         IO[bytes] type. Required.
        :type extension: ~azure.mgmt.kubernetesconfiguration.extensions.models.Extension or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Extension] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                cluster_rp=cluster_rp,
                cluster_resource_name=cluster_resource_name,
                cluster_name=cluster_name,
                extension_name=extension_name,
                extension=extension,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Extension", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Extension].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Extension](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        **kwargs: Any
    ) -> _models.Extension:
        """Gets Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :return: Extension or the result of cls(response)
        :rtype: ~azure.mgmt.kubernetesconfiguration.extensions.models.Extension
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Extension] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_name=extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Extension", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _delete_initial(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        force_delete: Optional[bool] = None,
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_name=extension_name,
            subscription_id=self._config.subscription_id,
            force_delete=force_delete,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        force_delete: Optional[bool] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension
        from the cluster.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param force_delete: Delete the extension resource in Azure - not the normal asynchronous
         delete. Default value is None.
        :type force_delete: bool
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                cluster_rp=cluster_rp,
                cluster_resource_name=cluster_resource_name,
                cluster_name=cluster_name,
                extension_name=extension_name,
                force_delete=force_delete,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        patch_extension: Union[_models.PatchExtension, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(patch_extension, (IOBase, bytes)):
            _content = patch_extension
        else:
            _json = self._serialize.body(patch_extension, "PatchExtension")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_name=extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        patch_extension: _models.PatchExtension,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Patch an existing Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param patch_extension: Properties to Patch in an existing Extension. Required.
        :type patch_extension: ~azure.mgmt.kubernetesconfiguration.extensions.models.PatchExtension
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        patch_extension: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Patch an existing Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param patch_extension: Properties to Patch in an existing Extension. Required.
        :type patch_extension: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        cluster_rp: str,
        cluster_resource_name: str,
        cluster_name: str,
        extension_name: str,
        patch_extension: Union[_models.PatchExtension, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Extension]:
        """Patch an existing Kubernetes Cluster Extension.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param extension_name: Name of the Extension. Required.
        :type extension_name: str
        :param patch_extension: Properties to Patch in an existing Extension. Is either a
         PatchExtension type or a IO[bytes] type. Required.
        :type patch_extension: ~azure.mgmt.kubernetesconfiguration.extensions.models.PatchExtension or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Extension or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Extension] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                cluster_rp=cluster_rp,
                cluster_resource_name=cluster_resource_name,
                cluster_name=cluster_name,
                extension_name=extension_name,
                patch_extension=patch_extension,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Extension", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Extension].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Extension](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace
    def list(
        self, resource_group_name: str, cluster_rp: str, cluster_resource_name: str, cluster_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.Extension"]:
        """List all Extensions in the cluster.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService,
         Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters,
         connectedClusters, provisionedClusters, appliances. Required.
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :return: An iterator like instance of either Extension or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.kubernetesconfiguration.extensions.models.Extension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ExtensionsList] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    cluster_rp=cluster_rp,
                    cluster_resource_name=cluster_resource_name,
                    cluster_name=cluster_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ExtensionsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
