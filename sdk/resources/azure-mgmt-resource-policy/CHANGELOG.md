# Release History

## tsp migration

### Breaking Changes

  - Renamed client name `PolicyClient` to `PolicyMgmtClient`
  - Model `PolicyAssignment` moved instance variable `display_name`, `policy_definition_id`, `definition_version`, `latest_definition_version`, `effective_definition_version`, `scope`, `not_scopes`, `parameters`, `description`, `metadata`, `enforcement_mode`, `non_compliance_messages`, `resource_selectors`, `overrides`, `assignment_type` and `instance_id` under property `properties`
  - Model `PolicyAssignmentUpdate` moved instance variable `resource_selectors` and `overrides` under property `properties`
  - Model `PolicyDefinition` moved instance variable `policy_type`, `mode`, `display_name`, `description`, `policy_rule`, `metadata`, `parameters`, `version`, `versions` and `external_evaluation_enforcement_settings` under property `properties`
  - Model `PolicyDefinitionVersion` moved instance variable `policy_type`, `mode`, `display_name`, `description`, `policy_rule`, `metadata`, `parameters`, `version` and `external_evaluation_enforcement_settings` under property `properties`
  - Model `PolicySetDefinition` moved instance variable `policy_type`, `display_name`, `description`, `metadata`, `parameters`, `policy_definitions`, `policy_definition_groups`, `version` and `versions` under property `properties`
  - Model `PolicySetDefinitionVersion` moved instance variable `policy_type`, `display_name`, `description`, `metadata`, `parameters`, `policy_definitions`, `policy_definition_groups` and `version` under property `properties`
  - Method `PolicyAssignmentsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_resource` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_resource_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.get_at_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.get_built_in` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.list_built_in` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionVersionsOperations.list_by_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.get_at_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.get_built_in` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.list_built_in` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicySetDefinitionsOperations.list_by_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`

## 1.0.0b1 (2025-12-17)

### Other Changes

  - Initial version