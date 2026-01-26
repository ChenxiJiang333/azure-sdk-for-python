## tsp migration

### Breaking Changes

- Model `Extension` moved instance variable `extension_type`, `auto_upgrade_minor_version`, `release_train`, `version`, `scope`, `configuration_settings`, `configuration_protected_settings`, `current_version`, `provisioning_state`, `statuses`, `error_info`, `custom_location_settings`, `package_uri`, `aks_assigned_identity` and `is_system_extension` under property `properties`
- Model `PatchExtension` moved instance variable `auto_upgrade_minor_version`, `release_train`, `version`, `configuration_settings` and `configuration_protected_settings` under property `properties`
- Method `ExtensionsOperations.begin_delete` changed its parameter `force_delete` from `positional_or_keyword` to `keyword_only`

### Other Changes

  - Deleted model `ExtensionsList` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
