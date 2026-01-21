## tsp migration

### Breaking Changes

- Model `LogAlertRuleDimension` deleted or renamed its instance variable `values`
- Model `LogAlertRuleResource` moved instance variable `description`, `display_name`, `severity`, `enabled`, `scopes`, `evaluation_frequency`, `window_size`, `override_query_time_range`, `target_resource_types` and `criteria` under property `properties`
- Deleted or renamed module `['azure.mgmt.previewalertrule.aio.operations', 'azure.mgmt.previewalertrule.operations']`

# Release History

## 1.0.0b1 (2026-01-21)

### Other Changes

  - Initial version