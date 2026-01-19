## tsp migration

### Breaking Changes

- Model `PrometheusRuleGroupResource` moved instance variable `description`, `enabled`, `cluster_name`, `scopes`, `interval` and `rules` under property `properties`
- Model `PrometheusRuleGroupResourcePatchParameters` moved instance variable `enabled` under property `properties`

### Other Changes

  - Deleted model `PrometheusRuleGroupResourceCollection` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2026-01-19)

### Other Changes

  - Initial version