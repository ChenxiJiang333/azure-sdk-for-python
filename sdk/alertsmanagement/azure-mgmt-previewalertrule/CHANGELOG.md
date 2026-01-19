## tsp migration

### Breaking Changes

- Deleted or renamed client `PreviewAlertRuleClient`
- Deleted or renamed enum value `AlertSeverity.FOUR`
- Deleted or renamed enum value `AlertSeverity.ONE`
- Deleted or renamed enum value `AlertSeverity.THREE`
- Deleted or renamed enum value `AlertSeverity.TWO`
- Deleted or renamed enum value `AlertSeverity.ZERO`
- Deleted or renamed enum value `AlertSeverity.fromhex`
- Deleted or renamed enum value `AlertSeverity.hex`
- Model `LogAlertRuleDimension` renamed its instance variable `values` to `values_property`
- Model `LogAlertRuleResource` moved instance variable `description`, `display_name`, `severity`, `enabled`, `scopes`, `evaluation_frequency`, `window_size`, `override_query_time_range`, `target_resource_types` and `criteria` under property `properties`
- Renamed module `['azure.mgmt.previewalertrule.aio.operations', 'azure.mgmt.previewalertrule.operations']` to `['azure.mgmt.previewalertrule.aio._operations', 'azure.mgmt.previewalertrule._operations']`

# Release History

## 1.0.0b1 (2026-01-19)

### Other Changes

  - Initial version