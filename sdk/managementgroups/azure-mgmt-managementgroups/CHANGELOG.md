# Release History

## 1.0.0b1 (Unreleased)

### Breaking Changes

  - Renamed client name `ManagementGroupsAPI` to `ManagementGroupsMgmtClient`
  - Deleted or renamed model `AzureAsyncOperationResults`
  - Method `ManagementGroupSubscriptionsOperations.get_subscription` renamed its parameter from `subscription_id` to `group_id`
  - Deleted model `HierarchySettingsList`/`ListSubscriptionUnderManagementGroup` which actually were not used by SDK users
  - Model `CreateManagementGroupRequest` moved instance variables `tenant_id`, `display_name`, `details` and `children` under property `properties`
  - Model `CreateOrUpdateSettingsRequest` moved instance variables `require_authorization_for_group_creation` and `default_management_group` under property `properties`
  - Model `DescendantInfo` moved instance variables `display_name` and `parent` under property `properties`
  - Model `EntityInfo` moved instance variables `tenant_id`, `display_name`, `parent`, `permissions`, `inherited_permissions`, `number_of_descendants`, `number_of_children`, `number_of_child_groups`, `parent_display_name_chain` and `parent_name_chain` under property `properties`
  - Model `HierarchySettings` moved instance variables `tenant_id`, `require_authorization_for_group_creation` and `default_management_group` under property `properties`
  - Model `HierarchySettingsInfo` moved instance variables `tenant_id`, `require_authorization_for_group_creation` and `default_management_group` under property `properties`
  - Model `ManagementGroup` moved instance variables `tenant_id`, `display_name`, `details` and `children` under property `properties`
  - Model `ManagementGroupInfo` moved instance variables `tenant_id` and `display_name` under property `properties`
  - Model `SubscriptionUnderManagementGroup` moved instance variables `tenant`, `display_name`, `parent` and `state` under property `properties`
  - Method `EntitiesOperations.list` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `EntitiesOperations.list` changed its parameter `select` from `positional_or_keyword` to `keyword_only`
  - Method `EntitiesOperations.list` changed its parameter `search` from `positional_or_keyword` to `keyword_only`
  - Method `EntitiesOperations.list` changed its parameter `view` from `positional_or_keyword` to `keyword_only`
  - Method `EntitiesOperations.list` changed its parameter `group_name` from `positional_or_keyword` to `keyword_only`
  - Method `EntitiesOperations.list` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupSubscriptionsOperations.create` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupSubscriptionsOperations.create` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ManagementGroupSubscriptionsOperations.delete` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupSubscriptionsOperations.delete` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ManagementGroupSubscriptionsOperations.get_subscription` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupSubscriptionsOperations.get_subscriptions_under_management_group` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.begin_create_or_update` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.begin_delete` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.get` changed its parameter `recurse` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.get` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.get_descendants` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.list` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.list` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `ManagementGroupsOperations.update` changed its parameter `cache_control` from `positional_or_keyword` to `keyword_only`


## 1.1.0b2 (2024-11-05)

### Other Changes

  - Update dependencies

## 1.1.0b1 (2022-11-01)

### Features Added

  - Added model EntitySearchType
  - Added model EntityViewParameterType
  - Added model ManagementGroupExpandType
  - Added model ParentGroupBagInfo

## 1.0.0 (2021-05-21)

**Features**

  - Model ManagementGroupDetails has a new parameter path
  - Model ManagementGroupDetails has a new parameter management_group_ancestors
  - Model ManagementGroupDetails has a new parameter management_group_ancestors_chain

**Breaking changes**

  - Operation ManagementGroupSubscriptionsOperations.get_subscriptions_under_management_group has a new signature
  - Operation ManagementGroupsOperations.list has a new signature
  - Operation EntitiesOperations.list has a new signature
  - Operation ManagementGroupsOperations.get_descendants has a new signature
  - Model ManagementGroup no longer has parameter path

## 1.0.0b1 (2020-12-09)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 0.2.0 (2019-02-21)

**Features**

  - Model EntityInfo has a new parameter number_of_children
  - Model EntityInfo has a new parameter number_of_child_groups

## 0.1.0 (2018-05-31)

  - Initial Release
