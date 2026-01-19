## tsp migration

### Breaking Changes

- Model `TenantActivityLogAlertResource` moved instance variable `tenant_scope`, `scopes`, `condition`, `actions`, `enabled` and `description` under property `properties`
- Model `TenantAlertRulePatchObject` moved instance variable `enabled` under property `properties`

### Other Changes

  - Deleted model `TenantAlertRuleList`/`AzureResource` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2026-01-19)

### Other Changes

  - Initial version