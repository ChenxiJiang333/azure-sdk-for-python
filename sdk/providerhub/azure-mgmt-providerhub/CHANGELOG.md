# Release History

## tsp migration

### Breaking Changes

  - Renamed client name `ProviderHub` to `ProviderHubClient`
  - Model `LocalizedOperationDisplayDefinition` renamed its instance variable `pt` to `pt_pt`
  - Model `LocalizedOperationDisplayDefinitionProperties` renamed its instance variable `pt` to `pt_pt`
  - Deleted or renamed method `Operations.create_or_update`
  - Deleted or renamed method `Operations.delete`
  - Deleted or renamed method `Operations.list_by_provider_registration`
  - Deleted model `AuthorizedApplicationArrayResponseWithContinuation`/`CustomRolloutArrayResponseWithContinuation`/`DefaultRolloutArrayResponseWithContinuation`/`GroupConnectivityInformation`/`NotificationRegistrationArrayResponseWithContinuation`/`OperationsContent`/`OperationsDefinitionArrayResponseWithContinuation`/`ProviderMonitorSettingArrayResponseWithContinuation`/`ProviderRegistrationArrayResponseWithContinuation`/`ResourceTypeRegistrationArrayResponseWithContinuation`/`SkuResourceArrayResponseWithContinuation` which actually were not used by SDK users

## 1.0.0b1 (2025-12-15)

### Other Changes

  - Initial version