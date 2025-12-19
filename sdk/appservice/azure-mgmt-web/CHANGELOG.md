# Release History

## tsp migration

### Breaking Changes

  - Deleted or renamed client `WebSiteManagementClient`
  - Deleted or renamed enum value `SupportedTlsVersions.ONE0`
  - Deleted or renamed enum value `SupportedTlsVersions.ONE1`
  - Deleted or renamed enum value `SupportedTlsVersions.ONE2`
  - Deleted or renamed enum value `SupportedTlsVersions.ONE3`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_AES128_GCM_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_AES256_GCM_SHA384`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES128_CBC_SHA`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES128_CBC_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES256_CBC_SHA`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES256_CBC_SHA384`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES128_CBC_SHA`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES128_CBC_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES128_GCM_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES256_CBC_SHA`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES256_CBC_SHA256`
  - Deleted or renamed enum value `TlsCipherSuites.TLS_RSA_WITH_AES256_GCM_SHA384`
  - Deleted or renamed method `WebAppsOperations.begin_swap_slot`
  - Method `RecommendationsOperations.disable_all_for_hosting_environment` re-ordered its parameters from `['self', 'resource_group_name', 'environment_name', 'hosting_environment_name', 'kwargs']` to `['self', 'resource_group_name', 'hosting_environment_name', 'environment_name', 'kwargs']`
  - Method `RecommendationsOperations.reset_all_filters_for_hosting_environment` re-ordered its parameters from `['self', 'resource_group_name', 'environment_name', 'hosting_environment_name', 'kwargs']` to `['self', 'resource_group_name', 'hosting_environment_name', 'environment_name', 'kwargs']`
  - Method `WebAppsOperations.begin_migrate_storage` re-ordered its parameters from `['self', 'resource_group_name', 'name', 'subscription_name', 'migration_options', 'kwargs']` to `['self', 'resource_group_name', 'name', 'migration_options', 'subscription_name', 'kwargs']`



  - Model `AddressResponse` moved instance variable `service_ip_address`, `internal_ip_address`, `outbound_ip_addresses` and `vip_mappings` under property `properties`
  - Model `AnalysisDefinition` moved instance variable `description` under property `properties`
  - Model `ApiKVReference` moved instance variable `reference`, `status`, `vault_name`, `secret_name`, `secret_version`, `identity_type`, `details`, `source` and `active_version` under property `properties`
  - Model `AppServiceEnvironmentPatchResource` moved instance variable `provisioning_state`, `status`, `virtual_network`, `internal_load_balancing_mode`, `multi_size`, `multi_role_count`, `ipssl_address_count`, `dns_suffix`, `maximum_number_of_machines`, `front_end_scale_factor`, `suspended`, `cluster_settings`, `user_whitelisted_ip_ranges`, `has_linux_workers`, `upgrade_preference`, `dedicated_host_count`, `zone_redundant`, `custom_dns_suffix_configuration`, `networking_configuration` and `upgrade_availability` under property `properties`
  - Model `AppServiceEnvironmentResource` moved instance variable `provisioning_state`, `status`, `virtual_network`, `internal_load_balancing_mode`, `multi_size`, `multi_role_count`, `ipssl_address_count`, `dns_suffix`, `maximum_number_of_machines`, `front_end_scale_factor`, `suspended`, `cluster_settings`, `user_whitelisted_ip_ranges`, `has_linux_workers`, `upgrade_preference`, `dedicated_host_count`, `zone_redundant`, `custom_dns_suffix_configuration`, `networking_configuration` and `upgrade_availability` under property `properties`
  - Model `AppServicePlan` moved instance variable `worker_tier_name`, `status`, `subscription`, `hosting_environment_profile`, `maximum_number_of_workers`, `number_of_workers`, `geo_region`, `per_site_scaling`, `elastic_scale_enabled`, `maximum_elastic_worker_count`, `number_of_sites`, `is_spot`, `spot_expiration_time`, `free_offer_expiration_time`, `resource_group`, `reserved`, `is_xenon`, `hyper_v`, `target_worker_count`, `target_worker_size_id`, `provisioning_state`, `kube_environment_profile`, `zone_redundant`, `async_scaling_enabled`, `plan_default_identity`, `is_custom_mode`, `registry_adapters`, `install_scripts`, `network`, `storage_mounts` and `rdp_enabled` under property `properties`
  - Model `AppServicePlanPatchResource` moved instance variable `worker_tier_name`, `status`, `subscription`, `hosting_environment_profile`, `maximum_number_of_workers`, `number_of_workers`, `geo_region`, `per_site_scaling`, `elastic_scale_enabled`, `maximum_elastic_worker_count`, `number_of_sites`, `is_spot`, `spot_expiration_time`, `free_offer_expiration_time`, `resource_group`, `reserved`, `is_xenon`, `hyper_v`, `target_worker_count`, `target_worker_size_id`, `provisioning_state`, `kube_environment_profile` and `zone_redundant` under property `properties`
  - Model `ApplicationStackResource` moved instance variable `name_properties_name`, `display`, `dependency`, `major_versions`, `frameworks`, `is_deprecated` under property `properties`
  - Model `AseRegion` moved instance variable `display_name`, `standard`, `dedicated_host`, `zone_redundant`, `available_sku`, `available_os` under property `properties`
  - Model `AseV3NetworkingConfiguration` moved instance variable `windows_outbound_ip_addresses`, `linux_outbound_ip_addresses`, `external_inbound_ip_addresses`, `internal_inbound_ip_addresses`, `allow_new_private_endpoint_connections`, `ftp_enabled`, `remote_debug_enabled`, `inbound_ip_address_override` under property `properties`
  - Model `BackupItem` moved instance variable `backup_id`, `storage_account_url`, `blob_name`, `name_properties_name`, `status`, `size_in_bytes`, `created`, `log`, `databases`, `scheduled`, `last_restore_time_stamp`, `finished_time_stamp`, `correlation_id`, `website_size_in_bytes` under property `properties`
  - Model `BackupRequest` moved instance variable `backup_name`, `enabled`, `storage_account_url`, `backup_schedule`, `databases` under property `properties`
  - Model `BillingMeter` moved instance variable `meter_id`, `billing_location`, `short_name`, `friendly_name`, `resource_type`, `os_type`, `multiplier` under property `properties`
  - Model `Certificate` moved instance variable `password`, `friendly_name`, `subject_name`, `host_names`, `pfx_blob`, `site_name`, `self_link`, `issuer`, `issue_date`, `expiration_date`, `thumbprint`, `valid`, `cer_blob`, `public_key_hash`, `hosting_environment_profile`, `key_vault_id`, `key_vault_secret_name`, `key_vault_secret_status`, `server_farm_id`, `canonical_name` under property `properties`
  - Model `Certificate` deleted or renamed its instance variable `domain_validation_method`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `password`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `friendly_name`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `subject_name`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `host_names`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `pfx_blob`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `site_name`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `self_link`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `issuer`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `issue_date`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `expiration_date`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `thumbprint`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `valid`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `cer_blob`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `public_key_hash`
  - Model `CertificatePatchResource` deleted or renamed its instance variable `hosting_environment_profile`
  - Model `CertificatePatchResource` moved instance variable `key_vault_id`, `key_vault_secret_name`, `key_vault_secret_status`, `server_farm_id`, `canonical_name`, `domain_validation_method` under property `properties`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `status`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `detailed_status`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `log_url`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `run_command`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `url`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `extra_info_url`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `web_job_type`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `error`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `using_sdk`
  - Model `ContinuousWebJob` deleted or renamed its instance variable `settings`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `deployment_id`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `status`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `number_of_instances_in_progress`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `number_of_instances_successful`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `number_of_instances_failed`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `failed_instances_logs`
  - Model `CsmDeploymentStatus` deleted or renamed its instance variable `errors`
  - Model `CsmPublishingCredentialsPoliciesEntity` deleted or renamed its instance variable `allow`
  - Model `CustomDnsSuffixConfiguration` deleted or renamed its instance variable `provisioning_state`
  - Model `CustomDnsSuffixConfiguration` deleted or renamed its instance variable `provisioning_details`
  - Model `CustomDnsSuffixConfiguration` deleted or renamed its instance variable `dns_suffix`
  - Model `CustomDnsSuffixConfiguration` deleted or renamed its instance variable `certificate_url`
  - Model `CustomDnsSuffixConfiguration` deleted or renamed its instance variable `key_vault_reference_identity`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `is_hostname_already_verified`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `custom_domain_verification_test`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `custom_domain_verification_failure_info`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `has_conflict_on_scale_unit`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `has_conflict_across_subscription`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `conflicting_app_resource_id`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `c_name_records`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `txt_records`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `a_records`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `alternate_c_name_records`
  - Model `CustomHostnameAnalysisResult` deleted or renamed its instance variable `alternate_txt_records`
  - Model `CustomHostnameSites` deleted or renamed its instance variable `custom_hostname`
  - Model `CustomHostnameSites` deleted or renamed its instance variable `region`
  - Model `CustomHostnameSites` deleted or renamed its instance variable `site_resource_ids`
  - Model `DatabaseConnection` moved instance variable `resource_id`, `connection_identity`, `connection_string`, `region`, `configuration_files` under property `properties`
  - Model `DatabaseConnectionPatchRequest` moved instance variable `resource_id`, `connection_identity`, `connection_string`, `region` under property `properties`
  - Model `DeletedAppRestoreRequest` moved instance variable `deleted_site_id`, `recover_configuration`, `snapshot_time`, `use_dr_secondary` under property `properties`
  - Model `DeletedSite` moved instance variable `deleted_site_id`, `deleted_timestamp`, `subscription`, `resource_group`, `deleted_site_name`, `slot`, `kind`, `geo_region_name` under property `properties`
  - Model `Deployment` moved instance variable `status`, `message`, `author`, `deployer`, `author_email`, `start_time`, `end_time`, `active`, `details` under property `properties`
  - Model `DetectorDefinitionResource` deleted or renamed its instance variable `display_name`
  - Model `DetectorDefinitionResource` deleted or renamed its instance variable `description`
  - Model `DetectorDefinitionResource` deleted or renamed its instance variable `rank`
  - Model `DetectorDefinitionResource` deleted or renamed its instance variable `is_enabled`
    - Model `DetectorDefinitionResource` moved instance variable `display_name`, `description`, `rank`, `is_enabled` under property `properties`
  - Model `DetectorResponse` deleted or renamed its instance variable `metadata`
  - Model `DetectorResponse` deleted or renamed its instance variable `dataset`
  - Model `DetectorResponse` deleted or renamed its instance variable `status`
  - Model `DetectorResponse` deleted or renamed its instance variable `data_providers_metadata`
  - Model `DetectorResponse` deleted or renamed its instance variable `suggested_utterances`
    - Model `DetectorResponse` moved instance variable `metadata`, `dataset`, `status`, `data_providers_metadata`, `suggested_utterances` under property `properties`
  - Model `DiagnosticAnalysis` deleted or renamed its instance variable `start_time`
  - Model `DiagnosticAnalysis` deleted or renamed its instance variable `end_time`
  - Model `DiagnosticAnalysis` deleted or renamed its instance variable `abnormal_time_periods`
   - Model `DiagnosticAnalysis` moved instance variable `start_time`, `end_time`, `abnormal_time_periods`, `payload`, `non_correlated_detectors` under property `properties`
   - Model `DiagnosticCategory` deleted or renamed its instance variable `description`
   - Model `DiagnosticCategory` moved instance variable `description` under property `properties`
  - Model `DiagnosticAnalysis` deleted or renamed its instance variable `payload`
  - Model `DiagnosticAnalysis` deleted or renamed its instance variable `non_correlated_detectors`
  - Model `DiagnosticCategory` deleted or renamed its instance variable `description`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `start_time`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `end_time`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `issue_detected`
   - Model `DiagnosticDetectorResponse` moved instance variable `start_time`, `end_time`, `issue_detected`, `detector_definition`, `metrics`, `abnormal_time_periods`, `data`, `response_meta_data` under property `properties`
   - Model `DiagnosticMetricSet` deleted or renamed its instance variable `values`
   - Model `DiagnosticMetricSet` moved instance variable `values` under property `properties`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `detector_definition`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `metrics`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `abnormal_time_periods`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `data`
  - Model `DiagnosticDetectorResponse` deleted or renamed its instance variable `response_meta_data`
  - Model `DiagnosticMetricSet` deleted or renamed its instance variable `values`
  - Model `FunctionAppStack` deleted or renamed its instance variable `display_text`
  - Model `FunctionAppStack` deleted or renamed its instance variable `value`
  - Model `FunctionAppStack` deleted or renamed its instance variable `major_versions`
  - Model `FunctionAppStack` deleted or renamed its instance variable `preferred_os`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `function_app_id`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `script_root_path_href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `script_href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `config_href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `test_data_href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `secrets_file_href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `href`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `config`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `files`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `test_data`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `invoke_url_template`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `language`
  - Model `FunctionEnvelope` deleted or renamed its instance variable `is_disabled`
  - Model `GeoRegion` deleted or renamed its instance variable `description`
  - Model `GeoRegion` deleted or renamed its instance variable `display_name`
  - Model `GeoRegion` deleted or renamed its instance variable `org_domain`
  - Model `HostNameBinding` deleted or renamed its instance variable `site_name`
  - Model `HostNameBinding` deleted or renamed its instance variable `domain_id`
  - Model `HostNameBinding` deleted or renamed its instance variable `azure_resource_name`
  - Model `HostNameBinding` deleted or renamed its instance variable `azure_resource_type`
  - Model `HostNameBinding` deleted or renamed its instance variable `custom_host_name_dns_record_type`
  - Model `HostNameBinding` deleted or renamed its instance variable `host_name_type`
  - Model `HostNameBinding` deleted or renamed its instance variable `ssl_state`
  - Model `HostNameBinding` deleted or renamed its instance variable `thumbprint`
  - Model `HostNameBinding` deleted or renamed its instance variable `virtual_ip`
  - Model `HybridConnection` deleted or renamed its instance variable `service_bus_namespace`
  - Model `HybridConnection` deleted or renamed its instance variable `relay_name`
  - Model `HybridConnection` deleted or renamed its instance variable `relay_arm_uri`
  - Model `HybridConnection` deleted or renamed its instance variable `hostname`
  - Model `HybridConnection` deleted or renamed its instance variable `port`
  - Model `HybridConnection` deleted or renamed its instance variable `send_key_name`
  - Model `HybridConnection` deleted or renamed its instance variable `send_key_value`
  - Model `HybridConnection` deleted or renamed its instance variable `service_bus_suffix`
  - Model `HybridConnectionKey` deleted or renamed its instance variable `send_key_name`
  - Model `HybridConnectionKey` deleted or renamed its instance variable `send_key_value`
  - Model `HybridConnectionLimits` deleted or renamed its instance variable `current`
  - Model `HybridConnectionLimits` deleted or renamed its instance variable `maximum`
  - Model `Identifier` deleted or renamed its instance variable `value`
  - Model `KubeEnvironment` deleted or renamed its instance variable `provisioning_state`
  - Model `KubeEnvironment` deleted or renamed its instance variable `deployment_errors`
  - Model `KubeEnvironment` deleted or renamed its instance variable `internal_load_balancer_enabled`
  - Model `KubeEnvironment` deleted or renamed its instance variable `default_domain`
  - Model `KubeEnvironment` deleted or renamed its instance variable `static_ip`
  - Model `KubeEnvironment` deleted or renamed its instance variable `environment_type`
  - Model `KubeEnvironment` deleted or renamed its instance variable `arc_configuration`
  - Model `KubeEnvironment` deleted or renamed its instance variable `app_logs_configuration`
  - Model `KubeEnvironment` deleted or renamed its instance variable `container_apps_configuration`
  - Model `KubeEnvironment` deleted or renamed its instance variable `aks_resource_id`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `provisioning_state`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `deployment_errors`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `internal_load_balancer_enabled`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `default_domain`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `static_ip`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `arc_configuration`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `app_logs_configuration`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `container_apps_configuration`
  - Model `KubeEnvironmentPatchResource` deleted or renamed its instance variable `aks_resource_id`
  - Model `MSDeploy` deleted or renamed its instance variable `package_uri`
  - Model `MSDeploy` deleted or renamed its instance variable `connection_string`
  - Model `MSDeploy` deleted or renamed its instance variable `db_type`
  - Model `MSDeploy` deleted or renamed its instance variable `set_parameters_xml_file_uri`
  - Model `MSDeploy` deleted or renamed its instance variable `set_parameters`
  - Model `MSDeploy` deleted or renamed its instance variable `skip_app_data`
  - Model `MSDeploy` deleted or renamed its instance variable `app_offline`
  - Model `MSDeploy` deleted or renamed its instance variable `add_on_packages`
  - Model `MSDeployLog` deleted or renamed its instance variable `entries`
  - Model `MSDeployStatus` deleted or renamed its instance variable `deployer`
  - Model `MSDeployStatus` deleted or renamed its instance variable `provisioning_state`
  - Model `MSDeployStatus` deleted or renamed its instance variable `start_time`
  - Model `MSDeployStatus` deleted or renamed its instance variable `end_time`
  - Model `MSDeployStatus` deleted or renamed its instance variable `complete`
  - Model `MigrateMySqlRequest` deleted or renamed its instance variable `connection_string`
  - Model `MigrateMySqlRequest` deleted or renamed its instance variable `migration_type`
  - Model `MigrateMySqlStatus` deleted or renamed its instance variable `migration_operation_status`
  - Model `MigrateMySqlStatus` deleted or renamed its instance variable `operation_id`
  - Model `MigrateMySqlStatus` deleted or renamed its instance variable `local_my_sql_enabled`
  - Model `NetworkFeatures` deleted or renamed its instance variable `virtual_network_name`
  - Model `NetworkFeatures` deleted or renamed its instance variable `virtual_network_connection`
  - Model `NetworkFeatures` deleted or renamed its instance variable `hybrid_connections`
  - Model `NetworkFeatures` deleted or renamed its instance variable `hybrid_connections_v2`
  - Model `PerfMonSet` deleted or renamed its instance variable `values`
  - Model `PremierAddOn` deleted or renamed its instance variable `sku`
  - Model `PremierAddOn` deleted or renamed its instance variable `product`
  - Model `PremierAddOn` deleted or renamed its instance variable `vendor`
  - Model `PremierAddOn` deleted or renamed its instance variable `marketplace_publisher`
  - Model `PremierAddOn` deleted or renamed its instance variable `marketplace_offer`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `sku`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `product`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `vendor`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `promo_code_required`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `quota`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `web_hosting_plan_restrictions`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `privacy_policy_url`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `legal_terms_url`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `marketplace_publisher`
  - Model `PremierAddOnOffer` deleted or renamed its instance variable `marketplace_offer`
  - Model `PremierAddOnPatchResource` deleted or renamed its instance variable `sku`
  - Model `PremierAddOnPatchResource` deleted or renamed its instance variable `product`
  - Model `PremierAddOnPatchResource` deleted or renamed its instance variable `vendor`
  - Model `PremierAddOnPatchResource` deleted or renamed its instance variable `marketplace_publisher`
  - Model `PremierAddOnPatchResource` deleted or renamed its instance variable `marketplace_offer`
  - Model `PrivateAccess` deleted or renamed its instance variable `enabled`
  - Model `PrivateAccess` deleted or renamed its instance variable `virtual_networks`
  - Model `ProcessInfo` deleted or renamed its instance variable `identifier`
  - Model `ProcessInfo` deleted or renamed its instance variable `deployment_name`
  - Model `ProcessInfo` deleted or renamed its instance variable `href`
  - Model `ProcessInfo` deleted or renamed its instance variable `minidump`
  - Model `ProcessInfo` deleted or renamed its instance variable `is_profile_running`
  - Model `ProcessInfo` deleted or renamed its instance variable `is_iis_profile_running`
  - Model `ProcessInfo` deleted or renamed its instance variable `iis_profile_timeout_in_seconds`
  - Model `ProcessInfo` deleted or renamed its instance variable `parent`
  - Model `ProcessInfo` deleted or renamed its instance variable `children`
  - Model `ProcessInfo` deleted or renamed its instance variable `threads`
  - Model `ProcessInfo` deleted or renamed its instance variable `open_file_handles`
  - Model `ProcessInfo` deleted or renamed its instance variable `modules`
  - Model `ProcessInfo` deleted or renamed its instance variable `file_name`
  - Model `ProcessInfo` deleted or renamed its instance variable `command_line`
  - Model `ProcessInfo` deleted or renamed its instance variable `user_name`
  - Model `ProcessInfo` deleted or renamed its instance variable `handle_count`
  - Model `ProcessInfo` deleted or renamed its instance variable `module_count`
  - Model `ProcessInfo` deleted or renamed its instance variable `thread_count`
  - Model `ProcessInfo` deleted or renamed its instance variable `start_time`
  - Model `ProcessInfo` deleted or renamed its instance variable `total_cpu_time`
  - Model `ProcessInfo` deleted or renamed its instance variable `user_cpu_time`
  - Model `ProcessInfo` deleted or renamed its instance variable `privileged_cpu_time`
  - Model `ProcessInfo` deleted or renamed its instance variable `working_set`
  - Model `ProcessInfo` deleted or renamed its instance variable `peak_working_set`
  - Model `ProcessInfo` deleted or renamed its instance variable `private_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `virtual_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `peak_virtual_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `paged_system_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `non_paged_system_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `paged_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `peak_paged_memory`
  - Model `ProcessInfo` deleted or renamed its instance variable `time_stamp`
  - Model `ProcessInfo` deleted or renamed its instance variable `environment_variables`
  - Model `ProcessInfo` deleted or renamed its instance variable `is_scm_site`
  - Model `ProcessInfo` deleted or renamed its instance variable `is_webjob`
  - Model `ProcessInfo` deleted or renamed its instance variable `description`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `base_address`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `file_name`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `href`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `file_path`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `module_memory_size`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `file_version`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `file_description`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `product`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `product_version`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `is_debug`
  - Model `ProcessModuleInfo` deleted or renamed its instance variable `language`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `identifier`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `href`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `process`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `start_address`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `current_priority`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `priority_level`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `base_priority`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `start_time`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `total_processor_time`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `user_processor_time`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `state`
  - Model `ProcessThreadInfo` deleted or renamed its instance variable `wait_reason`
  - Model `PublicCertificate` deleted or renamed its instance variable `blob`
  - Model `PublicCertificate` deleted or renamed its instance variable `public_certificate_location`
  - Model `PublicCertificate` deleted or renamed its instance variable `thumbprint`
  - Model `PushSettings` deleted or renamed its instance variable `is_push_enabled`
  - Model `PushSettings` deleted or renamed its instance variable `tag_whitelist_json`
  - Model `PushSettings` deleted or renamed its instance variable `tags_requiring_auth`
  - Model `PushSettings` deleted or renamed its instance variable `dynamic_tags_json`
  - Model `Recommendation` deleted or renamed its instance variable `creation_time`
  - Model `Recommendation` deleted or renamed its instance variable `recommendation_id`
  - Model `Recommendation` deleted or renamed its instance variable `resource_id`
  - Model `Recommendation` deleted or renamed its instance variable `resource_scope`
  - Model `Recommendation` deleted or renamed its instance variable `rule_name`
  - Model `Recommendation` deleted or renamed its instance variable `display_name`
  - Model `Recommendation` deleted or renamed its instance variable `message`
  - Model `Recommendation` deleted or renamed its instance variable `level`
  - Model `Recommendation` deleted or renamed its instance variable `channels`
  - Model `Recommendation` deleted or renamed its instance variable `category_tags`
  - Model `Recommendation` deleted or renamed its instance variable `action_name`
  - Model `Recommendation` deleted or renamed its instance variable `enabled`
  - Model `Recommendation` deleted or renamed its instance variable `states`
  - Model `Recommendation` deleted or renamed its instance variable `start_time`
  - Model `Recommendation` deleted or renamed its instance variable `end_time`
  - Model `Recommendation` deleted or renamed its instance variable `next_notification_time`
  - Model `Recommendation` deleted or renamed its instance variable `notification_expiration_time`
  - Model `Recommendation` deleted or renamed its instance variable `notified_time`
  - Model `Recommendation` deleted or renamed its instance variable `score`
  - Model `Recommendation` deleted or renamed its instance variable `is_dynamic`
  - Model `Recommendation` deleted or renamed its instance variable `extension_name`
  - Model `Recommendation` deleted or renamed its instance variable `blade_name`
  - Model `Recommendation` deleted or renamed its instance variable `forward_link`
  - Model `RecommendationRule` deleted or renamed its instance variable `recommendation_name`
  - Model `RecommendationRule` deleted or renamed its instance variable `display_name`
  - Model `RecommendationRule` deleted or renamed its instance variable `message`
  - Model `RecommendationRule` deleted or renamed its instance variable `recommendation_id`
  - Model `RecommendationRule` deleted or renamed its instance variable `description`
  - Model `RecommendationRule` deleted or renamed its instance variable `action_name`
  - Model `RecommendationRule` deleted or renamed its instance variable `level`
  - Model `RecommendationRule` deleted or renamed its instance variable `channels`
  - Model `RecommendationRule` deleted or renamed its instance variable `category_tags`
  - Model `RecommendationRule` deleted or renamed its instance variable `is_dynamic`
  - Model `RecommendationRule` deleted or renamed its instance variable `extension_name`
  - Model `RecommendationRule` deleted or renamed its instance variable `blade_name`
  - Model `RecommendationRule` deleted or renamed its instance variable `forward_link`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `entity_name`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `entity_connection_string`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `resource_type`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `resource_connection_string`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `hostname`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `port`
  - Model `RelayServiceConnectionEntity` deleted or renamed its instance variable `biztalk_uri`
  - Model `RemotePrivateEndpointConnection` deleted or renamed its instance variable `provisioning_state`
  - Model `RemotePrivateEndpointConnection` deleted or renamed its instance variable `private_endpoint`
  - Model `RemotePrivateEndpointConnection` deleted or renamed its instance variable `private_link_service_connection_state`
  - Model `RemotePrivateEndpointConnection` deleted or renamed its instance variable `ip_addresses`
  - Model `RemotePrivateEndpointConnectionARMResource` deleted or renamed its instance variable `provisioning_state`
  - Model `RemotePrivateEndpointConnectionARMResource` deleted or renamed its instance variable `private_endpoint`
  - Model `RemotePrivateEndpointConnectionARMResource` deleted or renamed its instance variable `private_link_service_connection_state`
  - Model `RemotePrivateEndpointConnectionARMResource` deleted or renamed its instance variable `ip_addresses`
  - Model `ResourceHealthMetadata` deleted or renamed its instance variable `category`
  - Model `ResourceHealthMetadata` deleted or renamed its instance variable `signal_availability`
  - Model `ResourceMetricDefinition` deleted or renamed its instance variable `unit`
  - Model `ResourceMetricDefinition` deleted or renamed its instance variable `primary_aggregation_type`
  - Model `ResourceMetricDefinition` deleted or renamed its instance variable `metric_availabilities`
  - Model `ResourceMetricDefinition` deleted or renamed its instance variable `resource_uri`
  - Model `RestoreRequest` deleted or renamed its instance variable `storage_account_url`
  - Model `RestoreRequest` deleted or renamed its instance variable `blob_name`
  - Model `RestoreRequest` deleted or renamed its instance variable `overwrite`
  - Model `RestoreRequest` deleted or renamed its instance variable `site_name`
  - Model `RestoreRequest` deleted or renamed its instance variable `databases`
  - Model `RestoreRequest` deleted or renamed its instance variable `ignore_conflicting_host_names`
  - Model `RestoreRequest` deleted or renamed its instance variable `ignore_databases`
  - Model `RestoreRequest` deleted or renamed its instance variable `app_service_plan`
  - Model `RestoreRequest` deleted or renamed its instance variable `operation_type`
  - Model `RestoreRequest` deleted or renamed its instance variable `adjust_connection_strings`
  - Model `RestoreRequest` deleted or renamed its instance variable `hosting_environment`
  - Model `Site` deleted or renamed its instance variable `state`
  - Model `Site` deleted or renamed its instance variable `host_names`
  - Model `Site` deleted or renamed its instance variable `repository_site_name`
  - Model `Site` deleted or renamed its instance variable `usage_state`
  - Model `Site` deleted or renamed its instance variable `enabled`
  - Model `Site` deleted or renamed its instance variable `enabled_host_names`
  - Model `Site` deleted or renamed its instance variable `availability_state`
  - Model `Site` deleted or renamed its instance variable `host_name_ssl_states`
  - Model `Site` deleted or renamed its instance variable `server_farm_id`
  - Model `Site` deleted or renamed its instance variable `reserved`
  - Model `Site` deleted or renamed its instance variable `is_xenon`
  - Model `Site` deleted or renamed its instance variable `hyper_v`
  - Model `Site` deleted or renamed its instance variable `last_modified_time_utc`
  - Model `Site` deleted or renamed its instance variable `dns_configuration`
  - Model `Site` deleted or renamed its instance variable `outbound_vnet_routing`
  - Model `Site` deleted or renamed its instance variable `site_config`
  - Model `Site` deleted or renamed its instance variable `function_app_config`
  - Model `Site` deleted or renamed its instance variable `dapr_config`
  - Model `Site` deleted or renamed its instance variable `workload_profile_name`
  - Model `Site` deleted or renamed its instance variable `resource_config`
  - Model `Site` deleted or renamed its instance variable `traffic_manager_host_names`
  - Model `Site` deleted or renamed its instance variable `scm_site_also_stopped`
  - Model `Site` deleted or renamed its instance variable `target_swap_slot`
  - Model `Site` deleted or renamed its instance variable `hosting_environment_profile`
  - Model `Site` deleted or renamed its instance variable `client_affinity_enabled`
  - Model `Site` deleted or renamed its instance variable `client_affinity_partitioning_enabled`
  - Model `Site` deleted or renamed its instance variable `client_affinity_proxy_enabled`
  - Model `Site` deleted or renamed its instance variable `client_cert_enabled`
  - Model `Site` deleted or renamed its instance variable `client_cert_mode`
  - Model `Site` deleted or renamed its instance variable `client_cert_exclusion_paths`
  - Model `Site` deleted or renamed its instance variable `ip_mode`
  - Model `Site` deleted or renamed its instance variable `end_to_end_encryption_enabled`
  - Model `Site` deleted or renamed its instance variable `ssh_enabled`
  - Model `Site` deleted or renamed its instance variable `host_names_disabled`
  - Model `Site` deleted or renamed its instance variable `custom_domain_verification_id`
  - Model `Site` deleted or renamed its instance variable `outbound_ip_addresses`
  - Model `Site` deleted or renamed its instance variable `possible_outbound_ip_addresses`
  - Model `Site` deleted or renamed its instance variable `container_size`
  - Model `Site` deleted or renamed its instance variable `daily_memory_time_quota`
  - Model `Site` deleted or renamed its instance variable `suspended_till`
  - Model `Site` deleted or renamed its instance variable `max_number_of_workers`
  - Model `Site` deleted or renamed its instance variable `cloning_info`
  - Model `Site` deleted or renamed its instance variable `resource_group`
  - Model `Site` deleted or renamed its instance variable `is_default_container`
  - Model `Site` deleted or renamed its instance variable `default_host_name`
  - Model `Site` deleted or renamed its instance variable `slot_swap_status`
  - Model `Site` deleted or renamed its instance variable `https_only`
  - Model `Site` deleted or renamed its instance variable `redundancy_mode`
  - Model `Site` deleted or renamed its instance variable `in_progress_operation_id`
  - Model `Site` deleted or renamed its instance variable `public_network_access`
  - Model `Site` deleted or renamed its instance variable `storage_account_required`
  - Model `Site` deleted or renamed its instance variable `key_vault_reference_identity`
  - Model `Site` deleted or renamed its instance variable `auto_generated_domain_name_label_scope`
  - Model `Site` deleted or renamed its instance variable `virtual_network_subnet_id`
  - Model `Site` deleted or renamed its instance variable `managed_environment_id`
  - Model `Site` deleted or renamed its instance variable `sku`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `enabled`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `runtime_version`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `unauthenticated_client_action`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `token_store_enabled`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `allowed_external_redirect_urls`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `default_provider`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `token_refresh_extension_hours`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `client_id`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `client_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `client_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `client_secret_certificate_thumbprint`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `issuer`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `validate_issuer`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `allowed_audiences`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `additional_login_params`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `aad_claims_authorization`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `google_client_id`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `google_client_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `google_client_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `google_o_auth_scopes`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `facebook_app_id`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `facebook_app_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `facebook_app_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `facebook_o_auth_scopes`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `git_hub_client_id`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `git_hub_client_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `git_hub_client_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `git_hub_o_auth_scopes`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `twitter_consumer_key`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `twitter_consumer_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `twitter_consumer_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `microsoft_account_client_id`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `microsoft_account_client_secret`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `microsoft_account_client_secret_setting_name`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `microsoft_account_o_auth_scopes`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `is_auth_from_file`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `auth_file_path`
  - Model `SiteAuthSettings` deleted or renamed its instance variable `config_version`
  - Model `SiteAuthSettingsV2` deleted or renamed its instance variable `platform`
  - Model `SiteAuthSettingsV2` deleted or renamed its instance variable `global_validation`
  - Model `SiteAuthSettingsV2` deleted or renamed its instance variable `identity_providers`
  - Model `SiteAuthSettingsV2` deleted or renamed its instance variable `login`
  - Model `SiteAuthSettingsV2` deleted or renamed its instance variable `http_settings`
  - Model `SiteConfigResource` deleted or renamed its instance variable `number_of_workers`
  - Model `SiteConfigResource` deleted or renamed its instance variable `default_documents`
  - Model `SiteConfigResource` deleted or renamed its instance variable `net_framework_version`
  - Model `SiteConfigResource` deleted or renamed its instance variable `php_version`
  - Model `SiteConfigResource` deleted or renamed its instance variable `python_version`
  - Model `SiteConfigResource` deleted or renamed its instance variable `node_version`
  - Model `SiteConfigResource` moved instance variable `power_shell_version`, `linux_fx_version`, `windows_fx_version`, `request_tracing_enabled`, `request_tracing_expiration_time`, `remote_debugging_enabled`, `remote_debugging_version`, `http_logging_enabled`, `acr_use_managed_identity_creds`, `acr_user_managed_identity_id`, `logs_directory_size_limit`, `detailed_error_logging_enabled`, `publishing_username`, `app_settings`, `metadata`, `connection_strings`, `machine_key`, `handler_mappings`, `document_root`, `scm_type`, `use32_bit_worker_process`, `web_sockets_enabled`, `always_on`, `java_version`, `java_container`, `java_container_version`, `app_command_line`, `managed_pipeline_mode`, `virtual_applications`, `load_balancing`, `experiments`, `limits`, `auto_heal_enabled`, `auto_heal_rules`, `tracing_options`, `vnet_name`, `vnet_route_all_enabled`, `vnet_private_ports_count`, `cors`, `push`, `api_definition`, `api_management_config`, `auto_swap_slot_name`, `local_my_sql_enabled`, `managed_service_identity_id`, `x_managed_service_identity_id`, `key_vault_reference_identity`, `ip_security_restrictions`, `ip_security_restrictions_default_action`, `scm_ip_security_restrictions`, `scm_ip_security_restrictions_default_action`, `scm_ip_security_restrictions_use_main`, `http20_enabled`, `http20_proxy_flag`, `min_tls_version`, `min_tls_cipher_suite`, `scm_min_tls_version`, `ftps_state`, `pre_warmed_instance_count`, `function_app_scale_limit`, `elastic_web_app_scale_limit`, `health_check_path`, `functions_runtime_scale_monitoring_enabled`, `website_time_zone`, `minimum_elastic_instance_count`, `azure_storage_accounts`, `public_network_access` under property `properties`
  - Model `SiteConfigurationSnapshotInfo` deleted or renamed its instance variable `time`
  - Model `SiteConfigurationSnapshotInfo` deleted or renamed its instance variable `snapshot_id`
  - Model `SiteContainer` moved instance variable `image`, `target_port`, `is_main`, `start_up_command`, `auth_type`, `user_name`, `password_secret`, `user_managed_identity_client_id`, `created_time`, `last_modified_time`, `volume_mounts`, `inherit_app_settings_and_connection_strings`, `environment_variables` under property `properties`
  - Model `SiteExtensionInfo` moved instance variable `extension_id`, `title`, `extension_type`, `summary`, `description`, `version`, `extension_url`, `project_url`, `icon_url`, `license_url`, `feed_url`, `authors`, `installer_command_line_params`, `published_date_time`, `download_count`, `local_is_latest_version`, `local_path`, `installed_date_time`, `provisioning_state`, `comment` under property `properties`
  - Model `SiteLogsConfig` moved instance variable `application_logs`, `http_logs`, `failed_requests_tracing`, `detailed_error_messages` under property `properties`
  - Model `SitePatchResource` moved instance variable `state`, `host_names`, `repository_site_name`, `usage_state`, `enabled`, `enabled_host_names`, `availability_state`, `host_name_ssl_states`, `server_farm_id`, `reserved`, `is_xenon`, `hyper_v`, `last_modified_time_utc`, `dns_configuration`, `site_config`, `traffic_manager_host_names`, `scm_site_also_stopped`, `target_swap_slot`, `hosting_environment_profile`, `client_affinity_enabled`, `client_affinity_proxy_enabled`, `client_cert_enabled`, `client_cert_mode`, `client_cert_exclusion_paths`, `host_names_disabled`, `custom_domain_verification_id`, `outbound_ip_addresses`, `possible_outbound_ip_addresses`, `container_size`, `daily_memory_time_quota`, `suspended_till`, `max_number_of_workers`, `cloning_info`, `resource_group`, `is_default_container`, `default_host_name`, `slot_swap_status`, `https_only`, `redundancy_mode`, `in_progress_operation_id`, `public_network_access`, `storage_account_required`, `key_vault_reference_identity`, `virtual_network_subnet_id` under property `properties`
  - Model `SitePhpErrorLogFlag` moved instance variable `local_log_errors`, `master_log_errors`, `local_log_errors_max_length`, `master_log_errors_max_length` under property `properties`
  - Model `SiteSourceControl` moved instance variable `repo_url`, `branch`, `is_manual_integration`, `is_git_hub_action`, `deployment_rollback_enabled`, `is_mercurial`, `git_hub_action_configuration` under property `properties`
  - Model `SlotConfigNamesResource` moved instance variable `connection_string_names`, `app_setting_names`, `azure_storage_config_names` under property `properties`
  - Model `SlotDifference` moved instance variable `level`, `setting_type`, `diff_rule`, `setting_name`, `value_in_current_slot`, `value_in_target_slot`, `description` under property `properties`
  - Model `Snapshot` deleted or renamed its instance variable `time`
  - Model `SnapshotRestoreRequest` moved instance variable `snapshot_time`, `recovery_source`, `overwrite`, `recover_configuration`, `ignore_conflicting_host_names`, `use_dr_secondary` under property `properties`
  - Model `SourceControl` moved instance variable `token`, `token_secret`, `refresh_token`, `expiration_time` under property `properties`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `default_hostname`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `repository_url`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `branch`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `custom_domains`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `repository_token`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `build_properties`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `private_endpoint_connections`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `staging_environment_policy`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `allow_config_file_updates`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `template_properties`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `content_distribution_endpoint`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `key_vault_reference_identity`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `user_provided_function_apps`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `linked_backends`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `provider`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `enterprise_grade_cdn_status`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `public_network_access`
  - Model `StaticSiteARMResource` deleted or renamed its instance variable `database_connections`
  - Model `StaticSiteBasicAuthPropertiesARMResource` deleted or renamed its instance variable `password`
  - Model `StaticSiteBasicAuthPropertiesARMResource` deleted or renamed its instance variable `secret_url`
  - Model `StaticSiteBasicAuthPropertiesARMResource` deleted or renamed its instance variable `applicable_environments_mode`
  - Model `StaticSiteBasicAuthPropertiesARMResource` deleted or renamed its instance variable `environments`
  - Model `StaticSiteBasicAuthPropertiesARMResource` deleted or renamed its instance variable `secret_state`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `build_id`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `source_branch`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `pull_request_title`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `hostname`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `created_time_utc`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `last_updated_on`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `status`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `user_provided_function_apps`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `linked_backends`
  - Model `StaticSiteBuildARMResource` deleted or renamed its instance variable `database_connections`
  - Model `StaticSiteCustomDomainOverviewARMResource` deleted or renamed its instance variable `domain_name`
  - Model `StaticSiteCustomDomainOverviewARMResource` deleted or renamed its instance variable `created_on`
  - Model `StaticSiteCustomDomainOverviewARMResource` deleted or renamed its instance variable `status`
  - Model `StaticSiteCustomDomainOverviewARMResource` deleted or renamed its instance variable `validation_token`
  - Model `StaticSiteCustomDomainOverviewARMResource` deleted or renamed its instance variable `error_message`
  - Model `StaticSiteCustomDomainRequestPropertiesARMResource` deleted or renamed its instance variable `validation_method`
  - Model `StaticSiteFunctionOverviewARMResource` deleted or renamed its instance variable `function_name`
  - Model `StaticSiteFunctionOverviewARMResource` deleted or renamed its instance variable `trigger_type`
  - Model `StaticSiteLinkedBackendARMResource` deleted or renamed its instance variable `backend_resource_id`
  - Model `StaticSiteLinkedBackendARMResource` deleted or renamed its instance variable `region`
  - Model `StaticSiteLinkedBackendARMResource` deleted or renamed its instance variable `created_on`
  - Model `StaticSiteLinkedBackendARMResource` deleted or renamed its instance variable `provisioning_state`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `default_hostname`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `repository_url`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `branch`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `custom_domains`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `repository_token`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `build_properties`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `private_endpoint_connections`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `staging_environment_policy`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `allow_config_file_updates`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `template_properties`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `content_distribution_endpoint`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `key_vault_reference_identity`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `user_provided_function_apps`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `linked_backends`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `provider`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `enterprise_grade_cdn_status`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `public_network_access`
  - Model `StaticSitePatchResource` deleted or renamed its instance variable `database_connections`
  - Model `StaticSiteResetPropertiesARMResource` deleted or renamed its instance variable `repository_token`
  - Model `StaticSiteResetPropertiesARMResource` deleted or renamed its instance variable `should_update_repository`
  - Model `StaticSiteUserARMResource` deleted or renamed its instance variable `provider`
  - Model `StaticSiteUserARMResource` deleted or renamed its instance variable `user_id`
  - Model `StaticSiteUserARMResource` deleted or renamed its instance variable `display_name`
  - Model `StaticSiteUserARMResource` deleted or renamed its instance variable `roles`
  - Model `StaticSiteUserInvitationRequestResource` deleted or renamed its instance variable `domain`
  - Model `StaticSiteUserInvitationRequestResource` deleted or renamed its instance variable `provider`
  - Model `StaticSiteUserInvitationRequestResource` deleted or renamed its instance variable `user_details`
  - Model `StaticSiteUserInvitationRequestResource` deleted or renamed its instance variable `roles`
  - Model `StaticSiteUserInvitationRequestResource` deleted or renamed its instance variable `num_hours_to_expiration`
  - Model `StaticSiteUserInvitationResponseResource` deleted or renamed its instance variable `expires_on`
  - Model `StaticSiteUserInvitationResponseResource` deleted or renamed its instance variable `invitation_url`
  - Model `StaticSiteUserProvidedFunctionApp` deleted or renamed its instance variable `function_app_resource_id`
  - Model `StaticSiteUserProvidedFunctionApp` deleted or renamed its instance variable `function_app_region`
  - Model `StaticSiteUserProvidedFunctionApp` deleted or renamed its instance variable `created_on`
  - Model `StaticSiteUserProvidedFunctionAppARMResource` deleted or renamed its instance variable `function_app_resource_id`
  - Model `StaticSiteUserProvidedFunctionAppARMResource` deleted or renamed its instance variable `function_app_region`
  - Model `StaticSiteUserProvidedFunctionAppARMResource` deleted or renamed its instance variable `created_on`
  - Model `StaticSiteZipDeploymentARMResource` deleted or renamed its instance variable `app_zip_url`
  - Model `StaticSiteZipDeploymentARMResource` deleted or renamed its instance variable `api_zip_url`
  - Model `StaticSiteZipDeploymentARMResource` deleted or renamed its instance variable `deployment_title`
  - Model `StaticSiteZipDeploymentARMResource` deleted or renamed its instance variable `provider`
  - Model `StaticSiteZipDeploymentARMResource` deleted or renamed its instance variable `function_language`
  - Model `StaticSitesWorkflowPreview` deleted or renamed its instance variable `path`
  - Model `StaticSitesWorkflowPreview` deleted or renamed its instance variable `contents`
  - Model `StaticSitesWorkflowPreviewRequest` deleted or renamed its instance variable `repository_url`
  - Model `StaticSitesWorkflowPreviewRequest` deleted or renamed its instance variable `branch`
  - Model `StaticSitesWorkflowPreviewRequest` deleted or renamed its instance variable `build_properties`
  - Model `StorageMigrationOptions` deleted or renamed its instance variable `azurefiles_connection_string`
  - Model `StorageMigrationOptions` deleted or renamed its instance variable `azurefiles_share`
  - Model `StorageMigrationOptions` deleted or renamed its instance variable `switch_site_after_migration`
  - Model `StorageMigrationOptions` deleted or renamed its instance variable `block_write_access_to_site`
  - Model `StorageMigrationResponse` deleted or renamed its instance variable `operation_id`
  - Model `SwiftVirtualNetwork` deleted or renamed its instance variable `subnet_resource_id`
  - Model `SwiftVirtualNetwork` deleted or renamed its instance variable `swift_supported`
  - Model `TriggeredJobHistory` deleted or renamed its instance variable `runs`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `latest_run`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `history_url`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `scheduler_logs_url`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `run_command`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `url`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `extra_info_url`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `web_job_type`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `error`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `using_sdk`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `public_network_access`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `storage_account_required`
  - Model `TriggeredWebJob` deleted or renamed its instance variable `settings`
  - Model `Usage` deleted or renamed its instance variable `display_name`
  - Model `Usage` deleted or renamed its instance variable `resource_name`
  - Model `Usage` deleted or renamed its instance variable `unit`
  - Model `Usage` deleted or renamed its instance variable `current_value`
  - Model `Usage` deleted or renamed its instance variable `limit`
  - Model `Usage` deleted or renamed its instance variable `next_reset_time`
  - Model `Usage` deleted or renamed its instance variable `compute_mode`
  - Model `Usage` deleted or renamed its instance variable `site_mode`
  - Model `User` deleted or renamed its instance variable `publishing_user_name`
  - Model `User` deleted or renamed its instance variable `publishing_password`
  - Model `User` deleted or renamed its instance variable `publishing_password_hash`
  - Model `User` deleted or renamed its instance variable `publishing_password_hash_salt`
  - Model `User` deleted or renamed its instance variable `scm_uri`
  - Model `ValidateRequest` deleted or renamed its instance variable `server_farm_id`
  - Model `ValidateRequest` deleted or renamed its instance variable `sku_name`
  - Model `ValidateRequest` deleted or renamed its instance variable `need_linux_workers`
  - Model `ValidateRequest` deleted or renamed its instance variable `is_spot`
  - Model `ValidateRequest` deleted or renamed its instance variable `capacity`
  - Model `ValidateRequest` deleted or renamed its instance variable `hosting_environment`
  - Model `ValidateRequest` deleted or renamed its instance variable `is_xenon`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_registry_base_url`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_registry_username`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_registry_password`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_image_repository`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_image_tag`
  - Model `ValidateRequest` deleted or renamed its instance variable `container_image_platform`
  - Model `ValidateRequest` deleted or renamed its instance variable `app_service_environment`
  - Model `VnetGateway` deleted or renamed its instance variable `vnet_name`
  - Model `VnetGateway` deleted or renamed its instance variable `vpn_package_uri`
  - Model `VnetInfoResource` deleted or renamed its instance variable `vnet_resource_id`
  - Model `VnetInfoResource` deleted or renamed its instance variable `cert_thumbprint`
  - Model `VnetInfoResource` deleted or renamed its instance variable `cert_blob`
  - Model `VnetInfoResource` deleted or renamed its instance variable `routes`
  - Model `VnetInfoResource` deleted or renamed its instance variable `resync_required`
  - Model `VnetInfoResource` deleted or renamed its instance variable `dns_servers`
  - Model `VnetInfoResource` deleted or renamed its instance variable `is_swift`
  - Model `VnetParameters` deleted or renamed its instance variable `vnet_resource_group`
  - Model `VnetParameters` deleted or renamed its instance variable `vnet_name`
  - Model `VnetParameters` deleted or renamed its instance variable `vnet_subnet_name`
  - Model `VnetParameters` deleted or renamed its instance variable `subnet_resource_id`
  - Model `VnetRoute` deleted or renamed its instance variable `start_address`
  - Model `VnetRoute` deleted or renamed its instance variable `end_address`
  - Model `VnetRoute` deleted or renamed its instance variable `route_type`
  - Model `VnetValidationFailureDetails` deleted or renamed its instance variable `message`
  - Model `VnetValidationFailureDetails` deleted or renamed its instance variable `failed`
  - Model `VnetValidationFailureDetails` deleted or renamed its instance variable `failed_tests`
  - Model `VnetValidationFailureDetails` deleted or renamed its instance variable `warnings`
  - Model `VnetValidationTestFailure` deleted or renamed its instance variable `test_name`
  - Model `VnetValidationTestFailure` deleted or renamed its instance variable `details`
  - Model `WebAppStack` deleted or renamed its instance variable `display_text`
  - Model `WebAppStack` deleted or renamed its instance variable `value`
  - Model `WebAppStack` deleted or renamed its instance variable `major_versions`
  - Model `WebAppStack` deleted or renamed its instance variable `preferred_os`
  - Model `WebJob` deleted or renamed its instance variable `run_command`
  - Model `WebJob` deleted or renamed its instance variable `url`
  - Model `WebJob` deleted or renamed its instance variable `extra_info_url`
  - Model `WebJob` deleted or renamed its instance variable `web_job_type`
  - Model `WebJob` deleted or renamed its instance variable `error`
  - Model `WebJob` deleted or renamed its instance variable `using_sdk`
  - Model `WebJob` deleted or renamed its instance variable `settings`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `state`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `status_url`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `detector_url`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `console_url`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `health_check_url`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `containers`
  - Model `WebSiteInstanceStatus` deleted or renamed its instance variable `physical_zone`
  - Model `WorkerPoolResource` deleted or renamed its instance variable `worker_size_id`
  - Model `WorkerPoolResource` deleted or renamed its instance variable `compute_mode`
  - Model `WorkerPoolResource` deleted or renamed its instance variable `worker_size`
  - Model `WorkerPoolResource` deleted or renamed its instance variable `worker_count`
  - Model `WorkerPoolResource` deleted or renamed its instance variable `instance_names`
  - Model `Workflow` deleted or renamed its instance variable `provisioning_state`
  - Model `Workflow` deleted or renamed its instance variable `created_time`
  - Model `Workflow` deleted or renamed its instance variable `changed_time`
  - Model `Workflow` deleted or renamed its instance variable `state`
  - Model `Workflow` deleted or renamed its instance variable `version`
  - Model `Workflow` deleted or renamed its instance variable `access_endpoint`
  - Model `Workflow` deleted or renamed its instance variable `endpoints_configuration`
  - Model `Workflow` deleted or renamed its instance variable `access_control`
  - Model `Workflow` deleted or renamed its instance variable `sku`
  - Model `Workflow` deleted or renamed its instance variable `integration_account`
  - Model `Workflow` deleted or renamed its instance variable `integration_service_environment`
  - Model `Workflow` deleted or renamed its instance variable `definition`
  - Model `Workflow` deleted or renamed its instance variable `parameters`
  - Model `Workflow` deleted or renamed its instance variable `kind`
  - Model `WorkflowRun` deleted or renamed its instance variable `wait_end_time`
  - Model `WorkflowRun` deleted or renamed its instance variable `start_time`
  - Model `WorkflowRun` deleted or renamed its instance variable `end_time`
  - Model `WorkflowRun` deleted or renamed its instance variable `status`
  - Model `WorkflowRun` deleted or renamed its instance variable `code`
  - Model `WorkflowRun` deleted or renamed its instance variable `error`
  - Model `WorkflowRun` deleted or renamed its instance variable `correlation_id`
  - Model `WorkflowRun` deleted or renamed its instance variable `correlation`
  - Model `WorkflowRun` deleted or renamed its instance variable `workflow`
  - Model `WorkflowRun` deleted or renamed its instance variable `trigger`
  - Model `WorkflowRun` deleted or renamed its instance variable `outputs`
  - Model `WorkflowRun` deleted or renamed its instance variable `response`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `start_time`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `end_time`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `status`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `code`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `error`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `tracking_id`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `correlation`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `inputs_link`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `outputs_link`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `tracked_properties`
  - Model `WorkflowRunAction` deleted or renamed its instance variable `retry_history`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `start_time`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `end_time`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `correlation`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `status`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `code`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `error`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `tracking_id`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `inputs`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `inputs_link`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `outputs`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `outputs_link`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `tracked_properties`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `retry_history`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `iteration_count`
  - Model `WorkflowRunActionRepetitionDefinition` deleted or renamed its instance variable `repetition_indexes`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `provisioning_state`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `created_time`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `changed_time`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `state`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `status`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `last_execution_time`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `next_execution_time`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `recurrence`
  - Model `WorkflowTrigger` deleted or renamed its instance variable `workflow`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `start_time`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `end_time`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `scheduled_time`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `status`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `code`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `error`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `tracking_id`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `correlation`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `inputs_link`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `outputs_link`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `fired`
  - Model `WorkflowTriggerHistory` deleted or renamed its instance variable `run`
  - Model `WorkflowVersion` deleted or renamed its instance variable `provisioning_state`
  - Model `WorkflowVersion` deleted or renamed its instance variable `created_time`
  - Model `WorkflowVersion` deleted or renamed its instance variable `changed_time`
  - Model `WorkflowVersion` deleted or renamed its instance variable `state`
  - Model `WorkflowVersion` deleted or renamed its instance variable `version`
  - Model `WorkflowVersion` deleted or renamed its instance variable `access_endpoint`
  - Model `WorkflowVersion` deleted or renamed its instance variable `endpoints_configuration`
  - Model `WorkflowVersion` deleted or renamed its instance variable `access_control`
  - Model `WorkflowVersion` deleted or renamed its instance variable `sku`
  - Model `WorkflowVersion` deleted or renamed its instance variable `integration_account`
  - Model `WorkflowVersion` deleted or renamed its instance variable `definition`
  - Model `WorkflowVersion` deleted or renamed its instance variable `parameters`
  - Deleted or renamed model `ApiKVReferenceCollection`
  - Deleted or renamed model `AppServiceEnvironmentCollection`
  - Deleted or renamed model `AppServicePlanCollection`
  - Deleted or renamed model `ApplicationStackCollection`
  - Deleted or renamed model `AseRegionCollection`
  - Deleted or renamed model `BackupItemCollection`
  - Deleted or renamed model `BillingMeterCollection`
  - Deleted or renamed model `CertificateCollection`
  - Deleted or renamed model `ContinuousWebJobCollection`
  - Deleted or renamed model `CsmDeploymentStatusCollection`
  - Deleted or renamed model `CsmOperationCollection`
  - Deleted or renamed model `CsmUsageQuotaCollection`
  - Deleted or renamed model `CustomHostnameSitesCollection`
  - Deleted or renamed model `DatabaseConnectionCollection`
  - Deleted or renamed model `DeletedWebAppCollection`
  - Deleted or renamed model `DeploymentCollection`
  - Deleted or renamed model `DetectorResponseCollection`
  - Deleted or renamed model `DiagnosticAnalysisCollection`
  - Deleted or renamed model `DiagnosticCategoryCollection`
  - Deleted or renamed model `DiagnosticDetectorCollection`
  - Deleted or renamed model `ExpressionTraces`
  - Deleted or renamed model `FunctionAppStackCollection`
  - Deleted or renamed model `FunctionEnvelopeCollection`
  - Deleted or renamed model `GeoRegionCollection`
  - Deleted or renamed model `HostNameBindingCollection`
  - Deleted or renamed model `HybridConnectionCollection`
  - Deleted or renamed model `IdentifierCollection`
  - Deleted or renamed model `InboundEnvironmentEndpointCollection`
  - Deleted or renamed model `KubeEnvironmentCollection`
  - Deleted or renamed model `OutboundEnvironmentEndpointCollection`
  - Deleted or renamed model `PerfMonCounterCollection`
  - Deleted or renamed model `PremierAddOnOfferCollection`
  - Deleted or renamed model `PrivateEndpointConnectionCollection`
  - Deleted or renamed model `PrivateLinkConnectionApprovalRequestResource`
  - Deleted or renamed model `ProcessInfoCollection`
  - Deleted or renamed model `ProcessModuleInfoCollection`
  - Deleted or renamed model `ProcessThreadInfoCollection`
  - Deleted or renamed model `PublicCertificateCollection`
  - Deleted or renamed model `PublishingCredentialsPoliciesCollection`
  - Deleted or renamed model `RecommendationCollection`
  - Deleted or renamed model `ResourceCollection`
  - Deleted or renamed model `ResourceHealthMetadataCollection`
  - Deleted or renamed model `ResourceMetricDefinitionCollection`
  - Deleted or renamed model `SiteConfigResourceCollection`
  - Deleted or renamed model `SiteConfigurationSnapshotInfoCollection`
  - Deleted or renamed model `SiteContainerCollection`
  - Deleted or renamed model `SiteExtensionInfoCollection`
  - Deleted or renamed model `SkuInfoCollection`
  - Deleted or renamed model `SlotDifferenceCollection`
  - Deleted or renamed model `SnapshotCollection`
  - Deleted or renamed model `SourceControlCollection`
  - Deleted or renamed model `StampCapacityCollection`
  - Deleted or renamed model `StaticSiteBasicAuthPropertiesCollection`
  - Deleted or renamed model `StaticSiteBuildCollection`
  - Deleted or renamed model `StaticSiteCollection`
  - Deleted or renamed model `StaticSiteCustomDomainOverviewCollection`
  - Deleted or renamed model `StaticSiteFunctionOverviewCollection`
  - Deleted or renamed model `StaticSiteLinkedBackendsCollection`
  - Deleted or renamed model `StaticSiteUserCollection`
  - Deleted or renamed model `StaticSiteUserProvidedFunctionAppsCollection`
  - Deleted or renamed model `TriggeredJobHistoryCollection`
  - Deleted or renamed model `TriggeredWebJobCollection`
  - Deleted or renamed model `UsageCollection`
  - Deleted or renamed model `WebAppCollection`
  - Deleted or renamed model `WebAppInstanceStatusCollection`
  - Deleted or renamed model `WebAppStackCollection`
  - Deleted or renamed model `WebJobCollection`
  - Deleted or renamed model `WorkerPoolCollection`
  - Deleted or renamed model `WorkflowEnvelopeCollection`
  - Deleted or renamed model `WorkflowRunActionRepetitionDefinitionCollection`
  - Method `AppServiceEnvironmentsOperations.begin_delete` changed its parameter `force_delete` from `positional_or_keyword` to `keyword_only`
  - Method `AppServiceEnvironmentsOperations.list_web_apps` changed its parameter `properties_to_include` from `positional_or_keyword` to `keyword_only`
  - Method `AppServicePlansOperations.list` changed its parameter `detailed` from `positional_or_keyword` to `keyword_only`
  - Method `AppServicePlansOperations.list_web_apps` changed its parameter `skip_token` from `positional_or_keyword` to `keyword_only`
  - Method `AppServicePlansOperations.restart_web_apps` changed its parameter `soft_restart` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis_slot` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis_slot` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_analysis_slot` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector_slot` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector_slot` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.execute_site_detector_slot` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_hosting_environment_detector_response` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `DiagnosticsOperations.get_site_detector_response_slot` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_available_stacks` changed its parameter `os_type_selected` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_available_stacks_on_prem` changed its parameter `os_type_selected` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_function_app_stacks` changed its parameter `stack_os_type` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_function_app_stacks_for_location` changed its parameter `stack_os_type` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_web_app_stacks` changed its parameter `stack_os_type` from `positional_or_keyword` to `keyword_only`
  - Method `ProviderOperations.get_web_app_stacks_for_location` changed its parameter `stack_os_type` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.disable_all_for_hosting_environment` changed its parameter `environment_name` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.disable_recommendation_for_hosting_environment` changed its parameter `environment_name` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.get_rule_details_by_hosting_environment` changed its parameter `update_seen` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.get_rule_details_by_hosting_environment` changed its parameter `recommendation_id` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.get_rule_details_by_web_app` changed its parameter `update_seen` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.get_rule_details_by_web_app` changed its parameter `recommendation_id` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.list` changed its parameter `featured` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.list_history_for_hosting_environment` changed its parameter `expired_only` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.list_history_for_web_app` changed its parameter `expired_only` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.list_recommended_rules_for_hosting_environment` changed its parameter `featured` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.list_recommended_rules_for_web_app` changed its parameter `featured` from `positional_or_keyword` to `keyword_only`
  - Method `RecommendationsOperations.reset_all_filters_for_hosting_environment` changed its parameter `environment_name` from `positional_or_keyword` to `keyword_only`
  - Method `StaticSitesOperations.begin_register_user_provided_function_app_with_static_site` changed its parameter `is_forced` from `positional_or_keyword` to `keyword_only`
  - Method `StaticSitesOperations.begin_register_user_provided_function_app_with_static_site_build` changed its parameter `is_forced` from `positional_or_keyword` to `keyword_only`
  - Method `StaticSitesOperations.unlink_backend` changed its parameter `is_cleaning_auth_config` from `positional_or_keyword` to `keyword_only`
  - Method `StaticSitesOperations.unlink_backend_from_build` changed its parameter `is_cleaning_auth_config` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.analyze_custom_hostname` changed its parameter `host_name` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.analyze_custom_hostname_slot` changed its parameter `host_name` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_migrate_storage` changed its parameter `subscription_name` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace_slot` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace_slot` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_network_trace_slot` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation_slot` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation_slot` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.begin_start_web_site_network_trace_operation_slot` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete` changed its parameter `delete_metrics` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete` changed its parameter `delete_empty_server_farm` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete_slot` changed its parameter `delete_metrics` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete_slot` changed its parameter `delete_empty_server_farm` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete_source_control` changed its parameter `additional_flags` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.delete_source_control_slot` changed its parameter `additional_flags` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.list_by_resource_group` changed its parameter `include_slots` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.restart` changed its parameter `soft_restart` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.restart` changed its parameter `synchronous` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.restart_slot` changed its parameter `soft_restart` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.restart_slot` changed its parameter `synchronous` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace_slot` changed its parameter `duration_in_seconds` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace_slot` changed its parameter `max_frame_length` from `positional_or_keyword` to `keyword_only`
  - Method `WebAppsOperations.start_web_site_network_trace_slot` changed its parameter `sas_url` from `positional_or_keyword` to `keyword_only`

## 10.2.0 (2025-12-17)

change log generation was timeout!!! You need to write it manually!!!

## 10.1.0 (2025-11-17)

### Features Added

  - Added operation AppServicePlansOperations.get_server_farm_instance_details
  - Added operation AppServicePlansOperations.get_server_farm_rdp_password
  - Added operation AppServicePlansOperations.recycle_managed_instance_worker
  - Model AppServicePlan has a new parameter identity
  - Model AppServicePlan has a new parameter install_scripts
  - Model AppServicePlan has a new parameter is_custom_mode
  - Model AppServicePlan has a new parameter network
  - Model AppServicePlan has a new parameter plan_default_identity
  - Model AppServicePlan has a new parameter rdp_enabled
  - Model AppServicePlan has a new parameter registry_adapters
  - Model AppServicePlan has a new parameter storage_mounts
  - Model AppServicePlanPatchResource has a new parameter identity
  - Model SitePatchResource has a new parameter public_network_access

## 10.0.0 (2025-08-21)

### Breaking Changes

  - This package now only targets the latest Api-Version available on Azure and removes APIs of other Api-Version. After this change, the package can have much smaller size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.

## 9.0.0 (2025-06-16)

### Features Added

  - Added operation WebSiteManagementClientOperationsMixin.regional_check_name_availability
  - Added operation group SiteCertificatesOperations
  - Model AppServicePlan has a new parameter async_scaling_enabled
  - Model Site has a new parameter client_affinity_partitioning_enabled
  - Model Site has a new parameter client_affinity_proxy_enabled
  - Model Site has a new parameter outbound_vnet_routing
  - Model Site has a new parameter ssh_enabled
  - Model SiteConfig has a new parameter http20_proxy_flag
  - Model SiteConfigResource has a new parameter http20_proxy_flag
  - Model SiteContainer has a new parameter inherit_app_settings_and_connection_strings
  - Model SitePatchResource has a new parameter client_affinity_proxy_enabled

### Breaking Changes

  - Model Site no longer has parameter vnet_backup_restore_enabled
  - Model Site no longer has parameter vnet_content_share_enabled
  - Model Site no longer has parameter vnet_image_pull_enabled
  - Model Site no longer has parameter vnet_route_all_enabled

## 8.0.0 (2025-01-23)

### Breaking Changes
  
  - Removed subfolders of some unused Api-Versions for smaller package size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.

## 7.3.1 (2024-08-19)

### Bugs Fixed

  - Fix type of property instance_count in model FunctionsAlwaysReadyConfig from float to int
  - Fix type of property maximum_instance_count in model FunctionsScaleAndConcurrency from float to int
  - Fix type of property instance_memory_mb in model FunctionsScaleAndConcurrency from float to int
  - Fix type of property per_instance_concurrency in model FunctionsScaleAndConcurrencyTriggersHttp from float to int

## 7.3.0 (2024-06-17)

### Features Added

  - Added operation WebAppsOperations.create_or_update_site_container
  - Added operation WebAppsOperations.create_or_update_site_container_slot
  - Added operation WebAppsOperations.delete_site_container
  - Added operation WebAppsOperations.delete_site_container_slot
  - Added operation WebAppsOperations.get_site_container
  - Added operation WebAppsOperations.get_site_container_slot
  - Added operation WebAppsOperations.list_site_containers
  - Added operation WebAppsOperations.list_site_containers_slot
  - Model AzureStorageInfoValue has a new parameter protocol
  - Model Site has a new parameter dns_configuration
  - Model Site has a new parameter function_app_config
  - Model Site has a new parameter vnet_backup_restore_enabled
  - Model SitePatchResource has a new parameter dns_configuration

## 7.2.0 (2023-11-20)

### Features Added

  - Added operation WebSiteManagementClientOperationsMixin.list_ase_regions
  - Added operation group GetUsagesInLocationOperations
  - Model ResourceNameAvailabilityRequest has a new parameter environment_id
  - Model Site has a new parameter dapr_config
  - Model Site has a new parameter resource_config
  - Model Site has a new parameter workload_profile_name
  - Model SiteConfig has a new parameter min_tls_cipher_suite
  - Model SiteConfigResource has a new parameter min_tls_cipher_suite
  - Operation WebSiteManagementClientOperationsMixin.check_name_availability has a new optional parameter environment_id

## 7.1.0 (2023-04-20)

### Features Added

  - Added operation StaticSitesOperations.create_or_update_basic_auth
  - Added operation StaticSitesOperations.create_or_update_build_database_connection
  - Added operation StaticSitesOperations.create_or_update_database_connection
  - Added operation StaticSitesOperations.delete_build_database_connection
  - Added operation StaticSitesOperations.delete_database_connection
  - Added operation StaticSitesOperations.get_basic_auth
  - Added operation StaticSitesOperations.get_build_database_connection
  - Added operation StaticSitesOperations.get_build_database_connection_with_details
  - Added operation StaticSitesOperations.get_build_database_connections
  - Added operation StaticSitesOperations.get_build_database_connections_with_details
  - Added operation StaticSitesOperations.get_database_connection
  - Added operation StaticSitesOperations.get_database_connection_with_details
  - Added operation StaticSitesOperations.get_database_connections
  - Added operation StaticSitesOperations.get_database_connections_with_details
  - Added operation StaticSitesOperations.list_basic_auth
  - Added operation StaticSitesOperations.update_build_database_connection
  - Added operation StaticSitesOperations.update_database_connection
  - Added operation WebAppsOperations.deploy_workflow_artifacts
  - Added operation WebAppsOperations.deploy_workflow_artifacts_slot
  - Added operation WebAppsOperations.get_instance_workflow_slot
  - Added operation WebAppsOperations.get_workflow
  - Added operation WebAppsOperations.list_instance_workflows_slot
  - Added operation WebAppsOperations.list_workflows
  - Added operation WebAppsOperations.list_workflows_connections
  - Added operation WebAppsOperations.list_workflows_connections_slot
  - Model Site has a new parameter managed_environment_id
  - Model SiteConfig has a new parameter elastic_web_app_scale_limit
  - Model SiteConfig has a new parameter ip_security_restrictions_default_action
  - Model SiteConfig has a new parameter metadata
  - Model SiteConfig has a new parameter scm_ip_security_restrictions_default_action
  - Model SiteConfigResource has a new parameter elastic_web_app_scale_limit
  - Model SiteConfigResource has a new parameter ip_security_restrictions_default_action
  - Model SiteConfigResource has a new parameter metadata
  - Model SiteConfigResource has a new parameter scm_ip_security_restrictions_default_action
  - Model StaticSiteARMResource has a new parameter database_connections
  - Model StaticSiteBuildARMResource has a new parameter database_connections
  - Model StaticSitePatchResource has a new parameter database_connections

## 7.0.0 (2022-07-04)

**Features**

  - Added operation AppServiceEnvironmentsOperations.begin_upgrade
  - Added operation AppServiceEnvironmentsOperations.delete_ase_custom_dns_suffix_configuration
  - Added operation AppServiceEnvironmentsOperations.get_ase_custom_dns_suffix_configuration
  - Added operation AppServiceEnvironmentsOperations.test_upgrade_available_notification
  - Added operation AppServiceEnvironmentsOperations.update_ase_custom_dns_suffix_configuration
  - Added operation StaticSitesOperations.begin_link_backend
  - Added operation StaticSitesOperations.begin_link_backend_to_build
  - Added operation StaticSitesOperations.begin_validate_backend
  - Added operation StaticSitesOperations.begin_validate_backend_for_build
  - Added operation StaticSitesOperations.get_linked_backend
  - Added operation StaticSitesOperations.get_linked_backend_for_build
  - Added operation StaticSitesOperations.get_linked_backends
  - Added operation StaticSitesOperations.get_linked_backends_for_build
  - Added operation StaticSitesOperations.unlink_backend
  - Added operation StaticSitesOperations.unlink_backend_from_build
  - Added operation WebAppsOperations.begin_get_production_site_deployment_status
  - Added operation WebAppsOperations.begin_get_slot_site_deployment_status_slot
  - Added operation WebAppsOperations.get_auth_settings_v2_without_secrets_slot
  - Added operation WebAppsOperations.list_production_site_deployment_statuses
  - Added operation WebAppsOperations.list_slot_site_deployment_statuses_slot
  - Added operation group WorkflowRunActionRepetitionsOperations
  - Added operation group WorkflowRunActionRepetitionsRequestHistoriesOperations
  - Added operation group WorkflowRunActionScopeRepetitionsOperations
  - Added operation group WorkflowRunActionsOperations
  - Added operation group WorkflowRunsOperations
  - Added operation group WorkflowTriggerHistoriesOperations
  - Added operation group WorkflowTriggersOperations
  - Added operation group WorkflowVersionsOperations
  - Added operation group WorkflowsOperations
  - Model AppServiceEnvironment has a new parameter custom_dns_suffix_configuration
  - Model AppServiceEnvironment has a new parameter networking_configuration
  - Model AppServiceEnvironment has a new parameter upgrade_availability
  - Model AppServiceEnvironment has a new parameter upgrade_preference
  - Model AppServiceEnvironmentPatchResource has a new parameter custom_dns_suffix_configuration
  - Model AppServiceEnvironmentPatchResource has a new parameter networking_configuration
  - Model AppServiceEnvironmentPatchResource has a new parameter upgrade_availability
  - Model AppServiceEnvironmentPatchResource has a new parameter upgrade_preference
  - Model AppServiceEnvironmentResource has a new parameter custom_dns_suffix_configuration
  - Model AppServiceEnvironmentResource has a new parameter networking_configuration
  - Model AppServiceEnvironmentResource has a new parameter upgrade_availability
  - Model AppServiceEnvironmentResource has a new parameter upgrade_preference
  - Model AppServicePlan has a new parameter number_of_workers
  - Model AppServicePlanPatchResource has a new parameter number_of_workers
  - Model AseV3NetworkingConfiguration has a new parameter ftp_enabled
  - Model AseV3NetworkingConfiguration has a new parameter inbound_ip_address_override
  - Model AseV3NetworkingConfiguration has a new parameter remote_debug_enabled
  - Model ErrorResponse has a new parameter error
  - Model Site has a new parameter public_network_access
  - Model Site has a new parameter vnet_content_share_enabled
  - Model Site has a new parameter vnet_image_pull_enabled
  - Model Site has a new parameter vnet_route_all_enabled
  - Model StaticSiteARMResource has a new parameter linked_backends
  - Model StaticSiteARMResource has a new parameter public_network_access
  - Model StaticSiteBuildARMResource has a new parameter linked_backends
  - Model StaticSitePatchResource has a new parameter linked_backends
  - Model StaticSitePatchResource has a new parameter public_network_access
  - Model TriggeredWebJob has a new parameter public_network_access
  - Model TriggeredWebJob has a new parameter storage_account_required

**Breaking changes**

  - Model CertificateEmail no longer has parameter id
  - Model CertificateEmail no longer has parameter kind
  - Model CertificateEmail no longer has parameter name
  - Model CertificateEmail no longer has parameter type
  - Model CertificateOrderAction no longer has parameter id
  - Model CertificateOrderAction no longer has parameter kind
  - Model CertificateOrderAction no longer has parameter name
  - Model CertificateOrderAction no longer has parameter type
  - Model ErrorResponse no longer has parameter code
  - Model ErrorResponse no longer has parameter message
  - Operation WebSiteManagementClientOperationsMixin.list_custom_host_name_sites has a new parameter hostname

## 6.1.0 (2022-01-24)

**Features**

  - Added operation WebAppsOperations.create_one_deploy_operation
  - Added operation WebAppsOperations.get_one_deploy_status

## 6.0.0 (2022-01-10)

**Features**

  - Added operation DomainsOperations.transfer_out
  - Added operation WebAppsOperations.get_auth_settings_v2_without_secrets
  - Added operation WebSiteManagementClientOperationsMixin.list_custom_host_name_sites
  - Added operation group ContainerAppsOperations
  - Added operation group ContainerAppsRevisionsOperations
  - Model KubeEnvironment has a new parameter container_apps_configuration
  - Model KubeEnvironment has a new parameter environment_type
  - Model KubeEnvironmentPatchResource has a new parameter container_apps_configuration
  - Model StaticSiteARMResource has a new parameter enterprise_grade_cdn_status
  - Model StaticSitePatchResource has a new parameter enterprise_grade_cdn_status

**Breaking changes**

  - Removed operation WebSiteManagementClientOperationsMixin.generate_github_access_token_for_appservice_cli_async

## 5.0.0 (2021-09-08)

**Features**

  - Model AppServicePlan has a new parameter zone_redundant
  - Model AppServicePlanPatchResource has a new parameter zone_redundant
  - Model AppServiceEnvironmentPatchResource has a new parameter zone_redundant
  - Model AppServiceEnvironmentResource has a new parameter zone_redundant
  - Model AzureActiveDirectoryRegistration has a new parameter client_secret_certificate_issuer
  - Model AzureActiveDirectoryRegistration has a new parameter client_secret_certificate_subject_alternative_name
  - Model AseV3NetworkingConfiguration has a new parameter external_inbound_ip_addresses
  - Model AseV3NetworkingConfiguration has a new parameter internal_inbound_ip_addresses
  - Model AppServiceEnvironment has a new parameter zone_redundant
  - Model ErrorEntity has a new parameter target
  - Model ErrorEntity has a new parameter details

**Breaking changes**

  - Model TokenStore no longer has parameter kind
  - Model TokenStore no longer has parameter id
  - Model TokenStore no longer has parameter name
  - Model TokenStore no longer has parameter type
  - Model IdentityProviders no longer has parameter kind
  - Model IdentityProviders no longer has parameter id
  - Model IdentityProviders no longer has parameter name
  - Model IdentityProviders no longer has parameter type
  - Model Google no longer has parameter kind
  - Model Google no longer has parameter id
  - Model Google no longer has parameter name
  - Model Google no longer has parameter type
  - Model Nonce no longer has parameter kind
  - Model Nonce no longer has parameter id
  - Model Nonce no longer has parameter name
  - Model Nonce no longer has parameter type
  - Model AppleRegistration no longer has parameter kind
  - Model AppleRegistration no longer has parameter id
  - Model AppleRegistration no longer has parameter name
  - Model AppleRegistration no longer has parameter type
  - Model ForwardProxy no longer has parameter kind
  - Model ForwardProxy no longer has parameter id
  - Model ForwardProxy no longer has parameter name
  - Model ForwardProxy no longer has parameter type
  - Model OpenIdConnectLogin no longer has parameter kind
  - Model OpenIdConnectLogin no longer has parameter id
  - Model OpenIdConnectLogin no longer has parameter name
  - Model OpenIdConnectLogin no longer has parameter type
  - Model AzureActiveDirectoryRegistration no longer has parameter kind
  - Model AzureActiveDirectoryRegistration no longer has parameter id
  - Model AzureActiveDirectoryRegistration no longer has parameter name
  - Model AzureActiveDirectoryRegistration no longer has parameter type
  - Model AzureActiveDirectoryLogin no longer has parameter kind
  - Model AzureActiveDirectoryLogin no longer has parameter id
  - Model AzureActiveDirectoryLogin no longer has parameter name
  - Model AzureActiveDirectoryLogin no longer has parameter type
  - Model TriggeredJobRun no longer has parameter kind
  - Model TriggeredJobRun no longer has parameter id
  - Model TriggeredJobRun no longer has parameter name
  - Model TriggeredJobRun no longer has parameter type
  - Model AppRegistration no longer has parameter kind
  - Model AppRegistration no longer has parameter id
  - Model AppRegistration no longer has parameter name
  - Model AppRegistration no longer has parameter type
  - Model VnetInfo no longer has parameter kind
  - Model VnetInfo no longer has parameter id
  - Model VnetInfo no longer has parameter name
  - Model VnetInfo no longer has parameter type
  - Model CustomOpenIdConnectProvider no longer has parameter kind
  - Model CustomOpenIdConnectProvider no longer has parameter id
  - Model CustomOpenIdConnectProvider no longer has parameter name
  - Model CustomOpenIdConnectProvider no longer has parameter type
  - Model TwitterRegistration no longer has parameter kind
  - Model TwitterRegistration no longer has parameter id
  - Model TwitterRegistration no longer has parameter name
  - Model TwitterRegistration no longer has parameter type
  - Model OpenIdConnectConfig no longer has parameter kind
  - Model OpenIdConnectConfig no longer has parameter id
  - Model OpenIdConnectConfig no longer has parameter name
  - Model OpenIdConnectConfig no longer has parameter type
  - Model AzureStaticWebApps no longer has parameter kind
  - Model AzureStaticWebApps no longer has parameter id
  - Model AzureStaticWebApps no longer has parameter name
  - Model AzureStaticWebApps no longer has parameter type
  - Model LegacyMicrosoftAccount no longer has parameter kind
  - Model LegacyMicrosoftAccount no longer has parameter id
  - Model LegacyMicrosoftAccount no longer has parameter name
  - Model LegacyMicrosoftAccount no longer has parameter type
  - Model AzureActiveDirectory no longer has parameter kind
  - Model AzureActiveDirectory no longer has parameter id
  - Model AzureActiveDirectory no longer has parameter name
  - Model AzureActiveDirectory no longer has parameter type
  - Model GitHub no longer has parameter kind
  - Model GitHub no longer has parameter id
  - Model GitHub no longer has parameter name
  - Model GitHub no longer has parameter type
  - Model HttpSettings no longer has parameter kind
  - Model HttpSettings no longer has parameter id
  - Model HttpSettings no longer has parameter name
  - Model HttpSettings no longer has parameter type
  - Model DetectorDefinition no longer has parameter kind
  - Model DetectorDefinition no longer has parameter id
  - Model DetectorDefinition no longer has parameter name
  - Model DetectorDefinition no longer has parameter type
  - Model Twitter no longer has parameter kind
  - Model Twitter no longer has parameter id
  - Model Twitter no longer has parameter name
  - Model Twitter no longer has parameter type
  - Model JwtClaimChecks no longer has parameter kind
  - Model JwtClaimChecks no longer has parameter id
  - Model JwtClaimChecks no longer has parameter name
  - Model JwtClaimChecks no longer has parameter type
  - Model CookieExpiration no longer has parameter kind
  - Model CookieExpiration no longer has parameter id
  - Model CookieExpiration no longer has parameter name
  - Model CookieExpiration no longer has parameter type
  - Model Apple no longer has parameter kind
  - Model Apple no longer has parameter id
  - Model Apple no longer has parameter name
  - Model Apple no longer has parameter type
  - Model OpenIdConnectRegistration no longer has parameter kind
  - Model OpenIdConnectRegistration no longer has parameter id
  - Model OpenIdConnectRegistration no longer has parameter name
  - Model OpenIdConnectRegistration no longer has parameter type
  - Model Login no longer has parameter kind
  - Model Login no longer has parameter id
  - Model Login no longer has parameter name
  - Model Login no longer has parameter type
  - Model Facebook no longer has parameter kind
  - Model Facebook no longer has parameter id
  - Model Facebook no longer has parameter name
  - Model Facebook no longer has parameter type
  - Model ClientRegistration no longer has parameter kind
  - Model ClientRegistration no longer has parameter id
  - Model ClientRegistration no longer has parameter name
  - Model ClientRegistration no longer has parameter type
  - Model GlobalValidation no longer has parameter kind
  - Model GlobalValidation no longer has parameter id
  - Model GlobalValidation no longer has parameter name
  - Model GlobalValidation no longer has parameter type
  - Model AuthPlatform no longer has parameter kind
  - Model AuthPlatform no longer has parameter id
  - Model AuthPlatform no longer has parameter name
  - Model AuthPlatform no longer has parameter type
  - Model FileSystemTokenStore has a new signature
  - Model AzureActiveDirectoryValidation has a new signature
  - Model LoginRoutes has a new signature
  - Model BlobStorageTokenStore has a new signature
  - Model OpenIdConnectClientCredential has a new signature
  - Model HttpSettingsRoutes has a new signature
  - Model LoginScopes has a new signature
  - Model AllowedAudiencesValidation has a new signature
  - Model AzureStaticWebAppsRegistration has a new signature

## 4.0.0 (2021-08-03)

**Features**

  - Model AppServicePlan has a new parameter elastic_scale_enabled
  - Added operation WebAppsOperations.update_swift_virtual_network_connection_with_check_slot
  - Added operation WebAppsOperations.create_or_update_swift_virtual_network_connection_with_check_slot
  - Added operation WebAppsOperations.update_swift_virtual_network_connection_with_check
  - Added operation WebAppsOperations.list_basic_publishing_credentials_policies
  - Added operation WebAppsOperations.list_basic_publishing_credentials_policies_slot

**Breaking changes**

  - Removed operation WebAppsOperations.get_basic_publishing_credentials_policies_slot
  - Removed operation WebAppsOperations.get_basic_publishing_credentials_policies

## 3.0.0 (2021-05-25)

**Features**

  - Model SiteAuthSettings has a new parameter config_version
  - Model CertificatePatchResource has a new parameter domain_validation_method
  - Model StaticSiteBuildProperties has a new parameter github_action_secret_name_override
  - Model StaticSiteBuildProperties has a new parameter output_location
  - Model StaticSiteBuildProperties has a new parameter api_build_command
  - Model StaticSiteBuildProperties has a new parameter skip_github_action_workflow_generation
  - Model StaticSiteBuildProperties has a new parameter app_build_command
  - Model DetectorResponse has a new parameter status
  - Model DetectorResponse has a new parameter data_providers_metadata
  - Model DetectorResponse has a new parameter suggested_utterances
  - Model StaticSitePatchResource has a new parameter key_vault_reference_identity
  - Model StaticSitePatchResource has a new parameter private_endpoint_connections
  - Model StaticSitePatchResource has a new parameter user_provided_function_apps
  - Model StaticSitePatchResource has a new parameter allow_config_file_updates
  - Model StaticSitePatchResource has a new parameter template_properties
  - Model StaticSitePatchResource has a new parameter staging_environment_policy
  - Model StaticSitePatchResource has a new parameter content_distribution_endpoint
  - Model StaticSitePatchResource has a new parameter provider
  - Model SiteConfigResource has a new parameter key_vault_reference_identity
  - Model SiteConfigResource has a new parameter functions_runtime_scale_monitoring_enabled
  - Model SiteConfigResource has a new parameter acr_user_managed_identity_id
  - Model SiteConfigResource has a new parameter public_network_access
  - Model SiteConfigResource has a new parameter website_time_zone
  - Model SiteConfigResource has a new parameter acr_use_managed_identity_creds
  - Model SiteConfigResource has a new parameter minimum_elastic_instance_count
  - Model SiteConfigResource has a new parameter function_app_scale_limit
  - Model SiteConfigResource has a new parameter azure_storage_accounts
  - Model ValidateRequest has a new parameter app_service_environment
  - Model StaticSiteCustomDomainOverviewARMResource has a new parameter status
  - Model StaticSiteCustomDomainOverviewARMResource has a new parameter error_message
  - Model StaticSiteCustomDomainOverviewARMResource has a new parameter validation_token
  - Model AppServicePlan has a new parameter extended_location
  - Model AppServicePlan has a new parameter kube_environment_profile
  - Model StaticSiteBuildARMResource has a new parameter user_provided_function_apps
  - Model AppServiceCertificateOrder has a new parameter contact
  - Model VnetParameters has a new parameter subnet_resource_id
  - Model SkuCapacity has a new parameter elastic_maximum
  - Model ApplicationStackResource has a new parameter is_deprecated
  - Model StackMajorVersion has a new parameter site_config_properties_dictionary
  - Model StackMajorVersion has a new parameter app_settings_dictionary
  - Model StatusCodesBasedTrigger has a new parameter path
  - Model AppServiceCertificateOrderPatchResource has a new parameter contact
  - Model BillingMeter has a new parameter multiplier
  - Model IdentityProviders has a new parameter legacy_microsoft_account
  - Model IdentityProviders has a new parameter apple
  - Model IdentityProviders has a new parameter azure_static_web_apps
  - Model StaticSiteARMResource has a new parameter key_vault_reference_identity
  - Model StaticSiteARMResource has a new parameter private_endpoint_connections
  - Model StaticSiteARMResource has a new parameter user_provided_function_apps
  - Model StaticSiteARMResource has a new parameter identity
  - Model StaticSiteARMResource has a new parameter allow_config_file_updates
  - Model StaticSiteARMResource has a new parameter template_properties
  - Model StaticSiteARMResource has a new parameter staging_environment_policy
  - Model StaticSiteARMResource has a new parameter content_distribution_endpoint
  - Model StaticSiteARMResource has a new parameter provider
  - Model SitePatchResource has a new parameter virtual_network_subnet_id
  - Model SitePatchResource has a new parameter storage_account_required
  - Model SitePatchResource has a new parameter key_vault_reference_identity
  - Model ApiKVReference has a new parameter name
  - Model ApiKVReference has a new parameter active_version
  - Model ApiKVReference has a new parameter type
  - Model ApiKVReference has a new parameter id
  - Model ApiKVReference has a new parameter kind
  - Model VnetValidationFailureDetails has a new parameter message
  - Model VnetValidationFailureDetails has a new parameter warnings
  - Model Site has a new parameter virtual_network_subnet_id
  - Model Site has a new parameter storage_account_required
  - Model Site has a new parameter extended_location
  - Model Site has a new parameter key_vault_reference_identity
  - Model Certificate has a new parameter domain_validation_method
  - Model CsmOperationDescription has a new parameter is_data_action
  - Model AutoHealTriggers has a new parameter slow_requests_with_path
  - Model AutoHealTriggers has a new parameter status_codes_range
  - Model SiteConfig has a new parameter key_vault_reference_identity
  - Model SiteConfig has a new parameter functions_runtime_scale_monitoring_enabled
  - Model SiteConfig has a new parameter acr_user_managed_identity_id
  - Model SiteConfig has a new parameter public_network_access
  - Model SiteConfig has a new parameter website_time_zone
  - Model SiteConfig has a new parameter acr_use_managed_identity_creds
  - Model SiteConfig has a new parameter minimum_elastic_instance_count
  - Model SiteConfig has a new parameter function_app_scale_limit
  - Model SiteConfig has a new parameter azure_storage_accounts
  - Model SlowRequestsBasedTrigger has a new parameter path
  - Model AppServicePlanPatchResource has a new parameter elastic_scale_enabled
  - Model AppServicePlanPatchResource has a new parameter kube_environment_profile
  - Model ApplicationStack has a new parameter is_deprecated
  - Model SiteSourceControl has a new parameter git_hub_action_configuration
  - Added operation ProviderOperations.get_function_app_stacks
  - Added operation ProviderOperations.get_web_app_stacks_for_location
  - Added operation ProviderOperations.get_web_app_stacks
  - Added operation ProviderOperations.get_function_app_stacks_for_location
  - Added operation StaticSitesOperations.get_private_endpoint_connection_list
  - Added operation StaticSitesOperations.detach_user_provided_function_app_from_static_site_build
  - Added operation StaticSitesOperations.begin_create_or_update_static_site
  - Added operation StaticSitesOperations.create_or_update_static_site_build_app_settings
  - Added operation StaticSitesOperations.begin_create_or_update_static_site_custom_domain
  - Added operation StaticSitesOperations.list_static_site_app_settings
  - Added operation StaticSitesOperations.begin_delete_private_endpoint_connection
  - Added operation StaticSitesOperations.detach_user_provided_function_app_from_static_site
  - Added operation StaticSitesOperations.begin_register_user_provided_function_app_with_static_site
  - Added operation StaticSitesOperations.begin_create_zip_deployment_for_static_site
  - Added operation StaticSitesOperations.begin_register_user_provided_function_app_with_static_site_build
  - Added operation StaticSitesOperations.list_static_site_configured_roles
  - Added operation StaticSitesOperations.begin_create_zip_deployment_for_static_site_build
  - Added operation StaticSitesOperations.begin_detach_static_site
  - Added operation StaticSitesOperations.get_private_endpoint_connection
  - Added operation StaticSitesOperations.begin_validate_custom_domain_can_be_added_to_static_site
  - Added operation StaticSitesOperations.create_or_update_static_site_app_settings
  - Added operation StaticSitesOperations.begin_delete_static_site_custom_domain
  - Added operation StaticSitesOperations.get_user_provided_function_app_for_static_site_build
  - Added operation StaticSitesOperations.get_user_provided_function_app_for_static_site
  - Added operation StaticSitesOperations.begin_approve_or_reject_private_endpoint_connection
  - Added operation StaticSitesOperations.begin_delete_static_site_build
  - Added operation StaticSitesOperations.get_static_site_custom_domain
  - Added operation StaticSitesOperations.begin_delete_static_site
  - Added operation StaticSitesOperations.get_user_provided_function_apps_for_static_site
  - Added operation StaticSitesOperations.get_user_provided_function_apps_for_static_site_build
  - Added operation StaticSitesOperations.get_private_link_resources
  - Added operation StaticSitesOperations.list_static_site_build_app_settings
  - Added operation AppServiceEnvironmentsOperations.get_private_endpoint_connection_list
  - Added operation AppServiceEnvironmentsOperations.get_private_link_resources
  - Added operation AppServiceEnvironmentsOperations.get_ase_v3_networking_configuration
  - Added operation AppServiceEnvironmentsOperations.get_private_endpoint_connection
  - Added operation AppServiceEnvironmentsOperations.begin_approve_or_reject_private_endpoint_connection
  - Added operation AppServiceEnvironmentsOperations.begin_delete_private_endpoint_connection
  - Added operation AppServiceEnvironmentsOperations.update_ase_networking_configuration
  - Added operation WebAppsOperations.update_ftp_allowed_slot
  - Added operation WebAppsOperations.get_private_endpoint_connection_list
  - Added operation WebAppsOperations.get_private_link_resources_slot
  - Added operation WebAppsOperations.get_site_connection_string_key_vault_reference
  - Added operation WebAppsOperations.get_ftp_allowed_slot
  - Added operation WebAppsOperations.get_site_connection_string_key_vault_reference_slot
  - Added operation WebAppsOperations.get_app_settings_key_vault_references
  - Added operation WebAppsOperations.get_site_connection_string_key_vault_references_slot
  - Added operation WebAppsOperations.get_app_settings_key_vault_references_slot
  - Added operation WebAppsOperations.get_app_setting_key_vault_reference_slot
  - Added operation WebAppsOperations.get_app_setting_key_vault_reference
  - Added operation WebAppsOperations.update_scm_allowed_slot
  - Added operation WebAppsOperations.get_private_endpoint_connection_list_slot
  - Added operation WebAppsOperations.get_scm_allowed_slot
  - Added operation WebAppsOperations.get_basic_publishing_credentials_policies_slot
  - Added operation WebAppsOperations.create_or_update_swift_virtual_network_connection_with_check
  - Added operation WebAppsOperations.get_private_endpoint_connection_slot
  - Added operation WebAppsOperations.begin_approve_or_reject_private_endpoint_connection_slot
  - Added operation WebAppsOperations.get_site_connection_string_key_vault_references
  - Added operation WebAppsOperations.begin_delete_private_endpoint_connection_slot
  - Added operation group KubeEnvironmentsOperations
  - Added operation group GlobalOperations
  - Added operation group CertificateOrdersDiagnosticsOperations

**Breaking changes**

  - Parameter id of model VirtualNetworkProfile is now required
  - Operation StaticSitesOperations.list_static_site_build_function_app_settings has a new signature
  - Operation StaticSitesOperations.list_static_site_build_functions has a new signature
  - Operation StaticSitesOperations.create_or_update_static_site_build_function_app_settings has a new signature
  - Operation StaticSitesOperations.get_static_site_build has a new signature
  - Operation CertificatesOperations.list has a new signature
  - Operation WebAppsOperations.delete_source_control has a new signature
  - Operation WebAppsOperations.delete_source_control_slot has a new signature
  - Model SwiftVirtualNetwork no longer has parameter system_data
  - Model CertificateOrderAction no longer has parameter system_data
  - Model GeoRegion no longer has parameter system_data
  - Model SiteAuthSettings no longer has parameter system_data
  - Model CsmPublishingCredentialsPoliciesCollection no longer has parameter system_data
  - Model AddressResponse no longer has parameter system_data
  - Model SiteLogsConfig no longer has parameter system_data
  - Model PrivateLinkConnectionApprovalRequestResource no longer has parameter system_data
  - Model PublicCertificate no longer has parameter system_data
  - Model Nonce no longer has parameter system_data
  - Model CertificatePatchResource no longer has parameter system_data
  - Model StorageMigrationOptions no longer has parameter system_data
  - Model DiagnosticCategory no longer has parameter system_data
  - Model DetectorResponse no longer has parameter system_data
  - Model CustomOpenIdConnectProvider no longer has parameter system_data
  - Model StaticSitePatchResource no longer has parameter system_data
  - Model CookieExpiration no longer has parameter system_data
  - Model MSDeployStatus no longer has parameter system_data
  - Model StaticSiteResetPropertiesARMResource no longer has parameter system_data
  - Model MSDeploy no longer has parameter system_data
  - Model DiagnosticDetectorResponse no longer has parameter system_data
  - Model DiagnosticAnalysis no longer has parameter system_data
  - Model SiteConfigResource no longer has parameter system_data
  - Model Recommendation no longer has parameter system_data
  - Model DeletedAppRestoreRequest no longer has parameter system_data
  - Model SlotConfigNamesResource no longer has parameter system_data
  - Model Domain no longer has parameter system_data
  - Model StorageMigrationResponse no longer has parameter system_data
  - Model VnetInfo no longer has parameter system_data
  - Model AzureActiveDirectoryLogin no longer has parameter system_data
  - Model SlotDifference no longer has parameter system_data
  - Model StaticSiteUserInvitationRequestResource no longer has parameter system_data
  - Model BackupRequest no longer has parameter system_data
  - Model PushSettings no longer has parameter system_data
  - Model StaticSiteCustomDomainOverviewARMResource no longer has parameter system_data
  - Model AppServicePlan no longer has parameter system_data
  - Model Google no longer has parameter system_data
  - Model Twitter no longer has parameter system_data
  - Model DomainOwnershipIdentifier no longer has parameter system_data
  - Model OpenIdConnectClientCredential no longer has parameter system_data
  - Model Identifier no longer has parameter system_data
  - Model RestoreRequest no longer has parameter system_data
  - Model SiteConfigurationSnapshotInfo no longer has parameter system_data
  - Model VnetRoute no longer has parameter system_data
  - Model StaticSiteBuildARMResource no longer has parameter system_data
  - Model SourceControl no longer has parameter system_data
  - Model AppServiceCertificateOrder no longer has parameter system_data
  - Model AzureActiveDirectory no longer has parameter system_data
  - Model DomainPatchResource no longer has parameter system_data
  - Model Resource no longer has parameter system_data
  - Model SiteAuthSettingsV2 no longer has parameter system_data
  - Model VnetParameters no longer has parameter system_data
  - Model ResourceMetricDefinition no longer has parameter system_data
  - Model LoginScopes no longer has parameter system_data
  - Model CertificateEmail no longer has parameter system_data
  - Model PremierAddOn no longer has parameter system_data
  - Model TriggeredJobRun no longer has parameter system_data
  - Model WebJob no longer has parameter system_data
  - Model StaticSiteUserARMResource no longer has parameter system_data
  - Model HybridConnectionKey no longer has parameter system_data
  - Model Deployment no longer has parameter system_data
  - Model PrivateAccess no longer has parameter system_data
  - Model VnetValidationTestFailure no longer has parameter system_data
  - Model StaticSitesWorkflowPreview no longer has parameter system_data
  - Model OpenIdConnectRegistration no longer has parameter system_data
  - Model ProxyOnlyResource no longer has parameter system_data
  - Model ApplicationStackResource no longer has parameter system_data
  - Model AzureStoragePropertyDictionaryResource no longer has parameter system_data
  - Model TwitterRegistration no longer has parameter system_data
  - Model RelayServiceConnectionEntity no longer has parameter system_data
  - Model CsmPublishingCredentialsPoliciesEntity no longer has parameter system_data
  - Model LoginRoutes no longer has parameter system_data
  - Model AnalysisDefinition no longer has parameter system_data
  - Model ReissueCertificateOrderRequest no longer has parameter system_data
  - Model User no longer has parameter system_data
  - Model AppServiceCertificateOrderPatchResource no longer has parameter system_data
  - Model TriggeredWebJob no longer has parameter system_data
  - Model HybridConnection no longer has parameter system_data
  - Model HttpSettingsRoutes no longer has parameter system_data
  - Model BillingMeter no longer has parameter system_data
  - Model SiteExtensionInfo no longer has parameter system_data
  - Model IdentityProviders no longer has parameter system_data
  - Model Snapshot no longer has parameter system_data
  - Model StaticSitesWorkflowPreviewRequest no longer has parameter system_data
  - Model HostNameBinding no longer has parameter system_data
  - Model AzureActiveDirectoryRegistration no longer has parameter system_data
  - Model StaticSiteARMResource no longer has parameter system_data
  - Model MigrateMySqlRequest no longer has parameter system_data
  - Model VnetGateway no longer has parameter system_data
  - Model ProcessInfo no longer has parameter system_data
  - Model WebSiteInstanceStatus no longer has parameter system_data
  - Model SitePatchResource no longer has parameter system_data
  - Model GitHub no longer has parameter system_data
  - Model TokenStore no longer has parameter system_data
  - Model ContinuousWebJob no longer has parameter system_data
  - Model FunctionEnvelope no longer has parameter system_data
  - Model BlobStorageTokenStore no longer has parameter system_data
  - Model PremierAddOnOffer no longer has parameter system_data
  - Model ProcessThreadInfo no longer has parameter system_data
  - Model ApiKVReference no longer has parameter location
  - Model AzureActiveDirectoryValidation no longer has parameter system_data
  - Model SnapshotRestoreRequest no longer has parameter system_data
  - Model DeletedSite no longer has parameter system_data
  - Model VnetValidationFailureDetails no longer has parameter system_data
  - Model Site no longer has parameter system_data
  - Model StaticSiteFunctionOverviewARMResource no longer has parameter system_data
  - Model RenewCertificateOrderRequest no longer has parameter system_data
  - Model Certificate no longer has parameter system_data
  - Model NetworkFeatures no longer has parameter system_data
  - Model ResourceHealthMetadata no longer has parameter system_data
  - Model DetectorDefinition no longer has parameter system_data
  - Model BackupItem no longer has parameter system_data
  - Model TriggeredJobHistory no longer has parameter system_data
  - Model Usage no longer has parameter system_data
  - Model MigrateMySqlStatus no longer has parameter system_data
  - Model ConnectionStringDictionary no longer has parameter system_data
  - Model CustomHostnameAnalysisResult no longer has parameter system_data
  - Model StringDictionary no longer has parameter system_data
  - Model TopLevelDomain no longer has parameter system_data
  - Model PremierAddOnPatchResource no longer has parameter system_data
  - Model AppServiceCertificatePatchResource no longer has parameter system_data
  - Model AllowedAudiencesValidation no longer has parameter system_data
  - Model Facebook no longer has parameter system_data
  - Model ClientRegistration no longer has parameter system_data
  - Model StaticSiteUserInvitationResponseResource no longer has parameter system_data
  - Model HybridConnectionLimits no longer has parameter system_data
  - Model RecommendationRule no longer has parameter system_data
  - Model ForwardProxy no longer has parameter system_data
  - Model Login no longer has parameter system_data
  - Model OpenIdConnectConfig no longer has parameter system_data
  - Model AppServiceCertificateResource no longer has parameter system_data
  - Model MSDeployLog no longer has parameter system_data
  - Model WorkerPoolResource no longer has parameter system_data
  - Model SitePhpErrorLogFlag no longer has parameter system_data
  - Model AppServicePlanPatchResource no longer has parameter system_data
  - Model OpenIdConnectLogin no longer has parameter system_data
  - Model SiteSourceControl no longer has parameter system_data
  - Model AuthPlatform no longer has parameter system_data
  - Model FileSystemTokenStore no longer has parameter system_data
  - Model AppRegistration no longer has parameter system_data
  - Model ProcessModuleInfo no longer has parameter system_data
  - Model HttpSettings no longer has parameter system_data
  - Model GlobalValidation no longer has parameter system_data
  - Model JwtClaimChecks no longer has parameter system_data
  - Model AppServiceEnvironmentResource has a new signature
  - Model AppServiceEnvironment has a new signature
  - Model DetectorInfo has a new signature
  - Model AppServiceEnvironmentPatchResource has a new signature
  - Removed operation StaticSitesOperations.create_or_update_static_site
  - Removed operation StaticSitesOperations.validate_custom_domain_can_be_added_to_static_site
  - Removed operation StaticSitesOperations.delete_static_site_custom_domain
  - Removed operation StaticSitesOperations.delete_static_site_build
  - Removed operation StaticSitesOperations.delete_static_site
  - Removed operation StaticSitesOperations.create_or_update_static_site_custom_domain
  - Removed operation StaticSitesOperations.detach_static_site
  - Removed operation WebAppsOperations.update_swift_virtual_network_connection
  - Removed operation WebAppsOperations.begin_copy_production_slot
  - Removed operation WebAppsOperations.create_or_update_swift_virtual_network_connection_slot
  - Removed operation WebAppsOperations.update_swift_virtual_network_connection_slot
  - Removed operation WebAppsOperations.create_or_update_swift_virtual_network_connection
  - Removed operation WebAppsOperations.begin_copy_slot

## 2.0.0 (2021-02-25)

**Features**

  - Model Usage has a new parameter system_data
  - Model StaticSiteFunctionOverviewARMResource has a new parameter system_data
  - Model HybridConnection has a new parameter system_data
  - Model GeoRegion has a new parameter system_data
  - Model IpSecurityRestriction has a new parameter headers
  - Model StaticSiteBuildARMResource has a new parameter system_data
  - Model PushSettings has a new parameter system_data
  - Model SlotDifference has a new parameter system_data
  - Model AppServiceCertificatePatchResource has a new parameter system_data
  - Model DiagnosticDetectorResponse has a new parameter system_data
  - Model MetricSpecification has a new parameter supported_aggregation_types
  - Model PremierAddOnPatchResource has a new parameter system_data
  - Model SitePatchResource has a new parameter custom_domain_verification_id
  - Model SitePatchResource has a new parameter system_data
  - Model SitePatchResource has a new parameter client_cert_mode
  - Model HostNameBinding has a new parameter system_data
  - Model CustomHostnameAnalysisResult has a new parameter system_data
  - Model VnetGateway has a new parameter system_data
  - Model MSDeployLog has a new parameter system_data
  - Model Site has a new parameter custom_domain_verification_id
  - Model Site has a new parameter system_data
  - Model Site has a new parameter client_cert_mode
  - Model PrivateEndpointConnectionResource has a new parameter system_data
  - Model ResourceHealthMetadata has a new parameter system_data
  - Model CertificatePatchResource has a new parameter system_data
  - Model WorkerPoolResource has a new parameter system_data
  - Model AppServiceEnvironmentResource has a new parameter system_data
  - Model DetectorResponse has a new parameter system_data
  - Model TriggeredWebJob has a new parameter system_data
  - Model SiteSourceControl has a new parameter is_git_hub_action
  - Model SiteSourceControl has a new parameter system_data
  - Model MSDeploy has a new parameter system_data
  - Model TriggeredJobHistory has a new parameter system_data
  - Model SiteConfigResource has a new parameter vnet_route_all_enabled
  - Model SiteConfigResource has a new parameter system_data
  - Model SiteConfigResource has a new parameter scm_min_tls_version
  - Model SiteConfigResource has a new parameter vnet_private_ports_count
  - Model BackupRequest has a new parameter system_data
  - Model DeletedSite has a new parameter system_data
  - Model RenewCertificateOrderRequest has a new parameter system_data
  - Model StorageMigrationResponse has a new parameter system_data
  - Model CsmPublishingCredentialsPoliciesCollection has a new parameter system_data
  - Model AddressResponse has a new parameter system_data
  - Model BillingMeter has a new parameter system_data
  - Model Deployment has a new parameter system_data
  - Model ProcessModuleInfo has a new parameter system_data
  - Model CertificateEmail has a new parameter system_data
  - Model Certificate has a new parameter system_data
  - Model StaticSitePatchResource has a new parameter system_data
  - Model SitePhpErrorLogFlag has a new parameter system_data
  - Model CsmPublishingCredentialsPoliciesEntity has a new parameter system_data
  - Model SwiftVirtualNetwork has a new parameter system_data
  - Model VnetRoute has a new parameter system_data
  - Model ConnectionStringDictionary has a new parameter system_data
  - Model WebSiteInstanceStatus has a new parameter system_data
  - Model WebSiteInstanceStatus has a new parameter health_check_url
  - Model HybridConnectionKey has a new parameter system_data
  - Model PremierAddOnOffer has a new parameter system_data
  - Model ContinuousWebJob has a new parameter system_data
  - Model SnapshotRestoreRequest has a new parameter system_data
  - Model SiteAuthSettings has a new parameter git_hub_client_id
  - Model SiteAuthSettings has a new parameter microsoft_account_client_secret_setting_name
  - Model SiteAuthSettings has a new parameter git_hub_client_secret
  - Model SiteAuthSettings has a new parameter is_auth_from_file
  - Model SiteAuthSettings has a new parameter auth_file_path
  - Model SiteAuthSettings has a new parameter google_client_secret_setting_name
  - Model SiteAuthSettings has a new parameter git_hub_client_secret_setting_name
  - Model SiteAuthSettings has a new parameter aad_claims_authorization
  - Model SiteAuthSettings has a new parameter system_data
  - Model SiteAuthSettings has a new parameter git_hub_o_auth_scopes
  - Model SiteAuthSettings has a new parameter client_secret_setting_name
  - Model SiteAuthSettings has a new parameter twitter_consumer_secret_setting_name
  - Model SiteAuthSettings has a new parameter facebook_app_secret_setting_name
  - Model DetectorDefinition has a new parameter system_data
  - Model SiteConfigurationSnapshotInfo has a new parameter system_data
  - Model PublicCertificate has a new parameter system_data
  - Model DomainOwnershipIdentifier has a new parameter system_data
  - Model StringDictionary has a new parameter system_data
  - Model PrivateLinkConnectionApprovalRequestResource has a new parameter system_data
  - Model SlotConfigNamesResource has a new parameter system_data
  - Model WebJob has a new parameter system_data
  - Model ApplicationStackResource has a new parameter system_data
  - Model ReissueCertificateOrderRequest has a new parameter system_data
  - Model User has a new parameter system_data
  - Model RestoreRequest has a new parameter system_data
  - Model StaticSiteUserInvitationRequestResource has a new parameter system_data
  - Model StorageMigrationOptions has a new parameter system_data
  - Model HybridConnectionLimits has a new parameter system_data
  - Model StaticSiteUserARMResource has a new parameter system_data
  - Model AppServiceCertificateResource has a new parameter system_data
  - Model AnalysisDefinition has a new parameter system_data
  - Model VnetInfo has a new parameter system_data
  - Model DomainPatchResource has a new parameter system_data
  - Model MSDeployStatus has a new parameter system_data
  - Model MigrateMySqlRequest has a new parameter system_data
  - Model Identifier has a new parameter system_data
  - Model SiteLogsConfig has a new parameter system_data
  - Model AppServiceCertificateOrder has a new parameter system_data
  - Model BackupItem has a new parameter system_data
  - Model ProcessInfo has a new parameter system_data
  - Model MigrateMySqlStatus has a new parameter system_data
  - Model StaticSiteResetPropertiesARMResource has a new parameter system_data
  - Model NetworkFeatures has a new parameter system_data
  - Model Recommendation has a new parameter system_data
  - Model ProcessThreadInfo has a new parameter system_data
  - Model AzureStoragePropertyDictionaryResource has a new parameter system_data
  - Model Domain has a new parameter system_data
  - Model StaticSiteARMResource has a new parameter system_data
  - Model ResourceMetricDefinition has a new parameter system_data
  - Model VnetValidationTestFailure has a new parameter system_data
  - Model StaticSiteUserInvitationResponseResource has a new parameter system_data
  - Model PrivateAccess has a new parameter system_data
  - Model SiteConfig has a new parameter vnet_route_all_enabled
  - Model SiteConfig has a new parameter vnet_private_ports_count
  - Model SiteConfig has a new parameter scm_min_tls_version
  - Model FunctionEnvelope has a new parameter system_data
  - Model TopLevelDomain has a new parameter system_data
  - Model RecommendationRule has a new parameter system_data
  - Model RelayServiceConnectionEntity has a new parameter system_data
  - Model ProxyOnlyResource has a new parameter system_data
  - Model Snapshot has a new parameter system_data
  - Model VnetParameters has a new parameter system_data
  - Model DiagnosticAnalysis has a new parameter system_data
  - Model CertificateOrderAction has a new parameter system_data
  - Model DeletedAppRestoreRequest has a new parameter system_data
  - Model AppServicePlan has a new parameter system_data
  - Model Resource has a new parameter system_data
  - Model StaticSiteCustomDomainOverviewARMResource has a new parameter system_data
  - Model PremierAddOn has a new parameter system_data
  - Model TriggeredJobRun has a new parameter system_data
  - Model LogSpecification has a new parameter log_filter_pattern
  - Model DiagnosticCategory has a new parameter system_data
  - Model SourceControl has a new parameter system_data
  - Model VnetValidationFailureDetails has a new parameter system_data
  - Model AppServiceEnvironmentPatchResource has a new parameter system_data
  - Model AppServiceCertificateOrderPatchResource has a new parameter system_data
  - Model SiteExtensionInfo has a new parameter system_data
  - Model AppServicePlanPatchResource has a new parameter system_data
  - Added operation WebAppsOperations.update_auth_settings_v2
  - Added operation WebAppsOperations.update_auth_settings_v2_slot
  - Added operation WebAppsOperations.get_auth_settings_v2
  - Added operation WebAppsOperations.get_auth_settings_v2_slot
  - Added operation StaticSitesOperations.preview_workflow
  - Added operation WebSiteManagementClientOperationsMixin.generate_github_access_token_for_appservice_cli_async

**Breaking changes**

  - Model SiteConfigResource no longer has parameter acr_use_managed_identity_creds
  - Model SiteConfigResource no longer has parameter acr_user_managed_identity_id
  - Model SiteConfig no longer has parameter acr_use_managed_identity_creds
  - Model SiteConfig no longer has parameter acr_user_managed_identity_id
  - Model FunctionSecrets has a new signature
  - Removed operation WebAppsOperations.get_app_settings_key_vault_references
  - Removed operation WebAppsOperations.get_app_setting_key_vault_reference

## 1.0.0 (2020-11-23)

- GA release

## 1.0.0b1 (2020-10-13)

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

## 0.48.0 (2020-09-22)

**Features**

  - Model SiteConfig has a new parameter acr_use_managed_identity_creds
  - Model SiteConfig has a new parameter acr_user_managed_identity_id
  - Model SiteConfigResource has a new parameter acr_use_managed_identity_creds
  - Model SiteConfigResource has a new parameter acr_user_managed_identity_id

## 0.47.0 (2020-06-03)

**Features**

  - Added operation WebAppsOperations.get_basic_publishing_credentials_policies
  - Added operation WebAppsOperations.update_scm_allowed
  - Added operation WebAppsOperations.update_ftp_allowed
  - Added operation WebAppsOperations.get_scm_allowed
  - Added operation WebAppsOperations.get_ftp_allowed

## 0.46.0 (2020-04-10)

**Features**

  - Model SiteConfig has a new parameter power_shell_version
  - Model SiteConfigResource has a new parameter power_shell_version
  - Added operation WebAppsOperations.get_private_endpoint_connection
  - Added operation WebAppsOperations.get_private_link_resources
  - Added operation WebAppsOperations.delete_private_endpoint_connection
  - Added operation WebAppsOperations.approve_or_reject_private_endpoint_connection

## 0.45.0 (2020-03-20)

**Features**

  - Added operation WebAppsOperations.list_host_keys
  - Added operation WebAppsOperations.sync_functions
  - Added operation WebAppsOperations.list_function_keys_slot
  - Added operation WebAppsOperations.sync_functions_slot
  - Added operation WebAppsOperations.delete_function_secret
  - Added operation WebAppsOperations.delete_host_secret_slot
  - Added operation WebAppsOperations.list_host_keys_slot
  - Added operation WebAppsOperations.delete_function_secret_slot
  - Added operation WebAppsOperations.create_or_update_host_secret
  - Added operation WebAppsOperations.list_sync_status
  - Added operation WebAppsOperations.list_sync_status_slot
  - Added operation WebAppsOperations.create_or_update_function_secret_slot
  - Added operation WebAppsOperations.list_function_keys
  - Added operation WebAppsOperations.create_or_update_host_secret_slot
  - Added operation WebAppsOperations.create_or_update_function_secret
  - Added operation WebAppsOperations.delete_host_secret
  - Added operation group StaticSitesOperations

## 0.44.0 (2019-11-08)

**Features**

  - Model EndpointDetail has a new parameter is_accessible
  - Model Identifier has a new parameter value
  - Model VirtualIPMapping has a new parameter service_name
  - Model SiteConfig has a new parameter health_check_path
  - Model SiteConfig has a new parameter pre_warmed_instance_count
  - Model SiteConfig has a new parameter api_management_config
  - Model CertificatePatchResource has a new parameter canonical_name
  - Model ValidateRequest has a new parameter container_image_platform
  - Model ValidateRequest has a new parameter
    container_registry_password
  - Model ValidateRequest has a new parameter
    container_image_repository
  - Model ValidateRequest has a new parameter container_image_tag
  - Model ValidateRequest has a new parameter
    container_registry_base_url
  - Model ValidateRequest has a new parameter
    container_registry_username
  - Model MetricSpecification has a new parameter
    supported_time_grain_types
  - Model FunctionEnvelope has a new parameter invoke_url_template
  - Model FunctionEnvelope has a new parameter is_disabled
  - Model FunctionEnvelope has a new parameter language
  - Model FunctionEnvelope has a new parameter test_data_href
  - Model GeoRegion has a new parameter org_domain
  - Model Certificate has a new parameter canonical_name
  - Model StackMajorVersion has a new parameter is_deprecated
  - Model StackMajorVersion has a new parameter is_hidden
  - Model StackMajorVersion has a new parameter is_preview
  - Model SiteConfigResource has a new parameter health_check_path
  - Model SiteConfigResource has a new parameter
    pre_warmed_instance_count
  - Model SiteConfigResource has a new parameter api_management_config
  - Model HostingEnvironmentDiagnostics has a new parameter
    diagnostics_output
  - Model AddressResponse has a new parameter type
  - Model AddressResponse has a new parameter id
  - Model AddressResponse has a new parameter name
  - Model AddressResponse has a new parameter kind
  - Added operation AppServiceEnvironmentsOperations.get_vip_info
  - Added operation WebAppsOperations.copy_production_slot
  - Added operation WebAppsOperations.list_site_backups
  - Added operation
    WebAppsOperations.get_app_setting_key_vault_reference
  - Added operation
    WebAppsOperations.get_app_settings_key_vault_references
  - Added operation WebAppsOperations.copy_slot_slot
  - Added operation WebAppsOperations.get_instance_info_slot
  - Added operation WebAppsOperations.get_instance_info
  - Added operation WebAppsOperations.list_site_backups_slot

**Breaking changes**

  - Operation
    WebAppsOperations.create_or_update_domain_ownership_identifier
    has a new signature
  - Operation
    WebAppsOperations.create_or_update_domain_ownership_identifier_slot
    has a new signature
  - Operation
    WebAppsOperations.update_domain_ownership_identifier_slot has a
    new signature
  - Operation WebAppsOperations.update_domain_ownership_identifier
    has a new signature
  - Model SitePatchResource no longer has parameter geo_distributions
  - Model Site no longer has parameter geo_distributions
  - Model EndpointDetail no longer has parameter is_accessable
  - Model ProcessThreadInfo no longer has parameter
    priviledged_processor_time
  - Model Identifier no longer has parameter identifier_id
  - Model SiteConfig no longer has parameter reserved_instance_count
  - Model SiteConfig no longer has parameter azure_storage_accounts
  - Model SiteConfigResource no longer has parameter
    reserved_instance_count
  - Model SiteConfigResource no longer has parameter
    azure_storage_accounts
  - Model HostingEnvironmentDiagnostics no longer has parameter
    diagnosics_output
  - Removed operation AppServicePlansOperations.list_metric_defintions
  - Removed operation AppServicePlansOperations.list_metrics
  - Removed operation
    WebSiteManagementClientOperationsMixin.validate_container_settings
  - Removed operation AppServiceEnvironmentsOperations.list_metrics
  - Removed operation
    AppServiceEnvironmentsOperations.list_worker_pool_instance_metrics
  - Removed operation
    AppServiceEnvironmentsOperations.list_multi_role_pool_instance_metrics
  - Removed operation
    AppServiceEnvironmentsOperations.list_multi_role_metrics
  - Removed operation AppServiceEnvironmentsOperations.list_vips
  - Removed operation
    AppServiceEnvironmentsOperations.list_web_worker_metrics
  - Removed operation
    AppServiceEnvironmentsOperations.list_metric_definitions
  - Removed operation WebAppsOperations.get_instance_process_thread
  - Removed operation WebAppsOperations.list_metrics
  - Removed operation WebAppsOperations.get_process_thread
  - Removed operation WebAppsOperations.list_hybrid_connection_keys
  - Removed operation WebAppsOperations.list_metric_definitions_slot
  - Removed operation WebAppsOperations.list_metrics_slot
  - Removed operation WebAppsOperations.get_process_thread_slot
  - Removed operation
    WebAppsOperations.list_hybrid_connection_keys_slot
  - Removed operation
    WebAppsOperations.get_instance_process_thread_slot
  - Removed operation WebAppsOperations.list_metric_definitions

## 0.43.1 (2019-10-17)

**General**

  - Fixed incorrectly generated multi-api package structure

## 0.43.0 (2019-10-01)

**Features**

  - Added operation group BillingMetersOperations
  - Added operation group WebSiteManagementClientOperationsMixin

**General**

  - Package is now multiapi

## 0.42.0 (2019-05-24)

**Features**

  - Model SitePatchResource has a new parameter identity
  - Model ManagedServiceIdentity has a new parameter
    user_assigned_identities
  - Model CloningInfo has a new parameter source_web_app_location
  - Added operation
    AppServiceEnvironmentsOperations.get_inbound_network_dependencies_endpoints
  - Added operation
    AppServiceEnvironmentsOperations.get_outbound_network_dependencies_endpoints
  - Added operation DeletedWebAppsOperations.list_by_location
  - Added operation
    DeletedWebAppsOperations.get_deleted_web_app_by_location

**Breaking changes**

  - Model ManagedServiceIdentity has a new parameter
    user_assigned_identities (renamed from identity_ids)

## 0.41.0 (2019-02-13)

**Features**

  - Model DeletedAppRestoreRequest has a new parameter
    use_dr_secondary
  - Model StackMinorVersion has a new parameter
    is_remote_debugging_enabled
  - Model IpSecurityRestriction has a new parameter subnet_traffic_tag
  - Model IpSecurityRestriction has a new parameter vnet_traffic_tag
  - Model IpSecurityRestriction has a new parameter
    vnet_subnet_resource_id
  - Model DeletedSite has a new parameter geo_region_name
  - Model SnapshotRestoreRequest has a new parameter use_dr_secondary
  - Model SiteAuthSettings has a new parameter
    client_secret_certificate_thumbprint
  - Model SiteConfig has a new parameter
    scm_ip_security_restrictions_use_main
  - Model SiteConfig has a new parameter scm_ip_security_restrictions
  - Model CorsSettings has a new parameter support_credentials
  - Model SiteConfigResource has a new parameter
    scm_ip_security_restrictions_use_main
  - Model SiteConfigResource has a new parameter
    scm_ip_security_restrictions
  - Model StackMajorVersion has a new parameter application_insights
  - Model AppServicePlanPatchResource has a new parameter
    maximum_elastic_worker_count
  - Model AppServicePlan has a new parameter
    maximum_elastic_worker_count
  - Model SitePatchResource has a new parameter geo_distributions
  - Model SitePatchResource has a new parameter
    in_progress_operation_id
  - Model SitePatchResource has a new parameter
    client_cert_exclusion_paths
  - Model SitePatchResource has a new parameter redundancy_mode
  - Model Site has a new parameter geo_distributions
  - Model Site has a new parameter in_progress_operation_id
  - Model Site has a new parameter client_cert_exclusion_paths
  - Model Site has a new parameter redundancy_mode
  - Model VnetInfo has a new parameter is_swift
  - Added operation WebAppsOperations.get_network_traces_slot_v2
  - Added operation
    WebAppsOperations.list_snapshots_from_dr_secondary_slot
  - Added operation WebAppsOperations.get_network_traces_slot
  - Added operation
    WebAppsOperations.start_web_site_network_trace_operation_slot
  - Added operation WebAppsOperations.get_network_trace_operation_v2
  - Added operation
    WebAppsOperations.start_web_site_network_trace_operation
  - Added operation WebAppsOperations.get_network_traces_v2
  - Added operation WebAppsOperations.stop_network_trace_slot
  - Added operation
    WebAppsOperations.get_network_trace_operation_slot_v2
  - Added operation
    WebAppsOperations.list_snapshots_from_dr_secondary
  - Added operation
    WebAppsOperations.get_network_trace_operation_slot
  - Added operation WebAppsOperations.stop_network_trace
  - Added operation WebAppsOperations.start_network_trace_slot
  - Added operation WebAppsOperations.get_network_trace_operation
  - Added operation WebAppsOperations.start_network_trace
  - Added operation WebAppsOperations.get_network_traces
  - Added operation
    RecommendationsOperations.list_recommended_rules_for_hosting_environment
  - Added operation
    RecommendationsOperations.list_history_for_hosting_environment
  - Added operation
    RecommendationsOperations.disable_all_for_hosting_environment
  - Added operation
    RecommendationsOperations.disable_recommendation_for_hosting_environment
  - Added operation
    RecommendationsOperations.reset_all_filters_for_hosting_environment
  - Added operation
    RecommendationsOperations.get_rule_details_by_hosting_environment

**Breaking changes**

  - Model AppServicePlanPatchResource no longer has parameter
    admin_site_name
  - Model AppServicePlan no longer has parameter admin_site_name

## 0.40.0 (2018-08-28)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**General Features**

  - Client class can be used as a context manager to keep the underlying
    HTTP session open for performance

**Features**

  - Model ValidateRequest has a new parameter is_xenon
  - Model SiteConfigResource has a new parameter
    reserved_instance_count
  - Model SiteConfigResource has a new parameter windows_fx_version
  - Model SiteConfigResource has a new parameter
    azure_storage_accounts
  - Model SiteConfigResource has a new parameter
    x_managed_service_identity_id
  - Model SiteConfigResource has a new parameter
    managed_service_identity_id
  - Model SiteConfigResource has a new parameter ftps_state
  - Model TriggeredWebJob has a new parameter web_job_type
  - Model CsmPublishingProfileOptions has a new parameter
    include_disaster_recovery_endpoints
  - Model SitePatchResource has a new parameter hyper_v
  - Model SitePatchResource has a new parameter is_xenon
  - Model StampCapacity has a new parameter is_linux
  - Model User has a new parameter scm_uri
  - Model SiteConfigurationSnapshotInfo has a new parameter snapshot_id
  - Model AppServiceEnvironmentPatchResource has a new parameter
    ssl_cert_key_vault_secret_name
  - Model AppServiceEnvironmentPatchResource has a new parameter
    has_linux_workers
  - Model AppServiceEnvironmentPatchResource has a new parameter
    ssl_cert_key_vault_id
  - Model BackupRequest has a new parameter backup_name
  - Model RecommendationRule has a new parameter id
  - Model RecommendationRule has a new parameter recommendation_name
  - Model RecommendationRule has a new parameter kind
  - Model RecommendationRule has a new parameter type
  - Model RecommendationRule has a new parameter category_tags
  - Model Site has a new parameter hyper_v
  - Model Site has a new parameter is_xenon
  - Model TriggeredJobRun has a new parameter web_job_id
  - Model TriggeredJobRun has a new parameter web_job_name
  - Model CertificateOrderAction has a new parameter action_type
  - Model SiteExtensionInfo has a new parameter
    installer_command_line_params
  - Model SiteExtensionInfo has a new parameter extension_id
  - Model SiteExtensionInfo has a new parameter extension_type
  - Model SiteAuthSettings has a new parameter validate_issuer
  - Model TriggeredJobHistory has a new parameter runs
  - Model ProcessInfo has a new parameter minidump
  - Model ProcessInfo has a new parameter total_cpu_time
  - Model ProcessInfo has a new parameter non_paged_system_memory
  - Model ProcessInfo has a new parameter working_set
  - Model ProcessInfo has a new parameter paged_memory
  - Model ProcessInfo has a new parameter private_memory
  - Model ProcessInfo has a new parameter user_cpu_time
  - Model ProcessInfo has a new parameter deployment_name
  - Model ProcessInfo has a new parameter peak_paged_memory
  - Model ProcessInfo has a new parameter peak_working_set
  - Model ProcessInfo has a new parameter peak_virtual_memory
  - Model ProcessInfo has a new parameter is_webjob
  - Model ProcessInfo has a new parameter privileged_cpu_time
  - Model ProcessInfo has a new parameter identifier
  - Model ProcessInfo has a new parameter paged_system_memory
  - Model ProcessInfo has a new parameter virtual_memory
  - Model ServiceSpecification has a new parameter log_specifications
  - Model ProcessThreadInfo has a new parameter identifier
  - Model ManagedServiceIdentity has a new parameter identity_ids
  - Model AppServicePlan has a new parameter
    free_offer_expiration_time
  - Model AppServicePlan has a new parameter hyper_v
  - Model AppServicePlan has a new parameter is_xenon
  - Model SiteConfig has a new parameter reserved_instance_count
  - Model SiteConfig has a new parameter windows_fx_version
  - Model SiteConfig has a new parameter azure_storage_accounts
  - Model SiteConfig has a new parameter
    x_managed_service_identity_id
  - Model SiteConfig has a new parameter managed_service_identity_id
  - Model SiteConfig has a new parameter ftps_state
  - Model WebJob has a new parameter web_job_type
  - Model Recommendation has a new parameter name
  - Model Recommendation has a new parameter id
  - Model Recommendation has a new parameter kind
  - Model Recommendation has a new parameter enabled
  - Model Recommendation has a new parameter type
  - Model Recommendation has a new parameter states
  - Model Recommendation has a new parameter category_tags
  - Model SlotConfigNamesResource has a new parameter
    azure_storage_config_names
  - Model SlotDifference has a new parameter level
  - Model AppServiceEnvironment has a new parameter
    ssl_cert_key_vault_secret_name
  - Model AppServiceEnvironment has a new parameter has_linux_workers
  - Model AppServiceEnvironment has a new parameter
    ssl_cert_key_vault_id
  - Model ContinuousWebJob has a new parameter web_job_type
  - Model AppServiceEnvironmentResource has a new parameter
    ssl_cert_key_vault_secret_name
  - Model AppServiceEnvironmentResource has a new parameter
    has_linux_workers
  - Model AppServiceEnvironmentResource has a new parameter
    ssl_cert_key_vault_id
  - Model AppServicePlanPatchResource has a new parameter
    free_offer_expiration_time
  - Model AppServicePlanPatchResource has a new parameter hyper_v
  - Model AppServicePlanPatchResource has a new parameter is_xenon
  - Model DeletedSite has a new parameter deleted_site_name
  - Model DeletedSite has a new parameter deleted_site_kind
  - Model DeletedSite has a new parameter kind
  - Model DeletedSite has a new parameter type
  - Model DeletedSite has a new parameter deleted_site_id
  - Added operation WebAppsOperations.put_private_access_vnet
  - Added operation
    WebAppsOperations.create_or_update_swift_virtual_network_connection
  - Added operation WebAppsOperations.update_azure_storage_accounts
  - Added operation WebAppsOperations.update_premier_add_on_slot
  - Added operation WebAppsOperations.get_container_logs_zip_slot
  - Added operation WebAppsOperations.discover_backup_slot
  - Added operation
    WebAppsOperations.update_swift_virtual_network_connection_slot
  - Added operation WebAppsOperations.get_private_access
  - Added operation WebAppsOperations.discover_backup
  - Added operation
    WebAppsOperations.create_or_update_swift_virtual_network_connection_slot
  - Added operation WebAppsOperations.delete_swift_virtual_network
  - Added operation WebAppsOperations.put_private_access_vnet_slot
  - Added operation WebAppsOperations.restore_from_deleted_app
  - Added operation WebAppsOperations.restore_from_backup_blob
  - Added operation
    WebAppsOperations.delete_swift_virtual_network_slot
  - Added operation WebAppsOperations.list_azure_storage_accounts
  - Added operation
    WebAppsOperations.list_azure_storage_accounts_slot
  - Added operation WebAppsOperations.restore_from_backup_blob_slot
  - Added operation
    WebAppsOperations.get_swift_virtual_network_connection
  - Added operation
    WebAppsOperations.get_swift_virtual_network_connection_slot
  - Added operation WebAppsOperations.get_container_logs_zip
  - Added operation WebAppsOperations.restore_snapshot
  - Added operation
    WebAppsOperations.update_swift_virtual_network_connection
  - Added operation WebAppsOperations.restore_snapshot_slot
  - Added operation WebAppsOperations.restore_from_deleted_app_slot
  - Added operation
    WebAppsOperations.update_azure_storage_accounts_slot
  - Added operation WebAppsOperations.get_private_access_slot
  - Added operation WebAppsOperations.update_premier_add_on
  - Added operation AppServiceEnvironmentsOperations.change_vnet
  - Added operation
    DiagnosticsOperations.list_site_detector_responses_slot
  - Added operation
    DiagnosticsOperations.get_site_detector_response_slot
  - Added operation DiagnosticsOperations.get_site_detector_response
  - Added operation
    DiagnosticsOperations.get_hosting_environment_detector_response
  - Added operation
    DiagnosticsOperations.list_site_detector_responses
  - Added operation
    DiagnosticsOperations.list_hosting_environment_detector_responses
  - Added operation
    RecommendationsOperations.disable_recommendation_for_subscription
  - Added operation
    RecommendationsOperations.disable_recommendation_for_site
  - Added operation group ResourceHealthMetadataOperations

**Breaking changes**

  - Operation RecommendationsOperations.get_rule_details_by_web_app
    has a new signature
  - Operation
    WebAppsOperations.list_publishing_profile_xml_with_secrets has
    a new signature
  - Operation
    WebAppsOperations.list_publishing_profile_xml_with_secrets_slot
    has a new signature
  - Operation WebAppsOperations.delete_slot has a new signature
  - Operation WebAppsOperations.delete has a new signature
  - Operation RecommendationsOperations.list_history_for_web_app has
    a new signature
  - Operation WebAppsOperations.update_slot has a new signature
  - Operation WebAppsOperations.create_or_update_slot has a new
    signature
  - Operation WebAppsOperations.create_or_update has a new signature
  - Operation WebAppsOperations.update has a new signature
  - Model TriggeredWebJob no longer has parameter
    triggered_web_job_name
  - Model TriggeredWebJob no longer has parameter job_type
  - Model SitePatchResource no longer has parameter snapshot_info
  - Model User no longer has parameter user_name
  - Model SiteConfigurationSnapshotInfo no longer has parameter
    site_configuration_snapshot_info_id
  - Model BackupRequest no longer has parameter backup_request_name
  - Model BackupRequest no longer has parameter backup_request_type
  - Model ResourceMetricDefinition no longer has parameter
    resource_metric_definition_id
  - Model ResourceMetricDefinition no longer has parameter
    resource_metric_definition_name
  - Model RecommendationRule no longer has parameter tags
  - Model SourceControl no longer has parameter source_control_name
  - Model Site no longer has parameter snapshot_info
  - Model VnetRoute no longer has parameter vnet_route_name
  - Model Certificate no longer has parameter geo_region
  - Model TriggeredJobRun no longer has parameter
    triggered_job_run_id
  - Model TriggeredJobRun no longer has parameter
    triggered_job_run_name
  - Model CertificateOrderAction no longer has parameter
    certificate_order_action_type
  - Model SiteExtensionInfo no longer has parameter
    site_extension_info_id
  - Model SiteExtensionInfo no longer has parameter installation_args
  - Model SiteExtensionInfo no longer has parameter
    site_extension_info_type
  - Model PremierAddOnOffer no longer has parameter
    premier_add_on_offer_name
  - Model TriggeredJobHistory no longer has parameter
    triggered_job_runs
  - Model ProcessInfo no longer has parameter total_processor_time
  - Model ProcessInfo no longer has parameter user_processor_time
  - Model ProcessInfo no longer has parameter
    peak_paged_memory_size64
  - Model ProcessInfo no longer has parameter
    privileged_processor_time
  - Model ProcessInfo no longer has parameter
    paged_system_memory_size64
  - Model ProcessInfo no longer has parameter process_info_name
  - Model ProcessInfo no longer has parameter peak_working_set64
  - Model ProcessInfo no longer has parameter virtual_memory_size64
  - Model ProcessInfo no longer has parameter mini_dump
  - Model ProcessInfo no longer has parameter is_web_job
  - Model ProcessInfo no longer has parameter private_memory_size64
  - Model ProcessInfo no longer has parameter
    nonpaged_system_memory_size64
  - Model ProcessInfo no longer has parameter working_set64
  - Model ProcessInfo no longer has parameter process_info_id
  - Model ProcessInfo no longer has parameter paged_memory_size64
  - Model ProcessInfo no longer has parameter
    peak_virtual_memory_size64
  - Model GeoRegion no longer has parameter geo_region_name
  - Model FunctionEnvelope no longer has parameter
    function_envelope_name
  - Model ProcessThreadInfo no longer has parameter
    process_thread_info_id
  - Model CloningInfo no longer has parameter ignore_quotas
  - Model AppServicePlan no longer has parameter
    app_service_plan_name
  - Model CertificatePatchResource no longer has parameter geo_region
  - Model WebJob no longer has parameter job_type
  - Model WebJob no longer has parameter web_job_name
  - Model Usage no longer has parameter usage_name
  - Model Deployment no longer has parameter deployment_id
  - Model Recommendation no longer has parameter tags
  - Model PremierAddOn no longer has parameter premier_add_on_tags
  - Model PremierAddOn no longer has parameter
    premier_add_on_location
  - Model PremierAddOn no longer has parameter premier_add_on_name
  - Model SlotDifference no longer has parameter slot_difference_type
  - Model ContinuousWebJob no longer has parameter
    continuous_web_job_name
  - Model ContinuousWebJob no longer has parameter job_type
  - Model TopLevelDomain no longer has parameter domain_name
  - Model AppServicePlanPatchResource no longer has parameter
    app_service_plan_patch_resource_name
  - Model MetricDefinition no longer has parameter
    metric_definition_name
  - Model PerfMonSample no longer has parameter core_count
  - Removed operation WebAppsOperations.recover
  - Removed operation WebAppsOperations.recover_slot
  - Removed operation
    WebAppsOperations.get_web_site_container_logs_zip
  - Removed operation
    WebAppsOperations.get_web_site_container_logs_zip_slot
  - Removed operation WebAppsOperations.discover_restore
  - Removed operation WebAppsOperations.discover_restore_slot
  - Model IpSecurityRestriction has a new signature

## 0.35.0 (2018-02-20)

**Breaking changes**

  - Many models signature changed to expose correctly required
    parameters. Example (non exhaustive) list:
      - AppServiceCertificateOrderPatchResource now requires
        product_type
      - AppServicePlanPatchResource now requires
        app_service_plan_patch_resource_name
      - CertificatePatchResource now requires password
      - DomainPatchResource now requires contact_admin,
        contact_billing, contact_registrant, contact_tech, consent
      - MigrateMySqlRequest now requires connection_string,
        migration_type
      - PushSettings now requires is_push_enabled
  - get_available_stacks now returns a pageable object

**Features**

  - Add certificate_registration_provider operations group
  - Add Diagnostics operations group
  - Add domain registration provider operations groups
  - All operations group have now a "models" attribute

## 0.34.1 (2017-10-24)

  - MSI fixes

## 0.34.0 (2017-10-16)

  - Add MSI support

## 0.33.0 (2017-10-04)

**Features**

  - Add providers.list_operations
  - Add verify_hosting_environment_vnet
  - Add web_apps.list_sync_function_triggers
  - Add web_apps.list_processes
  - Add web_apps.get_instance_process_module
  - Add web_apps.delete_process
  - Add web_apps.get_process_dump
  - Add web_apps continous web job operations
  - Add web_apps continous web job slots operations
  - Add web_apps public certificate operations
  - Add web_apps site_extension operations
  - Add web_apps functions operations
  - Add web_apps.list_function_secrets
  - Add web_apps.list_deployment_log
  - Add web_apps.list_deployment_log_slot
  - Add web_apps ms_deploy_status operations
  - Add web_apps ms_deploy_status_slot operations
  - Add web_apps ms_deploy_log_slot operations
  - Add web_apps instance_process_modules operations
  - Add web_apps instance_process_threads operations
  - Add web_apps instance_process_slot operations
  - Add web_apps instance_process_modules_slot operations
  - Add web_apps instance_process_threads_slot operations
  - Add web_apps.list_sync_function_triggers_slot
  - Add web_apps processes_slot operations
  - Add web_apps site_extensions_slot operations
  - Add web_apps triggered_web_jobs_slot operations
  - Add web_apps web_jobs_slot operations
  - Add web_apps triggered_web_jobs operations
  - Add web_apps web_jobs operations
  - Add web_apps.is_cloneable

**Breaking changes**

  - Remove 'name' and 'type' from several models (was ignored by server
    as read-only parameters)
  - Remove completely 'location' parameter from several models (None was
    the only acceptable value)
  - Remove a lot of incorrect parameter into DeletedSite
  - Remove deleted_web_apps.list_by_resource_group
  - Change web_apps.update_application_settings method signature
  - Change web_apps.update_connection_strings method signature
  - Change web_apps.update_metadata method signature
  - web_apps.recover now recover from a delete app to a previous
    snapshot
  - web_apps.recover_slot now recover from a delete app to a previous
    snapshot

## 0.32.0 (2017-04-26)

  - Support list web runtime stacks
  - Expose non resource based model type for SiteConfig,
    SiteAuthSettings, etc, to be used as property
  - Support list linux web available regions

## 0.31.1 (2017-04-20)

This wheel package is now built with the azure wheel extension

## 0.31.0 (2017-02-13)

  - Major refactoring and breaking changes
  - New API Version

## 0.30.0 (2016-10-17)

  - Initial release
