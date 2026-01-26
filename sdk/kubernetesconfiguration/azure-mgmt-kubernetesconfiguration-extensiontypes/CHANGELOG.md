## tsp migration

### Breaking Changes

- Model `ClusterScopeSettings` moved instance variable `allow_multiple_instances` and `default_release_namespace` under property `properties`
- Method `ExtensionTypesOperations.cluster_list_versions` changed its parameter `release_train`/`major_version`/`show_latest` from `positional_or_keyword` to `keyword_only`
- Method `ExtensionTypesOperations.list` changed its parameter `publisher_id`/`offer_id`/`plan_id`/`release_train` from `positional_or_keyword` to `keyword_only`
- Method `ExtensionTypesOperations.list_versions` changed its parameter `release_train`/`cluster_type`/`major_version`/`show_latest` from `positional_or_keyword` to `keyword_only`
- Method `ExtensionTypesOperations.location_list` changed its parameter `publisher_id`/`offer_id`/`plan_id`/`release_train`/`cluster_type` from `positional_or_keyword` to `keyword_only`

### Other Changes

  - Deleted model `ExtensionTypeVersionsList`/`ExtensionTypesList` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
