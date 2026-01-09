# Release History

## 1.1.0b2 (2026-01-09)

### Features Added

  - Added operation group FeaturesOperations
  - Added operation group IngestionPrivateEndpointConnectionsOperations
  - Added operation group KafkaConfigurationsOperations
  - Added operation group UsagesOperations
  - Model Account has a new parameter account_status
  - Model Account has a new parameter default_domain
  - Model Account has a new parameter ingestion_storage
  - Model Account has a new parameter managed_event_hub_state
  - Model Account has a new parameter managed_resources_public_network_access
  - Model Account has a new parameter merge_info
  - Model Account has a new parameter tenant_endpoint_state
  - Model AccountUpdateParameters has a new parameter account_status
  - Model AccountUpdateParameters has a new parameter cloud_connectors
  - Model AccountUpdateParameters has a new parameter created_at
  - Model AccountUpdateParameters has a new parameter created_by
  - Model AccountUpdateParameters has a new parameter created_by_object_id
  - Model AccountUpdateParameters has a new parameter default_domain
  - Model AccountUpdateParameters has a new parameter endpoints
  - Model AccountUpdateParameters has a new parameter friendly_name
  - Model AccountUpdateParameters has a new parameter ingestion_storage
  - Model AccountUpdateParameters has a new parameter managed_event_hub_state
  - Model AccountUpdateParameters has a new parameter managed_resource_group_name
  - Model AccountUpdateParameters has a new parameter managed_resources
  - Model AccountUpdateParameters has a new parameter managed_resources_public_network_access
  - Model AccountUpdateParameters has a new parameter merge_info
  - Model AccountUpdateParameters has a new parameter private_endpoint_connections
  - Model AccountUpdateParameters has a new parameter provisioning_state
  - Model AccountUpdateParameters has a new parameter public_network_access
  - Model AccountUpdateParameters has a new parameter tenant_endpoint_state
  - Model PrivateEndpointConnection has a new parameter system_data
  - Model PrivateLinkResource has a new parameter group_id
  - Model PrivateLinkResource has a new parameter required_members
  - Model PrivateLinkResource has a new parameter required_zone_names
  - Model PrivateLinkResource has a new parameter system_data
  - Model ProxyResource has a new parameter system_data

### Breaking Changes

  - Model AccountEndpoints no longer has parameter guardian
  - Model AccountList no longer has parameter count
  - Model AccountPropertiesEndpoints no longer has parameter guardian
  - Model AccountUpdateParameters no longer has parameter properties
  - Model PrivateEndpointConnectionList no longer has parameter count
  - Model PrivateLinkResource no longer has parameter properties
  - Model PrivateLinkResourceList no longer has parameter count

## 1.1.0b1 (2022-11-07)

### Features Added

  - Model AccountUpdateParameters has a new parameter identity
  - Model Identity has a new parameter user_assigned_identities

## 1.0.0 (2021-08-13)

**Features**

  - Model Account has a new parameter managed_resource_group_name
  - Model Account has a new parameter system_data
  - Model TrackedResource has a new parameter system_data
  - Model PrivateLinkResource has a new parameter properties
  - Added operation AccountsOperations.add_root_collection_admin
  - Added operation PrivateEndpointConnectionsOperations.begin_create_or_update

**Breaking changes**

  - Model PrivateLinkResource no longer has parameter required_zone_names
  - Model PrivateLinkResource no longer has parameter group_id
  - Model PrivateLinkResource no longer has parameter required_members
  - Model AccountUpdateParameters has a new signature
  - Removed operation PrivateEndpointConnectionsOperations.create_or_update

## 1.0.0b1 (2021-02-01)

* Initial Release
