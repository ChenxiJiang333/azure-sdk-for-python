## tsp migration

### Breaking Changes

- Model `FluxConfiguration` moved instance variable `scope`, `namespace`, `source_kind`, `suspend`, `git_repository`, `bucket`, `azure_blob`, `oci_repository`, `kustomizations`, `configuration_protected_settings`, `statuses`, `repository_public_key`, `source_synced_commit_id`, `source_updated_at`, `status_updated_at`, `wait_for_reconciliation`, `reconciliation_wait_duration`, `compliance_state`, `provisioning_state` and `error_message` under property `properties`
- Model `FluxConfigurationPatch` moved instance variable `source_kind`, `suspend`, `git_repository`, `bucket`, `azure_blob`, `oci_repository`, `kustomizations` and `configuration_protected_settings` under property `properties`
- Method `FluxConfigurationsOperations.begin_delete` changed its parameter `force_delete` from `positional_or_keyword` to `keyword_only`

### Other Changes

  - Deleted model `FluxConfigurationsList`/`KustomizationValidationType` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
