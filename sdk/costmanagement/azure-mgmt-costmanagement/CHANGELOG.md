# Release History

## 6.0.0 (2025-11-28)

### Breaking Changes

  - Deleted or renamed enum value `Term.P1_Y`
  - Deleted or renamed enum value `Term.P3_Y`
  - Model `BudgetComparisonExpression` renamed its instance variable `values` to `values_property`
  - Model `SourceCostAllocationResource` renamed its instance variable `values` to `values_property`
  - Model `TargetCostAllocationResource` renamed its instance variable `values` to `values_property`
  - Model `ForecastComparisonExpression` renamed its instance variable `values` to `values_property`
  - Model `ReportConfigComparisonExpression` renamed its instance variable `values` to `values_property`
  - Model `QueryComparisonExpression` renamed its instance variable `values` to `values_property`
  - Model `Alert` moved instance variable `definition`, `description`, `source`, `details`, `cost_entity_id`, `status`, `creation_time`, `close_time`, `modification_time`, `status_modification_user_name` and `status_modification_time` under property `properties`
  - Model `Budget` moved instance variable `category`, `amount`, `time_grain`, `time_period`, `filter`, `current_spend`, `notifications` and `forecast_spend` under property `properties`
  - Model `CostDetailsOperationResults` moved instance variable `manifest_version`, `data_format`, `byte_count`, `blob_count`, `compress_data`, `blobs`, `request_scope` and `request_body` under property `properties`
  - Model `Dimension` moved instance variable `description`, `filter_enabled`, `grouping_enabled`, `data`, `total`, `category`, `usage_start`, `usage_end` and `next_link` under property `properties`
  - Model `DismissAlertPayload` moved instance variable `definition`, `description`, `source`, `details`, `cost_entity_id`, `status`, `creation_time`, `close_time`, `modification_time`, `status_modification_user_name` and `status_modification_time` under property `properties`
  - Model `Export` moved instance variable `format`, `delivery_info`, `definition`, `run_history`, `partition_data`, `data_overwrite_behavior`, `compression_mode`, `export_description`, `next_run_time_estimate`, `system_suspension_context` and `schedule` under property `properties`
  - Model `ExportRun` moved instance variable `execution_type`, `status`, `submitted_by`, `submitted_time`, `processing_start_time`, `processing_end_time`, `start_date`, `end_date`, `file_name`, `manifest_file`, `run_settings` and `error` under property `properties`
  - Model `ForecastResult` moved instance variable `next_link`, `columns` and `rows` under property `properties`
  - Model `GenerateDetailedCostReportOperationResult` moved instance variable `expiry_time`, `valid_till` and `download_url` under property `properties`
  - Model `GenerateDetailedCostReportOperationStatuses` moved instance variable `expiry_time`, `valid_till` and `download_url` under property `properties`
  - Model `IncludedQuantityUtilizationSummary` moved instance variable `arm_sku_name`, `benefit_id`, `benefit_order_id`, `benefit_type`, `usage_date` and `utilization_percentage` under property `properties`
  - Model `OperationStatus` moved instance variable `report_url` and `valid_until` under property `properties`
  - Model `QueryResult` moved instance variable `next_link`, `columns` and `rows` under property `properties`
  - Model `SavingsPlanUtilizationSummary` moved instance variable `arm_sku_name`, `benefit_id`, `benefit_order_id`, `benefit_type`, `usage_date`, `avg_utilization_percentage`, `min_utilization_percentage` and `max_utilization_percentage` under property `properties`
  - Model `ScheduledAction` moved instance variable `display_name`, `file_destination`, `notification`, `notification_email`, `schedule`, `scope`, `status` and `view_id` under property `properties`
  - Model `View` moved instance variable `display_name`, `scope`, `created_on`, `modified_on`, `date_range`, `currency`, `chart`, `accumulated`, `metric`, `kpis`, `pivots`, `type_properties_query_type`, `timeframe`, `time_period`, `data_set` and `include_monetary_commitment` under property `properties`
  - Method `BenefitRecommendationsOperations.list` changed its parameter `orderby` from `positional_or_keyword` to `keyword_only`
  - Method `BenefitRecommendationsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `BenefitUtilizationSummariesOperations.list_by_billing_account_id` changed its parameter `grain_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `BenefitUtilizationSummariesOperations.list_by_billing_profile_id` changed its parameter `grain_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `BenefitUtilizationSummariesOperations.list_by_savings_plan_id` changed its parameter `grain_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `BenefitUtilizationSummariesOperations.list_by_savings_plan_order` changed its parameter `grain_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `DimensionsOperations.by_external_cloud_provider_type` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `DimensionsOperations.by_external_cloud_provider_type` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `DimensionsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `DimensionsOperations.list` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `ExportsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `ExportsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `GenerateReservationDetailsReportOperations.begin_by_billing_account_id` changed its parameter `start_date` from `positional_or_keyword` to `keyword_only`
  - Method `GenerateReservationDetailsReportOperations.begin_by_billing_account_id` changed its parameter `end_date` from `positional_or_keyword` to `keyword_only`
  - Method `GenerateReservationDetailsReportOperations.begin_by_billing_profile_id` changed its parameter `start_date` from `positional_or_keyword` to `keyword_only`
  - Method `GenerateReservationDetailsReportOperations.begin_by_billing_profile_id` changed its parameter `end_date` from `positional_or_keyword` to `keyword_only`
  - Method `ScheduledActionsOperations.create_or_update` deleted or renamed its parameter `if_match` of kind `positional_or_keyword`
  - Method `ScheduledActionsOperations.create_or_update_by_scope` deleted or renamed its parameter `if_match` of kind `positional_or_keyword`
  - Method `AlertsOperations.list` changed from `asynchronous` to `synchronous`
  - Method `ExportsOperations.list` changed from `asynchronous` to `synchronous`
  - Method `SettingsOperations.list` changed from `asynchronous` to `synchronous`
  - Deleted model `CostAllocationRuleList`/`EAPriceSheetProperties`/`EAPricesheetDownloadProperties`/`ErrorResponseAutoGenerated`/`KpiType`/`PivotType`/`ScheduledActionProxyResource`/`SettingTypeAutoGenerated` which actually were not used by SDK users

## 5.0.0 (2025-11-28)

### Features Added

  - Model `CostManagementClient` added parameter `cloud_setting` in method `__init__`
  - Client `CostManagementClient` added operation group `budgets`
  - Client `CostManagementClient` added operation group `settings`
  - Client `CostManagementClient` added operation group `generate_benefit_utilization_summaries_report`
  - Client `CostManagementClient` added operation group `cost_allocation_rules`
  - Model `Alert` added property `system_data`
  - Model `BenefitRecommendationModel` added property `system_data`
  - Model `BenefitResource` added property `system_data`
  - Model `BenefitUtilizationSummary` added property `system_data`
  - Model `CommonExportProperties` added property `data_overwrite_behavior`
  - Model `CommonExportProperties` added property `compression_mode`
  - Model `CommonExportProperties` added property `export_description`
  - Model `CommonExportProperties` added property `system_suspension_context`
  - Model `CostDetailsOperationResults` added property `system_data`
  - Model `DimensionsListResult` added property `next_link`
  - Model `Export` added property `identity`
  - Model `Export` added property `location`
  - Model `Export` added property `data_overwrite_behavior`
  - Model `Export` added property `compression_mode`
  - Model `Export` added property `export_description`
  - Model `Export` added property `system_suspension_context`
  - Model `Export` added property `system_data`
  - Model `ExportDatasetConfiguration` added property `data_version`
  - Model `ExportDatasetConfiguration` added property `filters`
  - Model `ExportDeliveryDestination` added property `type`
  - Model `ExportProperties` added property `data_overwrite_behavior`
  - Model `ExportProperties` added property `compression_mode`
  - Model `ExportProperties` added property `export_description`
  - Model `ExportProperties` added property `system_suspension_context`
  - Model `ExportRun` added property `start_date`
  - Model `ExportRun` added property `end_date`
  - Model `ExportRun` added property `manifest_file`
  - Enum `ExportType` added member `FOCUS_COST`
  - Enum `ExportType` added member `PRICE_SHEET`
  - Enum `ExportType` added member `RESERVATION_DETAILS`
  - Enum `ExportType` added member `RESERVATION_RECOMMENDATIONS`
  - Enum `ExportType` added member `RESERVATION_TRANSACTIONS`
  - Enum `FormatType` added member `PARQUET`
  - Model `GenerateDetailedCostReportOperationResult` added property `system_data`
  - Model `GenerateDetailedCostReportOperationStatuses` added property `system_data`
  - Enum `GranularityType` added member `MONTHLY`
  - Model `IncludedQuantityUtilizationSummary` added property `system_data`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Model `SavingsPlanUtilizationSummary` added property `system_data`
  - Enum `TimeframeType` added member `THE_CURRENT_MONTH`
  - Model `View` added property `system_data`
  - Added model `AsyncOperationStatusProperties`
  - Added model `BenefitUtilizationSummariesOperationStatus`
  - Added model `BenefitUtilizationSummariesRequest`
  - Added enum `BenefitUtilizationSummaryReportSchema`
  - Added model `Budget`
  - Added model `BudgetComparisonExpression`
  - Added model `BudgetFilter`
  - Added model `BudgetFilterProperties`
  - Added enum `BudgetNotificationOperatorType`
  - Added enum `BudgetOperatorType`
  - Added model `BudgetTimePeriod`
  - Added model `BudgetsListResult`
  - Added enum `CategoryType`
  - Added enum `CompressionModeType`
  - Added enum `CostAllocationPolicyType`
  - Added model `CostAllocationProportion`
  - Added model `CostAllocationResource`
  - Added enum `CostAllocationResourceType`
  - Added model `CostAllocationRuleCheckNameAvailabilityRequest`
  - Added model `CostAllocationRuleCheckNameAvailabilityResponse`
  - Added model `CostAllocationRuleDefinition`
  - Added model `CostAllocationRuleDetails`
  - Added model `CostAllocationRuleList`
  - Added model `CostAllocationRuleProperties`
  - Added enum `CultureCode`
  - Added model `CurrentSpend`
  - Added enum `DataOverwriteBehaviorType`
  - Added enum `DestinationType`
  - Added model `EAPriceSheetProperties`
  - Added model `EAPricesheetDownloadProperties`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDetail`
  - Added model `ErrorResponseAutoGenerated`
  - Added model `ExportRunRequest`
  - Added model `ExportSuspensionContext`
  - Added enum `FilterItemNames`
  - Added model `FilterItems`
  - Added model `ForecastSpend`
  - Added enum `Frequency`
  - Added model `MCAPriceSheetProperties`
  - Added model `Notification`
  - Added model `PricesheetDownloadProperties`
  - Added enum `Reason`
  - Added enum `RuleStatus`
  - Added model `Setting`
  - Added enum `SettingType`
  - Added enum `SettingTypeAutoGenerated`
  - Added enum `SettingsKind`
  - Added model `SettingsListResult`
  - Added model `SourceCostAllocationResource`
  - Added model `SystemAssignedServiceIdentity`
  - Added enum `SystemAssignedServiceIdentityType`
  - Added model `TagInheritanceProperties`
  - Added model `TagInheritanceSetting`
  - Added model `TargetCostAllocationResource`
  - Added enum `ThresholdType`
  - Added enum `TimeGrainType`
  - Model `PriceSheetOperations` added method `begin_download_by_billing_account`
  - Model `PriceSheetOperations` added method `begin_download_by_invoice`
  - Added model `BudgetsOperations`
  - Added model `CostAllocationRulesOperations`
  - Added model `GenerateBenefitUtilizationSummariesReportOperations`
  - Added model `SettingsOperations`

### Breaking Changes

  - Deleted or renamed method `PriceSheetOperations.begin_download`
  - Method `GenerateDetailedCostReportOperationStatusOperations.get` re-ordered its parameters from `['self', 'operation_id', 'scope', 'kwargs']` to `['self', 'scope', 'operation_id', 'kwargs']`
  - Method `GenerateDetailedCostReportOperationResultsOperations.begin_get` re-ordered its parameters from `['self', 'operation_id', 'scope', 'kwargs']` to `['self', 'scope', 'operation_id', 'kwargs']`

## 4.0.1 (2023-07-19)

### Bugs Fixed

  - Fix deserialization error for some operation when error happens

## 4.0.0 (2023-05-22)

### Features Added

  - Added operation group BenefitRecommendationsOperations
  - Added operation group BenefitUtilizationSummariesOperations
  - Added operation group GenerateCostDetailsReportOperations
  - Added operation group GenerateDetailedCostReportOperationResultsOperations
  - Added operation group GenerateDetailedCostReportOperationStatusOperations
  - Added operation group GenerateDetailedCostReportOperations
  - Added operation group PriceSheetOperations
  - Added operation group ScheduledActionsOperations
  - Model Alert has a new parameter e_tag
  - Model AlertPropertiesDetails has a new parameter company_name
  - Model AlertPropertiesDetails has a new parameter department_name
  - Model AlertPropertiesDetails has a new parameter enrollment_end_date
  - Model AlertPropertiesDetails has a new parameter enrollment_number
  - Model AlertPropertiesDetails has a new parameter enrollment_start_date
  - Model AlertPropertiesDetails has a new parameter invoicing_threshold
  - Model CommonExportProperties has a new parameter next_run_time_estimate
  - Model CommonExportProperties has a new parameter partition_data
  - Model CommonExportProperties has a new parameter run_history
  - Model Dimension has a new parameter e_tag
  - Model Dimension has a new parameter location
  - Model Dimension has a new parameter sku
  - Model Export has a new parameter next_run_time_estimate
  - Model Export has a new parameter partition_data
  - Model Export has a new parameter run_history
  - Model ExportDeliveryDestination has a new parameter sas_token
  - Model ExportDeliveryDestination has a new parameter storage_account
  - Model ExportProperties has a new parameter next_run_time_estimate
  - Model ExportProperties has a new parameter partition_data
  - Model ExportProperties has a new parameter run_history
  - Model Operation has a new parameter action_type
  - Model Operation has a new parameter is_data_action
  - Model Operation has a new parameter origin
  - Model OperationDisplay has a new parameter description
  - Operation ExportsOperations.get has a new optional parameter expand
  - Operation ExportsOperations.list has a new optional parameter expand

### Breaking Changes

  - Model Alert no longer has parameter tags
  - Model ProxyResource no longer has parameter e_tag
  - Model ReportConfigFilter no longer has parameter tag_key
  - Model ReportConfigFilter no longer has parameter tag_value
  - Model Resource no longer has parameter tags
  - Removed operation group SettingsOperations

## 4.0.0b1 (2022-11-07)

### Features Added

  - Added operation group BenefitRecommendationsOperations
  - Added operation group BenefitUtilizationSummariesOperations
  - Added operation group GenerateCostDetailsReportOperations
  - Added operation group GenerateDetailedCostReportOperationResultsOperations
  - Added operation group GenerateDetailedCostReportOperationStatusOperations
  - Added operation group GenerateDetailedCostReportOperations
  - Added operation group PriceSheetOperations
  - Added operation group ScheduledActionsOperations
  - Model Alert has a new parameter e_tag
  - Model AlertPropertiesDetails has a new parameter company_name
  - Model AlertPropertiesDetails has a new parameter department_name
  - Model AlertPropertiesDetails has a new parameter enrollment_end_date
  - Model AlertPropertiesDetails has a new parameter enrollment_number
  - Model AlertPropertiesDetails has a new parameter enrollment_start_date
  - Model AlertPropertiesDetails has a new parameter invoicing_threshold
  - Model CommonExportProperties has a new parameter next_run_time_estimate
  - Model CommonExportProperties has a new parameter partition_data
  - Model CommonExportProperties has a new parameter run_history
  - Model Dimension has a new parameter e_tag
  - Model Dimension has a new parameter location
  - Model Dimension has a new parameter sku
  - Model Export has a new parameter next_run_time_estimate
  - Model Export has a new parameter partition_data
  - Model Export has a new parameter run_history
  - Model ExportDeliveryDestination has a new parameter sas_token
  - Model ExportDeliveryDestination has a new parameter storage_account
  - Model ExportProperties has a new parameter next_run_time_estimate
  - Model ExportProperties has a new parameter partition_data
  - Model ExportProperties has a new parameter run_history
  - Model Operation has a new parameter action_type
  - Model Operation has a new parameter is_data_action
  - Model Operation has a new parameter origin
  - Model OperationDisplay has a new parameter description

### Breaking Changes

  - Model Alert no longer has parameter tags
  - Model ProxyResource no longer has parameter e_tag
  - Model ReportConfigFilter no longer has parameter tag_key
  - Model ReportConfigFilter no longer has parameter tag_value
  - Model Resource no longer has parameter tags
  - Operation ExportsOperations.get has a new parameter expand
  - Operation ExportsOperations.list has a new parameter expand
  - Removed operation group SettingsOperations

## 3.0.0 (2021-07-27)

**Breaking changes**

  - Parameter dataset of model QueryDefinition is now required
  - Parameter dataset of model ForecastDefinition is now required

## 2.0.0 (2021-06-08)

**Features**

  - Model QueryResult has a new parameter sku
  - Model QueryResult has a new parameter e_tag
  - Model QueryResult has a new parameter location
  - Model View has a new parameter date_range
  - Model View has a new parameter data_set
  - Model View has a new parameter include_monetary_commitment
  - Model View has a new parameter currency
  - Model ExportExecution has a new parameter tags
  - Added operation group GenerateReservationDetailsReportOperations
  - Added operation group SettingsOperations

**Breaking changes**

  - Parameter recurrence of model ExportSchedule is now required
  - Operation ExportsOperations.list has a new signature
  - Operation ExportsOperations.get has a new signature
  - Model Export no longer has parameter run_history
  - Model Export no longer has parameter next_run_time_estimate
  - Model View no longer has parameter dataset
  - Model ExportExecution no longer has parameter e_tag
  - Model ExportExecution no longer has parameter error
  - Model CommonExportProperties no longer has parameter run_history
  - Model CommonExportProperties no longer has parameter next_run_time_estimate
  - Model ExportProperties no longer has parameter run_history
  - Model ExportProperties no longer has parameter next_run_time_estimate
  - Model QueryFilter has a new signature
  - Model ReportConfigFilter has a new signature

## 1.0.0 (2021-02-04)

**Features**

  - Model ExportExecution has a new parameter e_tag

**Breaking changes**

  - Model ExportExecution no longer has parameter tags

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


## 0.2.0 (2020-04-08)

**Features**

  - Added operation DimensionsOperations.list
  - Added operation QueryOperations.usage

**Breaking changes**

  - Model QueryDataset no longer has parameter sorting
  - Removed operation DimensionsOperations.list_by_subscription
  - Removed operation QueryOperations.usage_by_scope

**General Breaking Changes**

This version uses a next-generation code generator that *might*
introduce breaking changes. In summary, some modules were incorrectly
visible/importable and have been renamed. This fixed several issues
caused by usage of classes that were not supposed to be used in the
first place.

  - CostManagementClient cannot be imported from
    `azure.mgmt.costmanagement.cost_management_client` anymore (import from
    `azure.mgmt.costmanagement` works like before)
  - CostManagementClientConfiguration import has been moved from
    `azure.mgmt.costmanagement.cost_management_client` to `azure.mgmt.costmanagement`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using `azure.mgmt.costmanagement.models.my_class` (import from
    `azure.mgmt.costmanagement.models` works like before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.costmanagement.operations.my_class_operations` (import from
    `azure.mgmt.costmanagement.operations` works like before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 0.1.0 (2019-05-04)

  - Initial Release
