## tsp migration

## 2.2.0b1 (2026-03-12)

change log generation failed!!! You need to write it manually!!!

### Breaking Changes

- Deleted or renamed model `ServiceManagedIdentity
- Deleted or renamed model `PrivateEndpointConnectionListResultDescription
- Deleted or renamed model `ListOperations
- Deleted or renamed enum value `ManagedServiceIdentityType.SYSTEM_ASSIGNED_USER_ASSIGNED
- Deleted or renamed enum value `ManagedServiceIdentityType.USER_ASSIGNED

- Model `DicomService` moved instance variables `provisioning_state`, `authentication_configuration`, `cors_configuration`, `service_url`, `private_endpoint_connections`, `public_network_access`, `event_state`, `encryption`, `storage_configuration` and `enable_data_partitions` under property `properties
- Model `FhirService` moved instance variables `provisioning_state`, `acr_configuration`, `authentication_configuration`, `cors_configuration`, `export_configuration`, `private_endpoint_connections`, `public_network_access`, `event_state`, `resource_version_policy_configuration`, `import_configuration`, `implementation_guides_configuration` and `encryption` under property `properties
- Model `IotConnector` moved instance variables `provisioning_state`, `ingestion_endpoint_configuration` and `device_mapping` under property `properties
- Model `IotFhirDestination` moved instance variables `provisioning_state`, `resource_identity_resolution_type`, `fhir_service_resource_id` and `fhir_mapping` under property `properties
- Model `PrivateEndpointConnection` moved instance variables `private_endpoint`, `private_link_service_connection_state` and `provisioning_state` under property `properties
- Model `ServicesPatchDescription` moved instance variable `public_network_access

### Other Changes

- Deleted model `DicomServiceCollection`/`FhirServiceCollection`/`IotConnectorCollection`/`IotFhirDestinationCollection`/`WorkspaceList` which actually were not used by SDK users

# Release History

## 3.0.0b1 (2026-03-12)

### Features Added

  - Model PrivateEndpointConnection has a new parameter system_data
  - Model PrivateEndpointConnectionDescription has a new parameter properties
  - Model PrivateEndpointConnectionListResultDescription has a new parameter next_link
  - Model PrivateLinkResourceDescription has a new parameter properties
  - Model PrivateLinkResourceListResultDescription has a new parameter next_link
  - Model Resource has a new parameter system_data
  - Model ServiceManagedIdentity has a new parameter principal_id
  - Model ServiceManagedIdentity has a new parameter tenant_id
  - Model ServiceManagedIdentity has a new parameter user_assigned_identities
  - Model StorageConfiguration has a new parameter storage_indexing_configuration

### Breaking Changes

  - Model PrivateEndpointConnectionDescription no longer has parameter private_endpoint
  - Model PrivateEndpointConnectionDescription no longer has parameter private_link_service_connection_state
  - Model PrivateEndpointConnectionDescription no longer has parameter provisioning_state
  - Model PrivateLinkResourceDescription no longer has parameter group_id
  - Model PrivateLinkResourceDescription no longer has parameter required_members
  - Model PrivateLinkResourceDescription no longer has parameter required_zone_names
  - Model ServiceManagedIdentity has a new required parameter type
  - Model ServiceManagedIdentity no longer has parameter identity
  - Parameter value of model DicomServiceCollection is now required
  - Parameter value of model FhirServiceCollection is now required
  - Parameter value of model IotConnectorCollection is now required
  - Parameter value of model IotFhirDestinationCollection is now required
  - Parameter value of model ServicesDescriptionListResult is now required
  - Parameter value of model WorkspaceList is now required

## 2.1.0 (2024-04-22)

### Features Added

  - Model DicomService has a new parameter enable_data_partitions
  - Model DicomService has a new parameter storage_configuration
  - Model FhirServiceAuthenticationConfiguration has a new parameter smart_identity_providers

## 2.0.0 (2023-12-18)

### Features Added

  - Model DicomService has a new parameter cors_configuration
  - Model DicomService has a new parameter encryption
  - Model DicomService has a new parameter event_state
  - Model FhirService has a new parameter encryption
  - Model FhirService has a new parameter implementation_guides_configuration
  - Model FhirService has a new parameter import_configuration
  - Model MetricSpecification has a new parameter enable_regional_mdm_account
  - Model MetricSpecification has a new parameter is_internal
  - Model MetricSpecification has a new parameter metric_filter_pattern
  - Model MetricSpecification has a new parameter resource_id_dimension_name_override
  - Model MetricSpecification has a new parameter source_mdm_account
  - Model ServiceCosmosDbConfigurationInfo has a new parameter cross_tenant_cmk_application_id
  - Model ServicesProperties has a new parameter import_configuration

### Breaking Changes

  - Model FhirService no longer has parameter access_policies

## 1.2.0b1 (2022-11-22)

### Features Added

  - Model DicomService has a new parameter cors_configuration
  - Model FhirService has a new parameter import_configuration
  - Model MetricSpecification has a new parameter enable_regional_mdm_account
  - Model MetricSpecification has a new parameter is_internal
  - Model MetricSpecification has a new parameter metric_filter_pattern
  - Model MetricSpecification has a new parameter resource_id_dimension_name_override
  - Model MetricSpecification has a new parameter source_mdm_account
  - Model ServicesProperties has a new parameter import_configuration

## 1.1.0 (2022-03-31)

**Features**

  - Added operation group WorkspacePrivateEndpointConnectionsOperations
  - Added operation group WorkspacePrivateLinkResourcesOperations
  - Model DicomService has a new parameter identity
  - Model DicomService has a new parameter private_endpoint_connections
  - Model DicomService has a new parameter public_network_access
  - Model DicomServicePatchResource has a new parameter identity
  - Model FhirService has a new parameter event_state
  - Model FhirService has a new parameter private_endpoint_connections
  - Model FhirService has a new parameter public_network_access
  - Model FhirService has a new parameter resource_version_policy_configuration
  - Model FhirServiceAcrConfiguration has a new parameter oci_artifacts
  - Model OperationDetail has a new parameter properties
  - Model OperationResultsDescription has a new parameter end_time
  - Model ServiceAcrConfigurationInfo has a new parameter oci_artifacts
  - Model ServiceManagedIdentityIdentity has a new parameter principal_id
  - Model ServiceManagedIdentityIdentity has a new parameter tenant_id
  - Model ServiceManagedIdentityIdentity has a new parameter user_assigned_identities
  - Model WorkspaceProperties has a new parameter private_endpoint_connections
  - Model WorkspaceProperties has a new parameter public_network_access

**Breaking changes**

  - Parameter type of model ServiceManagedIdentityIdentity is now required

## 1.1.0b1 (2021-08-26)

**Features**

  - Added operation group IotConnectorFhirDestinationOperations
  - Added operation group WorkspacesOperations
  - Added operation group FhirDestinationsOperations
  - Added operation group DicomServicesOperations
  - Added operation group FhirServicesOperations
  - Added operation group IotConnectorsOperations

## 1.0.0 (2021-04-12)

**Features**

  - Model ServicesDescription has a new parameter system_data
  - Model ServicesProperties has a new parameter acr_configuration

## 1.0.0b1 (2020-12-04)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True) For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 0.2.0 (2020-11-02)

**Features**

  - Model ServiceCosmosDbConfigurationInfo has a new parameter key_vault_key_uri
  - Model ServicesPatchDescription has a new parameter public_network_access
  - Model ServicesDescription has a new parameter identity
  - Model ServicesProperties has a new parameter public_network_access
  - Model ServicesProperties has a new parameter export_configuration
  - Model ServicesProperties has a new parameter private_endpoint_connections
  - Added operation group PrivateEndpointConnectionsOperations
  - Added operation group PrivateLinkResourcesOperations

**Breaking changes**

  - Operation ServicesOperations.update has a new signature
  - Model Resource no longer has parameter kind
  - Model Resource no longer has parameter tags
  - Model Resource no longer has parameter etag
  - Model Resource no longer has parameter location

## 0.1.0 (2019-08-03)

  - Initial Release
