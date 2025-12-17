# Release History

## tsp migration

### Breaking Changes

  - Deleted or renamed client `PolicyClient`
  - Model `ErrorResponse` moved instance variable `code`, `message`, `target`, `details` and `additional_info` under property `error`
  - Model `PolicyAssignment` moved instance variable `display_name`, `policy_definition_id`, `definition_version`, `latest_definition_version`, `effective_definition_version`, `scope`, `not_scopes`, `parameters`, `description`, `metadata`, `enforcement_mode`, `non_compliance_messages`, `resource_selectors` and `overrides` under property `properties`
  - Model `PolicyAssignmentUpdate` moved instance variable `resource_selectors` and `overrides` under property `properties`
  - Model `PolicyDefinition` moved instance variable `policy_type`, `mode`, `display_name`, `description`, `policy_rule`, `metadata`, `parameters`, `version` and `versions` under property `properties`
  - Model `PolicyDefinitionVersion` moved instance variable `policy_type`, `mode`, `display_name`, `description`, `policy_rule`, `metadata`, `parameters` and `version` under property `properties`
  - Model `PolicySetDefinition` moved instance variable `policy_type`, `display_name`, `description`, `metadata`, `parameters`, `policy_definitions`, `policy_definition_groups`, `version` and `versions` under property `properties`
  - Model `PolicySetDefinitionVersion` moved instance variable `policy_type`, `display_name`, `description`, `metadata`, `parameters`, `policy_definitions`, `policy_definition_groups` and `version` under property `properties`
  - Deleted or renamed model `Alias`
  - Deleted or renamed model `AliasPath`
  - Deleted or renamed model `AliasPathAttributes`
  - Deleted or renamed model `AliasPathMetadata`
  - Deleted or renamed model `AliasPathTokenType`
  - Deleted or renamed model `AliasPattern`
  - Deleted or renamed model `AliasPatternType`
  - Deleted or renamed model `AliasType`
  - Deleted or renamed model `AssignmentScopeValidation`
  - Deleted or renamed model `DataEffect`
  - Deleted or renamed model `DataManifestCustomResourceFunctionDefinition`
  - Deleted or renamed model `DataPolicyManifest`
  - Deleted or renamed model `ExemptionCategory`
  - Deleted or renamed model `PolicyExemption`
  - Deleted or renamed model `PolicyExemptionUpdate`
  - Deleted or renamed model `PolicyVariableColumn`
  - Deleted or renamed model `PolicyVariableValueColumnValue`
  - Deleted or renamed model `ResourceTypeAliases`
  - Deleted or renamed model `Variable`
  - Deleted or renamed model `VariableValue`
  - Method `PolicyAssignmentsOperations.get` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_management_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_resource` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Method `PolicyAssignmentsOperations.list_for_resource_group` changed its parameter `expand` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed method `PolicyAssignmentsOperations.create_by_id`
  - Deleted or renamed method `PolicyAssignmentsOperations.delete_by_id`
  - Deleted or renamed method `PolicyAssignmentsOperations.get_by_id`
  - Deleted or renamed method `PolicyAssignmentsOperations.update_by_id`
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
  - Deleted or renamed model `DataPolicyManifestsOperations`
  - Deleted or renamed model `PolicyExemptionsOperations`
  - Deleted or renamed model `VariableValuesOperations`
  - Deleted or renamed model `VariablesOperations`

## 1.0.0b1 (2025-12-17)

### Other Changes

  - Initial version