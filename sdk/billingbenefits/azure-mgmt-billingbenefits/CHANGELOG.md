# Release History

## tsp migration

### Breaing Changes

  - Deleted or renamed model `BillingBenefitsRP`
  - Deleted or renamed enum value `BillingPlan.P1_M`
  - Model `PurchaseRequest` moved instance variable `display_name`/`billing_scope_id`/`term`/`billing_plan`/`applied_scope_type`/`commitment`/`effective_date_time`/`renew`/`applied_scope_properties` under property `properties`
  - Model `ReservationOrderAliasRequest` moved instance variable `display_name`/`billing_scope_id`/`term`/`billing_plan`/`applied_scope_type`/`applied_scope_properties`/`quantity`/`renew`/`reserved_resource_type`/`review_date_time`/`reserved_resource_properties` under property `properties`
  - Model `ReservationOrderAliasResponse` moved instance variable `display_name`/`reservation_order_id`/`provisioning_state`/`billing_scope_id`/`term`/`billing_plan`/`applied_scope_type`/`applied_scope_properties`/`quantity`/`renew`/`reserved_resource_type`/`review_date_time`/`reserved_resource_properties` under property `properties`
  - Model `RoleAssignmentEntity` moved instance variable `principal_id`/`role_definition_id`/`scope` under property `properties`
  - Model `SavingsPlanModel` moved instance variable `display_name`/`provisioning_state`/`display_provisioning_state`/`billing_scope_id`/`billing_profile_id`/`customer_id`/`billing_account_id`/`term`/`billing_plan`/`applied_scope_type`/`user_friendly_applied_scope_type`/`applied_scope_properties`/`commitment`/`effective_date_time`/`expiry_date_time`/`purchase_date_time`/`benefit_start_time`/`extended_status_info`/`renew`/`utilization`/`renew_source`/`renew_destination`/`renew_properties` under property `properties`
  - Model `SavingsPlanOrderAliasModel` moved instance variable `display_name`/`savings_plan_order_id`/`provisioning_state`/`billing_scope_id`/`term`/`billing_plan`/`applied_scope_type`/`applied_scope_properties`/`commitment` under property `properties`
  - Model `SavingsPlanOrderModel` moved instance variable `display_name`/`provisioning_state`/`billing_scope_id`/`billing_profile_id`/`customer_id`/`billing_account_id`/`term`/`billing_plan`/`expiry_date_time`/`benefit_start_time`/`plan_information`/`savings_plans`/`extended_status_info` under property `properties`
  - Deleted or renamed enum value `Term.P1_Y`
  - Deleted or renamed enum value `Term.P3_Y`
  - Deleted or renamed enum value `Term.P5_Y`
  - Deleted or renamed model `BillingInformation`
  - Deleted or renamed model `OperationResultError`
  - Deleted or renamed model `PricingCurrencyDuration`
  - Deleted or renamed model `PricingCurrencyTotal`
  - Deleted model `SavingsPlanModelList`/`SavingsPlanOrderModelList` which actually were not used by SDK users
  - Deleted or renamed model `SavingsPlanPurchaseValidateRequest`
  - Method `SavingsPlanOperations.list_all` changed its parameter `orderby`/`refresh_summary`/`skiptoken`/`selected_state`/`take` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed method `SavingsPlanOperations.update`
  - Deleted or renamed model `BillingBenefitsRPOperationsMixin`

## 1.0.0b2 (2025-12-17)

### Features Added

  - Enum `CommitmentGrain` added member `FULL_TERM`
  - Enum `CommitmentGrain` added member `UNKNOWN`
  - Model `SavingsPlanOrderAliasModel` added property `properties`
  - Model `Sku` added property `tier`
  - Model `Sku` added property `size`
  - Model `Sku` added property `family`
  - Model `Sku` added property `capacity`
  - Added model `ApplicableMacc`
  - Added enum `ApplyDiscountOn`
  - Added model `ArmManagedServiceIdentity`
  - Added model `AutomaticShortfallSuppressReason`
  - Added model `Award`
  - Added enum `BenefitType`
  - Added model `BenefitValidateModel`
  - Added model `BenefitValidateRequest`
  - Added model `BenefitValidateResponse`
  - Added model `BenefitValidateResponseProperty`
  - Added model `CatalogClaimsItem`
  - Added model `ChargeShortfallRequest`
  - Added model `ConditionalCredit`
  - Added model `ConditionalCreditContributor`
  - Added enum `ConditionalCreditEntityType`
  - Added model `ConditionalCreditMilestone`
  - Added model `ConditionalCreditMilestoneBase`
  - Added model `ConditionalCreditPatchRequest`
  - Added model `ConditionalCreditPatchRequestProperties`
  - Added model `ConditionalCreditProperties`
  - Added enum `ConditionalCreditStatus`
  - Added enum `ConditionalCreditsProvisioningState`
  - Added model `ConditionalCreditsValidateModel`
  - Added model `ConditionsItem`
  - Added model `Contributor`
  - Added model `ContributorConditionalCreditMilestone`
  - Added model `ContributorConditionalCreditProperties`
  - Added model `Credit`
  - Added model `CreditBreakdownItem`
  - Added model `CreditDimension`
  - Added enum `CreditExpirationPolicy`
  - Added model `CreditPatchProperties`
  - Added model `CreditPatchRequest`
  - Added model `CreditPolicies`
  - Added model `CreditProperties`
  - Added model `CreditReason`
  - Added enum `CreditRedemptionPolicy`
  - Added model `CreditSource`
  - Added model `CreditSourcePatchRequest`
  - Added model `CreditSourceProperties`
  - Added enum `CreditStatus`
  - Added model `CreditsValidateModel`
  - Added model `CustomPriceProperties`
  - Added model `Discount`
  - Added enum `DiscountAppliedScopeType`
  - Added enum `DiscountCombinationRule`
  - Added enum `DiscountEntityType`
  - Added model `DiscountPatchRequest`
  - Added model `DiscountPatchRequestProperties`
  - Added model `DiscountProperties`
  - Added enum `DiscountProvisioningState`
  - Added enum `DiscountRuleType`
  - Added enum `DiscountStatus`
  - Added enum `DiscountType`
  - Added model `DiscountTypeCustomPrice`
  - Added model `DiscountTypeCustomPriceMultiCurrency`
  - Added model `DiscountTypeProduct`
  - Added model `DiscountTypeProductFamily`
  - Added model `DiscountTypeProductSku`
  - Added model `DiscountTypeProperties`
  - Added enum `EnablementMode`
  - Added model `EntityTypeAffiliateDiscount`
  - Added model `EntityTypePrimaryDiscount`
  - Added model `Macc`
  - Added enum `MaccEntityType`
  - Added model `MaccMilestone`
  - Added enum `MaccMilestoneStatus`
  - Added model `MaccModelProperties`
  - Added model `MaccPatchRequest`
  - Added model `MaccPatchRequestProperties`
  - Added enum `MaccStatus`
  - Added model `MaccValidateModel`
  - Added model `ManagedServiceIdentity`
  - Added enum `ManagedServiceIdentityType`
  - Added model `MarketSetPricesItems`
  - Added enum `MilestoneStatus`
  - Added model `Plan`
  - Added model `PriceGuaranteeProperties`
  - Added enum `PricingPolicy`
  - Added model `PrimaryConditionalCreditProperties`
  - Added model `ProxyResource`
  - Added model `ResourceSku`
  - Added model `SavingsPlanOrderAliasProperties`
  - Added model `SavingsPlanValidateModel`
  - Added model `SellerResourceListRequest`
  - Added model `SellerResourceListRequestProperties`
  - Added model `Shortfall`
  - Added enum `SkuTier`
  - Added model `TrackedResource`
  - Added model `UserAssignedIdentity`
  - Model `SavingsPlanOperations` added method `begin_update`
  - Added model `ApplicableMaccsOperations`
  - Added model `BenefitOperations`
  - Added model `ConditionalCreditContributorsOperationGroupOperations`
  - Added model `ConditionalCreditContributorsOperations`
  - Added model `ConditionalCreditsOperationGroupOperations`
  - Added model `ConditionalCreditsOperations`
  - Added model `ContributorsOperationGroupOperations`
  - Added model `ContributorsOperations`
  - Added model `CreditsOperationGroupOperations`
  - Added model `CreditsOperations`
  - Added model `DiscountOperations`
  - Added model `DiscountsOperations`
  - Added model `MaccsOperations`
  - Added model `SellerResourceOperations`
  - Added model `SourcesOperations`

### Breaking Changes

  - Deleted or renamed model `BillingBenefitsRP`
  - Deleted or renamed enum value `BillingPlan.P1_M`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `display_name`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `savings_plan_order_id`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `provisioning_state`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `billing_scope_id`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `term`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `billing_plan`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `applied_scope_type`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `applied_scope_properties`
  - Model `SavingsPlanOrderAliasModel` deleted or renamed its instance variable `commitment`
  - Deleted or renamed enum value `Term.P1_Y`
  - Deleted or renamed enum value `Term.P3_Y`
  - Deleted or renamed enum value `Term.P5_Y`
  - Deleted or renamed model `BillingInformation`
  - Deleted or renamed model `OperationResultError`
  - Deleted or renamed model `PricingCurrencyDuration`
  - Deleted or renamed model `PricingCurrencyTotal`
  - Deleted or renamed model `SavingsPlanModelList`
  - Deleted or renamed model `SavingsPlanOrderModelList`
  - Deleted or renamed model `SavingsPlanPurchaseValidateRequest`
  - Method `SavingsPlanOperations.list_all` changed its parameter `orderby` from `positional_or_keyword` to `keyword_only`
  - Method `SavingsPlanOperations.list_all` changed its parameter `refresh_summary` from `positional_or_keyword` to `keyword_only`
  - Method `SavingsPlanOperations.list_all` changed its parameter `skiptoken` from `positional_or_keyword` to `keyword_only`
  - Method `SavingsPlanOperations.list_all` changed its parameter `selected_state` from `positional_or_keyword` to `keyword_only`
  - Method `SavingsPlanOperations.list_all` changed its parameter `take` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed method `SavingsPlanOperations.update`
  - Deleted or renamed model `BillingBenefitsRPOperationsMixin`

## 1.0.0b1 (2022-12-14)

* Initial Release
