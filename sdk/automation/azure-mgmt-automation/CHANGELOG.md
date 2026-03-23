## tsp migration

### Breaking Changes

- Deleted or renamed client method `AutomationClient.convert_graph_runbook_content`
- Method `NodeCountInformationOperations.get` changed from `asynchronous` to `synchronous`
- Method `SoftwareUpdateConfigurationsOperations.list` changed from `asynchronous` to `synchronous`
- Model `Activity` deleted or renamed its instance variable `definition`
- Model `Activity` deleted or renamed its instance variable `parameter_sets`
- Model `Activity` deleted or renamed its instance variable `output_types`
- Model `Activity` deleted or renamed its instance variable `creation_time`
- Model `Activity` deleted or renamed its instance variable `last_modified_time`
- Model `Activity` deleted or renamed its instance variable `description`
- Model `AgentRegistration` deleted or renamed its instance variable `keys`
- Model `AutomationAccount` deleted or renamed its instance variable `sku`
- Model `AutomationAccount` deleted or renamed its instance variable `last_modified_by`
- Model `AutomationAccount` deleted or renamed its instance variable `state`
- Model `AutomationAccount` deleted or renamed its instance variable `creation_time`
- Model `AutomationAccount` deleted or renamed its instance variable `last_modified_time`
- Model `AutomationAccount` deleted or renamed its instance variable `description`
- Model `AutomationAccount` deleted or renamed its instance variable `encryption`
- Model `AutomationAccount` deleted or renamed its instance variable `private_endpoint_connections`
- Model `AutomationAccount` deleted or renamed its instance variable `public_network_access`
- Model `AutomationAccount` deleted or renamed its instance variable `disable_local_auth`
- Model `AutomationAccount` deleted or renamed its instance variable `automation_hybrid_service_url`
- Model `AutomationAccountCreateOrUpdateParameters` deleted or renamed its instance variable `sku`
- Model `AutomationAccountCreateOrUpdateParameters` deleted or renamed its instance variable `encryption`
- Model `AutomationAccountCreateOrUpdateParameters` deleted or renamed its instance variable `public_network_access`
- Model `AutomationAccountCreateOrUpdateParameters` deleted or renamed its instance variable `disable_local_auth`
- Model `AutomationAccountUpdateParameters` deleted or renamed its instance variable `sku`
- Model `AutomationAccountUpdateParameters` deleted or renamed its instance variable `encryption`
- Model `AutomationAccountUpdateParameters` deleted or renamed its instance variable `public_network_access`
- Model `AutomationAccountUpdateParameters` deleted or renamed its instance variable `disable_local_auth`
- Model `Certificate` deleted or renamed its instance variable `thumbprint`
- Model `Certificate` deleted or renamed its instance variable `expiry_time`
- Model `Certificate` deleted or renamed its instance variable `is_exportable`
- Model `Certificate` deleted or renamed its instance variable `creation_time`
- Model `Certificate` deleted or renamed its instance variable `last_modified_time`
- Model `Certificate` deleted or renamed its instance variable `description`
- Model `CertificateCreateOrUpdateParameters` deleted or renamed its instance variable `base64_value`
- Model `CertificateCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `CertificateCreateOrUpdateParameters` deleted or renamed its instance variable `thumbprint`
- Model `CertificateCreateOrUpdateParameters` deleted or renamed its instance variable `is_exportable`
- Model `CertificateUpdateParameters` deleted or renamed its instance variable `description`
- Model `Connection` deleted or renamed its instance variable `connection_type`
- Model `Connection` deleted or renamed its instance variable `field_definition_values`
- Model `Connection` deleted or renamed its instance variable `creation_time`
- Model `Connection` deleted or renamed its instance variable `last_modified_time`
- Model `Connection` deleted or renamed its instance variable `description`
- Model `ConnectionCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `ConnectionCreateOrUpdateParameters` deleted or renamed its instance variable `connection_type`
- Model `ConnectionCreateOrUpdateParameters` deleted or renamed its instance variable `field_definition_values`
- Model `ConnectionType` deleted or renamed its instance variable `is_global`
- Model `ConnectionType` deleted or renamed its instance variable `field_definitions`
- Model `ConnectionType` deleted or renamed its instance variable `creation_time`
- Model `ConnectionType` deleted or renamed its instance variable `last_modified_time`
- Model `ConnectionType` deleted or renamed its instance variable `description`
- Model `ConnectionTypeCreateOrUpdateParameters` deleted or renamed its instance variable `is_global`
- Model `ConnectionTypeCreateOrUpdateParameters` deleted or renamed its instance variable `field_definitions`
- Model `ConnectionUpdateParameters` deleted or renamed its instance variable `description`
- Model `ConnectionUpdateParameters` deleted or renamed its instance variable `field_definition_values`
- Model `Credential` deleted or renamed its instance variable `user_name`
- Model `Credential` deleted or renamed its instance variable `creation_time`
- Model `Credential` deleted or renamed its instance variable `last_modified_time`
- Model `Credential` deleted or renamed its instance variable `description`
- Model `CredentialCreateOrUpdateParameters` deleted or renamed its instance variable `user_name`
- Model `CredentialCreateOrUpdateParameters` deleted or renamed its instance variable `password`
- Model `CredentialCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `CredentialUpdateParameters` deleted or renamed its instance variable `user_name`
- Model `CredentialUpdateParameters` deleted or renamed its instance variable `password`
- Model `CredentialUpdateParameters` deleted or renamed its instance variable `description`
- Model `DeletedAutomationAccount` deleted or renamed its instance variable `automation_account_resource_id`
- Model `DeletedAutomationAccount` deleted or renamed its instance variable `automation_account_id`
- Model `DeletedAutomationAccount` deleted or renamed its instance variable `location_properties_location`
- Model `DeletedAutomationAccount` deleted or renamed its instance variable `deletion_time`
- Model `DeletedRunbook` deleted or renamed its instance variable `runbook_id`
- Model `DeletedRunbook` deleted or renamed its instance variable `runbook_type`
- Model `DeletedRunbook` deleted or renamed its instance variable `runtime`
- Model `DeletedRunbook` deleted or renamed its instance variable `runtime_environment`
- Model `DeletedRunbook` deleted or renamed its instance variable `creation_time`
- Model `DeletedRunbook` deleted or renamed its instance variable `deletion_time`
- Model `DscConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `DscConfiguration` deleted or renamed its instance variable `job_count`
- Model `DscConfiguration` deleted or renamed its instance variable `parameters`
- Model `DscConfiguration` deleted or renamed its instance variable `source`
- Model `DscConfiguration` deleted or renamed its instance variable `state`
- Model `DscConfiguration` deleted or renamed its instance variable `log_verbose`
- Model `DscConfiguration` deleted or renamed its instance variable `creation_time`
- Model `DscConfiguration` deleted or renamed its instance variable `last_modified_time`
- Model `DscConfiguration` deleted or renamed its instance variable `node_configuration_count`
- Model `DscConfiguration` deleted or renamed its instance variable `description`
- Model `DscConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `log_verbose`
- Model `DscConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `log_progress`
- Model `DscConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `source`
- Model `DscConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `parameters`
- Model `DscConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `DscConfigurationUpdateParameters` deleted or renamed its instance variable `log_verbose`
- Model `DscConfigurationUpdateParameters` deleted or renamed its instance variable `log_progress`
- Model `DscConfigurationUpdateParameters` deleted or renamed its instance variable `source`
- Model `DscConfigurationUpdateParameters` deleted or renamed its instance variable `parameters`
- Model `DscConfigurationUpdateParameters` deleted or renamed its instance variable `description`
- Model `DscNode` deleted or renamed its instance variable `last_seen`
- Model `DscNode` deleted or renamed its instance variable `registration_time`
- Model `DscNode` deleted or renamed its instance variable `ip`
- Model `DscNode` deleted or renamed its instance variable `account_id`
- Model `DscNode` deleted or renamed its instance variable `status`
- Model `DscNode` deleted or renamed its instance variable `node_id`
- Model `DscNode` deleted or renamed its instance variable `etag`
- Model `DscNode` deleted or renamed its instance variable `total_count`
- Model `DscNode` deleted or renamed its instance variable `extension_handler`
- Model `DscNode` deleted or renamed its instance variable `name_properties_node_configuration_name`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `last_modified_time`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `creation_time`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `configuration`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `source`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `node_count`
- Model `DscNodeConfiguration` deleted or renamed its instance variable `increment_node_configuration_build`
- Model `DscNodeConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `source`
- Model `DscNodeConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `configuration`
- Model `DscNodeConfigurationCreateOrUpdateParameters` deleted or renamed its instance variable `increment_node_configuration_build`
- Model `DscNodeUpdateParametersProperties` deleted or renamed its instance variable `name`
- Model `ErrorResponse` deleted or renamed its instance variable `code`
- Model `ErrorResponse` deleted or renamed its instance variable `message`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `ip`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `registered_date_time`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `last_seen_date_time`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `vm_resource_id`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `worker_type`
- Model `HybridRunbookWorker` deleted or renamed its instance variable `worker_name`
- Model `HybridRunbookWorkerCreateParameters` deleted or renamed its instance variable `vm_resource_id`
- Model `HybridRunbookWorkerGroup` deleted or renamed its instance variable `group_type`
- Model `HybridRunbookWorkerGroup` deleted or renamed its instance variable `credential`
- Model `HybridRunbookWorkerGroupCreateOrUpdateParameters` deleted or renamed its instance variable `credential`
- Model `Job` deleted or renamed its instance variable `runbook`
- Model `Job` deleted or renamed its instance variable `started_by`
- Model `Job` deleted or renamed its instance variable `run_on`
- Model `Job` deleted or renamed its instance variable `job_runtime_environment`
- Model `Job` deleted or renamed its instance variable `job_id`
- Model `Job` deleted or renamed its instance variable `creation_time`
- Model `Job` deleted or renamed its instance variable `status`
- Model `Job` deleted or renamed its instance variable `status_details`
- Model `Job` deleted or renamed its instance variable `start_time`
- Model `Job` deleted or renamed its instance variable `end_time`
- Model `Job` deleted or renamed its instance variable `exception`
- Model `Job` deleted or renamed its instance variable `last_modified_time`
- Model `Job` deleted or renamed its instance variable `last_status_modified_time`
- Model `Job` deleted or renamed its instance variable `parameters`
- Model `Job` deleted or renamed its instance variable `provisioning_state`
- Model `JobCollectionItem` deleted or renamed its instance variable `runbook`
- Model `JobCollectionItem` deleted or renamed its instance variable `job_id`
- Model `JobCollectionItem` deleted or renamed its instance variable `started_by`
- Model `JobCollectionItem` deleted or renamed its instance variable `creation_time`
- Model `JobCollectionItem` deleted or renamed its instance variable `status`
- Model `JobCollectionItem` deleted or renamed its instance variable `start_time`
- Model `JobCollectionItem` deleted or renamed its instance variable `end_time`
- Model `JobCollectionItem` deleted or renamed its instance variable `last_modified_time`
- Model `JobCollectionItem` deleted or renamed its instance variable `provisioning_state`
- Model `JobCollectionItem` deleted or renamed its instance variable `job_runtime_environment`
- Model `JobCollectionItem` deleted or renamed its instance variable `run_on`
- Model `JobCreateParameters` deleted or renamed its instance variable `runbook`
- Model `JobCreateParameters` deleted or renamed its instance variable `parameters`
- Model `JobCreateParameters` deleted or renamed its instance variable `run_on`
- Model `JobSchedule` deleted or renamed its instance variable `job_schedule_id`
- Model `JobSchedule` deleted or renamed its instance variable `schedule`
- Model `JobSchedule` deleted or renamed its instance variable `runbook`
- Model `JobSchedule` deleted or renamed its instance variable `run_on`
- Model `JobSchedule` deleted or renamed its instance variable `parameters`
- Model `JobScheduleCreateParameters` deleted or renamed its instance variable `schedule`
- Model `JobScheduleCreateParameters` deleted or renamed its instance variable `runbook`
- Model `JobScheduleCreateParameters` deleted or renamed its instance variable `run_on`
- Model `JobScheduleCreateParameters` deleted or renamed its instance variable `parameters`
- Model `JobStream` deleted or renamed its instance variable `job_stream_id`
- Model `JobStream` deleted or renamed its instance variable `time`
- Model `JobStream` deleted or renamed its instance variable `stream_type`
- Model `JobStream` deleted or renamed its instance variable `stream_text`
- Model `JobStream` deleted or renamed its instance variable `summary`
- Model `JobStream` deleted or renamed its instance variable `value`
- Model `KeyListResult` deleted or renamed its instance variable `keys`
- Model `Module` deleted or renamed its instance variable `is_global`
- Model `Module` deleted or renamed its instance variable `version`
- Model `Module` deleted or renamed its instance variable `size_in_bytes`
- Model `Module` deleted or renamed its instance variable `activity_count`
- Model `Module` deleted or renamed its instance variable `provisioning_state`
- Model `Module` deleted or renamed its instance variable `content_link`
- Model `Module` deleted or renamed its instance variable `error`
- Model `Module` deleted or renamed its instance variable `creation_time`
- Model `Module` deleted or renamed its instance variable `last_modified_time`
- Model `Module` deleted or renamed its instance variable `description`
- Model `Module` deleted or renamed its instance variable `is_composite`
- Model `ModuleCreateOrUpdateParameters` deleted or renamed its instance variable `content_link`
- Model `ModuleUpdateParameters` deleted or renamed its instance variable `content_link`
- Model `Operation` deleted or renamed its instance variable `service_specification`
- Model `Package` deleted or renamed its instance variable `default`
- Model `Package` deleted or renamed its instance variable `version`
- Model `Package` deleted or renamed its instance variable `size_in_bytes`
- Model `Package` deleted or renamed its instance variable `provisioning_state`
- Model `Package` deleted or renamed its instance variable `content_link`
- Model `Package` deleted or renamed its instance variable `error`
- Model `Package` deleted or renamed its instance variable `all_of`
- Model `PackageCreateOrUpdateParameters` deleted or renamed its instance variable `content_link`
- Model `PackageUpdateParameters` deleted or renamed its instance variable `content_link`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `private_endpoint`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `group_ids`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `private_link_service_connection_state`
- Model `PrivateLinkResource` deleted or renamed its instance variable `group_id`
- Model `PrivateLinkResource` deleted or renamed its instance variable `required_members`
- Model `PythonPackageCreateParameters` deleted or renamed its instance variable `content_link`
- Model `Runbook` deleted or renamed its instance variable `runtime_environment`
- Model `Runbook` deleted or renamed its instance variable `runbook_type`
- Model `Runbook` deleted or renamed its instance variable `publish_content_link`
- Model `Runbook` deleted or renamed its instance variable `state`
- Model `Runbook` deleted or renamed its instance variable `log_verbose`
- Model `Runbook` deleted or renamed its instance variable `log_progress`
- Model `Runbook` deleted or renamed its instance variable `log_activity_trace`
- Model `Runbook` deleted or renamed its instance variable `job_count`
- Model `Runbook` deleted or renamed its instance variable `parameters`
- Model `Runbook` deleted or renamed its instance variable `output_types`
- Model `Runbook` deleted or renamed its instance variable `draft`
- Model `Runbook` deleted or renamed its instance variable `provisioning_state`
- Model `Runbook` deleted or renamed its instance variable `last_modified_by`
- Model `Runbook` deleted or renamed its instance variable `creation_time`
- Model `Runbook` deleted or renamed its instance variable `last_modified_time`
- Model `Runbook` deleted or renamed its instance variable `description`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `log_verbose`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `log_progress`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `runtime_environment`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `runbook_type`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `draft`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `publish_content_link`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `RunbookCreateOrUpdateParameters` deleted or renamed its instance variable `log_activity_trace`
- Model `RunbookUpdateParameters` deleted or renamed its instance variable `description`
- Model `RunbookUpdateParameters` deleted or renamed its instance variable `log_verbose`
- Model `RunbookUpdateParameters` deleted or renamed its instance variable `log_progress`
- Model `RunbookUpdateParameters` deleted or renamed its instance variable `log_activity_trace`
- Model `RuntimeEnvironment` deleted or renamed its instance variable `default_packages`
- Model `RuntimeEnvironment` deleted or renamed its instance variable `description`
- Model `RuntimeEnvironment` deleted or renamed its instance variable `language`
- Model `RuntimeEnvironment` deleted or renamed its instance variable `version`
- Model `RuntimeEnvironmentUpdateParameters` deleted or renamed its instance variable `default_packages`
- Model `Schedule` deleted or renamed its instance variable `start_time`
- Model `Schedule` deleted or renamed its instance variable `start_time_offset_minutes`
- Model `Schedule` deleted or renamed its instance variable `expiry_time`
- Model `Schedule` deleted or renamed its instance variable `expiry_time_offset_minutes`
- Model `Schedule` deleted or renamed its instance variable `is_enabled`
- Model `Schedule` deleted or renamed its instance variable `next_run`
- Model `Schedule` deleted or renamed its instance variable `next_run_offset_minutes`
- Model `Schedule` deleted or renamed its instance variable `interval`
- Model `Schedule` deleted or renamed its instance variable `frequency`
- Model `Schedule` deleted or renamed its instance variable `time_zone`
- Model `Schedule` deleted or renamed its instance variable `advanced_schedule`
- Model `Schedule` deleted or renamed its instance variable `creation_time`
- Model `Schedule` deleted or renamed its instance variable `last_modified_time`
- Model `Schedule` deleted or renamed its instance variable `description`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `start_time`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `expiry_time`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `interval`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `frequency`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `time_zone`
- Model `ScheduleCreateOrUpdateParameters` deleted or renamed its instance variable `advanced_schedule`
- Model `ScheduleUpdateParameters` deleted or renamed its instance variable `description`
- Model `ScheduleUpdateParameters` deleted or renamed its instance variable `is_enabled`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `update_configuration`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `schedule_info`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `error`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `creation_time`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `created_by`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `last_modified_time`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `last_modified_by`
- Model `SoftwareUpdateConfiguration` deleted or renamed its instance variable `tasks`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `update_configuration`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `tasks`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `frequency`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `start_time`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `creation_time`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `last_modified_time`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `provisioning_state`
- Model `SoftwareUpdateConfigurationCollectionItem` deleted or renamed its instance variable `next_run`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `target_computer`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `target_computer_type`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `software_update_configuration`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `status`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `os_type`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `correlation_id`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `source_computer_id`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `start_time`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `end_time`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `configured_duration`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `job`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `creation_time`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `created_by`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `last_modified_time`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `last_modified_by`
- Model `SoftwareUpdateConfigurationMachineRun` deleted or renamed its instance variable `error`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `software_update_configuration`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `status`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `configured_duration`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `os_type`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `start_time`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `end_time`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `computer_count`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `failed_count`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `creation_time`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `created_by`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `last_modified_time`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `last_modified_by`
- Model `SoftwareUpdateConfigurationRun` deleted or renamed its instance variable `tasks`
- Model `SourceControl` deleted or renamed its instance variable `repo_url`
- Model `SourceControl` deleted or renamed its instance variable `branch`
- Model `SourceControl` deleted or renamed its instance variable `folder_path`
- Model `SourceControl` deleted or renamed its instance variable `auto_sync`
- Model `SourceControl` deleted or renamed its instance variable `publish_runbook`
- Model `SourceControl` deleted or renamed its instance variable `source_type`
- Model `SourceControl` deleted or renamed its instance variable `description`
- Model `SourceControl` deleted or renamed its instance variable `creation_time`
- Model `SourceControl` deleted or renamed its instance variable `last_modified_time`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `repo_url`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `branch`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `folder_path`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `auto_sync`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `publish_runbook`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `source_type`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `security_token`
- Model `SourceControlCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `source_control_sync_job_id`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `creation_time`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `provisioning_state`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `start_time`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `end_time`
- Model `SourceControlSyncJob` deleted or renamed its instance variable `sync_type`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `source_control_sync_job_id`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `creation_time`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `provisioning_state`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `start_time`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `end_time`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `sync_type`
- Model `SourceControlSyncJobById` deleted or renamed its instance variable `exception`
- Model `SourceControlSyncJobCreateParameters` deleted or renamed its instance variable `commit_id`
- Model `SourceControlSyncJobStream` deleted or renamed its instance variable `source_control_sync_job_stream_id`
- Model `SourceControlSyncJobStream` deleted or renamed its instance variable `summary`
- Model `SourceControlSyncJobStream` deleted or renamed its instance variable `time`
- Model `SourceControlSyncJobStream` deleted or renamed its instance variable `stream_type`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `source_control_sync_job_stream_id`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `summary`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `time`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `stream_type`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `stream_text`
- Model `SourceControlSyncJobStreamById` deleted or renamed its instance variable `value`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `branch`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `folder_path`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `auto_sync`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `publish_runbook`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `security_token`
- Model `SourceControlUpdateParameters` deleted or renamed its instance variable `description`
- Model `Variable` deleted or renamed its instance variable `value`
- Model `Variable` deleted or renamed its instance variable `is_encrypted`
- Model `Variable` deleted or renamed its instance variable `creation_time`
- Model `Variable` deleted or renamed its instance variable `last_modified_time`
- Model `Variable` deleted or renamed its instance variable `description`
- Model `VariableCreateOrUpdateParameters` deleted or renamed its instance variable `value`
- Model `VariableCreateOrUpdateParameters` deleted or renamed its instance variable `description`
- Model `VariableCreateOrUpdateParameters` deleted or renamed its instance variable `is_encrypted`
- Model `VariableUpdateParameters` deleted or renamed its instance variable `value`
- Model `VariableUpdateParameters` deleted or renamed its instance variable `description`
- Model `Watcher` deleted or renamed its instance variable `execution_frequency_in_seconds`
- Model `Watcher` deleted or renamed its instance variable `script_name`
- Model `Watcher` deleted or renamed its instance variable `script_parameters`
- Model `Watcher` deleted or renamed its instance variable `script_run_on`
- Model `Watcher` deleted or renamed its instance variable `status`
- Model `Watcher` deleted or renamed its instance variable `creation_time`
- Model `Watcher` deleted or renamed its instance variable `last_modified_time`
- Model `Watcher` deleted or renamed its instance variable `last_modified_by`
- Model `Watcher` deleted or renamed its instance variable `description`
- Model `WatcherUpdateParameters` deleted or renamed its instance variable `execution_frequency_in_seconds`
- Model `Webhook` deleted or renamed its instance variable `is_enabled`
- Model `Webhook` deleted or renamed its instance variable `uri`
- Model `Webhook` deleted or renamed its instance variable `expiry_time`
- Model `Webhook` deleted or renamed its instance variable `last_invoked_time`
- Model `Webhook` deleted or renamed its instance variable `parameters`
- Model `Webhook` deleted or renamed its instance variable `runbook`
- Model `Webhook` deleted or renamed its instance variable `run_on`
- Model `Webhook` deleted or renamed its instance variable `creation_time`
- Model `Webhook` deleted or renamed its instance variable `last_modified_time`
- Model `Webhook` deleted or renamed its instance variable `last_modified_by`
- Model `Webhook` deleted or renamed its instance variable `description`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `is_enabled`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `uri`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `expiry_time`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `parameters`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `runbook`
- Model `WebhookCreateOrUpdateParameters` deleted or renamed its instance variable `run_on`
- Model `WebhookUpdateParameters` deleted or renamed its instance variable `is_enabled`
- Model `WebhookUpdateParameters` deleted or renamed its instance variable `run_on`
- Model `WebhookUpdateParameters` deleted or renamed its instance variable `parameters`
- Model `WebhookUpdateParameters` deleted or renamed its instance variable `description`
- Deleted or renamed model `JobListResultV2`
- Deleted or renamed model `NodeCounts`
- Deleted or renamed model `RunbookCreateOrUpdateDraftParameters`
- Deleted or renamed model `RunbookCreateOrUpdateDraftProperties`
- Deleted or renamed model `SourceControlSyncJobStreamsListBySyncJob`
- Method `DscConfigurationOperations.list_by_automation_account` changed its parameter `inlinecount` from `positional_or_keyword` to `keyword_only`
- Method `DscNodeConfigurationOperations.list_by_automation_account` changed its parameter `inlinecount` from `positional_or_keyword` to `keyword_only`
- Method `DscNodeOperations.list_by_automation_account` changed its parameter `inlinecount` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.create` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.get` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.get_output` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.get_runbook_content` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.list_by_automation_account` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.resume` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.stop` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobOperations.suspend` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobStreamOperations.get` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `JobStreamOperations.list_by_job` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationMachineRunsOperations.get_by_id` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationMachineRunsOperations.list` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationRunsOperations.get_by_id` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationRunsOperations.list` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationsOperations.create` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationsOperations.delete` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationsOperations.get_by_name` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Method `SoftwareUpdateConfigurationsOperations.list` changed its parameter `client_request_id` from `positional_or_keyword` to `keyword_only`
- Deleted or renamed model `DeletedAutomationAccountsOperations`

# Release History

## 1.1.0 (2026-03-23)

change log generation failed!!! You need to write it manually!!!

## 1.1.0b4 (2024-11-05)

### Other Changes

  - Update dependencies

## 1.1.0b3 (2022-12-12)

### Features Added

  - Added operation group DeletedAutomationAccountsOperations
  - Added operation group Python3PackageOperations
  - Model HybridRunbookWorkerGroupCreateOrUpdateParameters has a new parameter name
  - Model Operation has a new parameter origin
  - Model Operation has a new parameter service_specification
  - Model OperationDisplay has a new parameter description

### Breaking Changes

  - Model HybridRunbookWorkerGroup no longer has parameter hybrid_runbook_workers
  - Operation DscConfigurationOperations.create_or_update no longer has parameter content_type
  - Operation DscConfigurationOperations.update no longer has parameter content_type
  - Operation HybridRunbookWorkerGroupOperations.update has a new required parameter hybrid_runbook_worker_group_updation_parameters
  - Operation HybridRunbookWorkerGroupOperations.update no longer has parameter parameters

## 1.1.0b2 (2022-07-18)

**Features**

  - Added operation HybridRunbookWorkerGroupOperations.create
  - Added operation group AutomationClientOperationsMixin
  - Added operation group HybridRunbookWorkersOperations
  - Added operation group PrivateEndpointConnectionsOperations
  - Added operation group PrivateLinkResourcesOperations
  - Model AutomationAccount has a new parameter automation_hybrid_service_url
  - Model AutomationAccount has a new parameter disable_local_auth
  - Model AutomationAccount has a new parameter encryption
  - Model AutomationAccount has a new parameter identity
  - Model AutomationAccount has a new parameter private_endpoint_connections
  - Model AutomationAccount has a new parameter public_network_access
  - Model AutomationAccount has a new parameter system_data
  - Model AutomationAccountCreateOrUpdateParameters has a new parameter disable_local_auth
  - Model AutomationAccountCreateOrUpdateParameters has a new parameter encryption
  - Model AutomationAccountCreateOrUpdateParameters has a new parameter identity
  - Model AutomationAccountCreateOrUpdateParameters has a new parameter public_network_access
  - Model AutomationAccountUpdateParameters has a new parameter disable_local_auth
  - Model AutomationAccountUpdateParameters has a new parameter encryption
  - Model AutomationAccountUpdateParameters has a new parameter identity
  - Model AutomationAccountUpdateParameters has a new parameter public_network_access
  - Model HybridRunbookWorker has a new parameter id
  - Model HybridRunbookWorker has a new parameter registered_date_time
  - Model HybridRunbookWorker has a new parameter system_data
  - Model HybridRunbookWorker has a new parameter type
  - Model HybridRunbookWorker has a new parameter vm_resource_id
  - Model HybridRunbookWorker has a new parameter worker_name
  - Model HybridRunbookWorker has a new parameter worker_type
  - Model HybridRunbookWorkerGroup has a new parameter system_data
  - Model HybridRunbookWorkerGroup has a new parameter type
  - Operation DscConfigurationOperations.create_or_update has a new optional and keyword-only parameter content_type
  - Operation DscConfigurationOperations.update has a new optional and keyword-only parameter content_type

**Breaking changes**

  - Model HybridRunbookWorker no longer has parameter registration_time

## 1.1.0b1 (2021-03-16)

**Features**

  - Model SoftwareUpdateConfigurationCollectionItem has a new parameter tasks

## 1.0.0 (2020-12-17)

- GA release

## 1.0.0b1 (2020-11-11)

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

## 0.1.1 (2019-05-13)

**Bugfixes**

  - Remove incorrect "count_type1" parameter from client signature
    #4965

## 0.1.0 (2019-04-16)

  - Initial Release
