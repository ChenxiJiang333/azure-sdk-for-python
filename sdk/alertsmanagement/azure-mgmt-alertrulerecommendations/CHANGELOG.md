## tsp migration

### Breaking Changes

  - Model `AlertRuleRecommendationResource` moved instance variable `alert_rule_type`, `category`, `display_information` and `rule_arm_template` under property `properties`
  - Method `AlertRuleRecommendationsOperations.list_by_target_type` changed its parameter `target_type` from `positional_or_keyword` to `keyword_only`

### Other Changes

  - Deleted model `AlertRuleRecommendationsListResponse` which actually were not used by SDK users

# Release History

## 1.0.0b1 (2026-01-19)

### Other Changes

  - Initial version