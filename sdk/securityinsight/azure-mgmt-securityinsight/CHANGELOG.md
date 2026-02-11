# Release History

## 2.0.0b3 (2026-02-11)

change log generation failed!!! You need to write it manually!!!

## 2.0.0b3 (2026-02-11)

### Features Added

  - Added operation EntitiesOperations.run_playbook
  - Added operation UpdateOperations.recommendation
  - Added operation group AlertRuleOperations
  - Added operation group BillingStatisticsOperations
  - Added operation group ContentPackageOperations
  - Added operation group ContentPackagesOperations
  - Added operation group ContentTemplateOperations
  - Added operation group ContentTemplatesOperations
  - Added operation group DataConnectorDefinitionsOperations
  - Added operation group GetTriggeredAnalyticsRuleRunsOperations
  - Added operation group HuntCommentsOperations
  - Added operation group HuntRelationsOperations
  - Added operation group HuntsOperations
  - Added operation group ProductPackageOperations
  - Added operation group ProductPackagesOperations
  - Added operation group ProductTemplateOperations
  - Added operation group ProductTemplatesOperations
  - Added operation group ReevaluateOperations
  - Added operation group ThreatIntelligenceOperations
  - Added operation group TriggeredAnalyticsRuleRunOperations
  - Added operation group WorkspaceManagerAssignmentJobsOperations
  - Added operation group WorkspaceManagerAssignmentsOperations
  - Added operation group WorkspaceManagerConfigurationsOperations
  - Added operation group WorkspaceManagerGroupsOperations
  - Added operation group WorkspaceManagerMembersOperations
  - Model ActivityEntityQueryTemplate has a new parameter etag
  - Model EnrichmentIpGeodata has a new parameter city_confidence_factor
  - Model EnrichmentIpGeodata has a new parameter country_confidence_factor
  - Model EnrichmentIpGeodata has a new parameter state_confidence_factor
  - Model EntityQueryTemplate has a new parameter etag
  - Model FusionAlertRule has a new parameter sub_techniques
  - Model FusionAlertRuleTemplate has a new parameter sub_techniques
  - Model GetQueriesResponse has a new parameter next_link
  - Model IncidentAdditionalData has a new parameter merged_incident_number
  - Model IncidentAdditionalData has a new parameter merged_incident_url
  - Model MLBehaviorAnalyticsAlertRule has a new parameter sub_techniques
  - Model MTPDataConnector has a new parameter filtered_providers
  - Model MTPDataConnectorDataTypes has a new parameter alerts
  - Model MTPDataConnectorProperties has a new parameter filtered_providers
  - Model NrtAlertRule has a new parameter sub_techniques
  - Model Recommendation has a new parameter creation_time_utc
  - Model Recommendation has a new parameter etag
  - Model Recommendation has a new parameter last_modified_time_utc
  - Model Recommendation has a new parameter name
  - Model Recommendation has a new parameter suggestions
  - Model Recommendation has a new parameter system_data
  - Model Recommendation has a new parameter type
  - Model RecommendationList has a new parameter next_link
  - Model RecommendationPatch has a new parameter properties
  - Model Repo has a new parameter installation_id
  - Model ScheduledAlertRule has a new parameter sub_techniques
  - Model ScheduledAlertRuleProperties has a new parameter sub_techniques
  - Model ScheduledAlertRuleTemplate has a new parameter sub_techniques
  - Model SettingList has a new parameter next_link
  - Model SourceControl has a new parameter pull_request
  - Model SourceControl has a new parameter repository_access
  - Model SourceControl has a new parameter service_principal
  - Model SourceControl has a new parameter workload_identity_federation
  - Model ThreatIntelligenceAlertRule has a new parameter sub_techniques
  - Model Watchlist has a new parameter provisioning_state

### Breaking Changes

  - Model EnrichmentIpGeodata no longer has parameter city_cf
  - Model EnrichmentIpGeodata no longer has parameter country_cf
  - Model EnrichmentIpGeodata no longer has parameter state_cf
  - Model IoTDeviceEntity no longer has parameter device_sub_type
  - Model IoTDeviceEntity no longer has parameter importance
  - Model IoTDeviceEntity no longer has parameter is_authorized
  - Model IoTDeviceEntity no longer has parameter is_programming
  - Model IoTDeviceEntity no longer has parameter is_scanner
  - Model IoTDeviceEntity no longer has parameter nic_entity_ids
  - Model IoTDeviceEntity no longer has parameter owners
  - Model IoTDeviceEntity no longer has parameter purdue_layer
  - Model IoTDeviceEntity no longer has parameter sensor
  - Model IoTDeviceEntity no longer has parameter site
  - Model IoTDeviceEntity no longer has parameter zone
  - Model IoTDeviceEntityProperties no longer has parameter device_sub_type
  - Model IoTDeviceEntityProperties no longer has parameter importance
  - Model IoTDeviceEntityProperties no longer has parameter is_authorized
  - Model IoTDeviceEntityProperties no longer has parameter is_programming
  - Model IoTDeviceEntityProperties no longer has parameter is_scanner
  - Model IoTDeviceEntityProperties no longer has parameter nic_entity_ids
  - Model IoTDeviceEntityProperties no longer has parameter owners
  - Model IoTDeviceEntityProperties no longer has parameter purdue_layer
  - Model IoTDeviceEntityProperties no longer has parameter sensor
  - Model IoTDeviceEntityProperties no longer has parameter site
  - Model IoTDeviceEntityProperties no longer has parameter zone
  - Model MSTIDataConnectorDataTypes no longer has parameter bing_safety_phishing_url
  - Model Recommendation no longer has parameter actions
  - Model Recommendation no longer has parameter category
  - Model Recommendation no longer has parameter content
  - Model Recommendation no longer has parameter context
  - Model Recommendation no longer has parameter display_until_time_utc
  - Model Recommendation no longer has parameter hide_until_time_utc
  - Model Recommendation no longer has parameter instructions
  - Model Recommendation no longer has parameter priority
  - Model Recommendation no longer has parameter recommendation_type_title
  - Model Recommendation no longer has parameter visible
  - Model Recommendation no longer has parameter workspace_id
  - Model RecommendationPatch no longer has parameter hide_until_time_utc
  - Model RecommendationPatch no longer has parameter state
  - Model Repository no longer has parameter path_mapping
  - Operation SourceControlOperations.list_repositories has a new required parameter repository_access
  - Operation SourceControlOperations.list_repositories no longer has parameter repo_type
  - Operation SourceControlsOperations.delete has a new required parameter repository_access
  - Parameter branch of model Repository is now required
  - Parameter content_types of model SourceControl is now required
  - Parameter display_name of model SourceControl is now required
  - Parameter logic_app_resource_id of model PlaybookActionProperties is now required
  - Parameter repo_type of model SourceControl is now required
  - Parameter repository of model SourceControl is now required
  - Parameter url of model Repository is now required
  - Parameter value of model AutomationRulesList is now required
  - Parameter value of model IncidentTaskList is now required
  - Parameter value of model RecommendationList is now required
  - Removed operation IncidentsOperations.create_team
  - Removed operation UpdateOperations.begin_recommendation
  - Removed operation group DomainWhoisOperations
  - Removed operation group IPGeodataOperations
  - Renamed operation WatchlistsOperations.create_or_update to WatchlistsOperations.begin_create_or_update
  - Renamed operation WatchlistsOperations.delete to WatchlistsOperations.begin_delete

## 2.0.0b2 (2022-12-27)

### Features Added

  - Added operation group GetOperations
  - Added operation group GetRecommendationsOperations
  - Added operation group IncidentTasksOperations
  - Added operation group UpdateOperations
  - Model AlertDetailsOverride has a new parameter alert_dynamic_properties
  - Model NrtAlertRule has a new parameter sentinel_entities_mappings
  - Model NrtAlertRuleTemplate has a new parameter sentinel_entities_mappings
  - Model NrtAlertRuleTemplateProperties has a new parameter sentinel_entities_mappings
  - Model QueryBasedAlertRuleTemplateProperties has a new parameter sentinel_entities_mappings
  - Model ScheduledAlertRule has a new parameter sentinel_entities_mappings
  - Model ScheduledAlertRuleCommonProperties has a new parameter sentinel_entities_mappings
  - Model ScheduledAlertRuleProperties has a new parameter sentinel_entities_mappings
  - Model ScheduledAlertRuleTemplate has a new parameter sentinel_entities_mappings
  - Model SecurityAlertTimelineItem has a new parameter intent
  - Model SecurityAlertTimelineItem has a new parameter techniques

## 2.0.0b1 (2022-09-29)

### Features Added

  - Added operation DataConnectorsOperations.connect
  - Added operation DataConnectorsOperations.disconnect
  - Added operation IncidentsOperations.create_team
  - Added operation IncidentsOperations.run_playbook
  - Added operation group BookmarkOperations
  - Added operation group BookmarkRelationsOperations
  - Added operation group DataConnectorsCheckRequirementsOperations
  - Added operation group DomainWhoisOperations
  - Added operation group EntitiesGetTimelineOperations
  - Added operation group EntitiesOperations
  - Added operation group EntitiesRelationsOperations
  - Added operation group EntityQueriesOperations
  - Added operation group EntityQueryTemplatesOperations
  - Added operation group EntityRelationsOperations
  - Added operation group FileImportsOperations
  - Added operation group IPGeodataOperations
  - Added operation group MetadataOperations
  - Added operation group OfficeConsentsOperations
  - Added operation group ProductSettingsOperations
  - Added operation group SecurityMLAnalyticsSettingsOperations
  - Added operation group SourceControlOperations
  - Added operation group SourceControlsOperations
  - Model Bookmark has a new parameter entity_mappings
  - Model Bookmark has a new parameter tactics
  - Model Bookmark has a new parameter techniques
  - Model FusionAlertRule has a new parameter scenario_exclusion_patterns
  - Model FusionAlertRule has a new parameter source_settings
  - Model FusionAlertRule has a new parameter techniques
  - Model FusionAlertRuleTemplate has a new parameter source_settings
  - Model FusionAlertRuleTemplate has a new parameter techniques
  - Model Incident has a new parameter provider_incident_id
  - Model Incident has a new parameter provider_name
  - Model Incident has a new parameter team_information
  - Model IncidentAdditionalData has a new parameter provider_incident_url
  - Model IncidentAdditionalData has a new parameter techniques
  - Model IncidentOwnerInfo has a new parameter owner_type
  - Model IoTDeviceEntity has a new parameter device_sub_type
  - Model IoTDeviceEntity has a new parameter importance
  - Model IoTDeviceEntity has a new parameter is_authorized
  - Model IoTDeviceEntity has a new parameter is_programming
  - Model IoTDeviceEntity has a new parameter is_scanner
  - Model IoTDeviceEntity has a new parameter nic_entity_ids
  - Model IoTDeviceEntity has a new parameter owners
  - Model IoTDeviceEntity has a new parameter purdue_layer
  - Model IoTDeviceEntity has a new parameter sensor
  - Model IoTDeviceEntity has a new parameter site
  - Model IoTDeviceEntity has a new parameter zone
  - Model IoTDeviceEntityProperties has a new parameter device_sub_type
  - Model IoTDeviceEntityProperties has a new parameter importance
  - Model IoTDeviceEntityProperties has a new parameter is_authorized
  - Model IoTDeviceEntityProperties has a new parameter is_programming
  - Model IoTDeviceEntityProperties has a new parameter is_scanner
  - Model IoTDeviceEntityProperties has a new parameter nic_entity_ids
  - Model IoTDeviceEntityProperties has a new parameter owners
  - Model IoTDeviceEntityProperties has a new parameter purdue_layer
  - Model IoTDeviceEntityProperties has a new parameter sensor
  - Model IoTDeviceEntityProperties has a new parameter site
  - Model IoTDeviceEntityProperties has a new parameter zone
  - Model ScheduledAlertRule has a new parameter techniques
  - Model ScheduledAlertRuleProperties has a new parameter techniques
  - Model ScheduledAlertRuleTemplate has a new parameter techniques
  - Model Watchlist has a new parameter source_type

### Breaking Changes

  - Parameter alerts of model AlertsDataTypeOfDataConnector is now required
  - Parameter alerts of model MCASDataConnectorDataTypes is now required
  - Parameter exchange of model OfficeDataConnectorDataTypes is now required
  - Parameter indicators of model TIDataConnectorDataTypes is now required
  - Parameter logs of model AwsCloudTrailDataConnectorDataTypes is now required
  - Parameter share_point of model OfficeDataConnectorDataTypes is now required
  - Parameter state of model AwsCloudTrailDataConnectorDataTypesLogs is now required
  - Parameter state of model DataConnectorDataTypeCommon is now required
  - Parameter state of model OfficeDataConnectorDataTypesExchange is now required
  - Parameter state of model OfficeDataConnectorDataTypesSharePoint is now required
  - Parameter state of model OfficeDataConnectorDataTypesTeams is now required
  - Parameter state of model TIDataConnectorDataTypesIndicators is now required
  - Parameter teams of model OfficeDataConnectorDataTypes is now required
  - Parameter tenant_id of model DataConnectorTenantId is now required

## 1.0.0 (2022-07-26)

**Breaking changes**

  - Model Bookmark no longer has parameter entity_mappings
  - Model Bookmark no longer has parameter tactics
  - Model Bookmark no longer has parameter techniques
  - Model FusionAlertRule no longer has parameter scenario_exclusion_patterns
  - Model FusionAlertRule no longer has parameter source_settings
  - Model FusionAlertRule no longer has parameter techniques
  - Model FusionAlertRuleTemplate no longer has parameter source_settings
  - Model FusionAlertRuleTemplate no longer has parameter techniques
  - Model Incident no longer has parameter provider_incident_id
  - Model Incident no longer has parameter provider_name
  - Model Incident no longer has parameter team_information
  - Model IncidentAdditionalData no longer has parameter provider_incident_url
  - Model IncidentAdditionalData no longer has parameter techniques
  - Model IncidentOwnerInfo no longer has parameter owner_type
  - Model ScheduledAlertRule no longer has parameter techniques
  - Model ScheduledAlertRuleProperties no longer has parameter techniques
  - Model ScheduledAlertRuleTemplate no longer has parameter techniques
  - Model Watchlist no longer has parameter source_type
  - Parameter logic_app_resource_id of model PlaybookActionProperties is now required
  - Removed operation DataConnectorsOperations.connect
  - Removed operation DataConnectorsOperations.disconnect
  - Removed operation IncidentsOperations.create_team
  - Removed operation IncidentsOperations.run_playbook
  - Removed operation group BookmarkOperations
  - Removed operation group BookmarkRelationsOperations
  - Removed operation group DataConnectorsCheckRequirementsOperations
  - Removed operation group DomainWhoisOperations
  - Removed operation group EntitiesGetTimelineOperations
  - Removed operation group EntitiesOperations
  - Removed operation group EntitiesRelationsOperations
  - Removed operation group EntityQueriesOperations
  - Removed operation group EntityQueryTemplatesOperations
  - Removed operation group EntityRelationsOperations
  - Removed operation group IPGeodataOperations
  - Removed operation group MetadataOperations
  - Removed operation group OfficeConsentsOperations
  - Removed operation group ProductSettingsOperations
  - Removed operation group SourceControlOperations
  - Removed operation group SourceControlsOperations

## 1.0.0b2 (2022-03-30)

**Features**

  - Added operation ActionsOperations.create_or_update
  - Added operation ActionsOperations.delete
  - Added operation ActionsOperations.get
  - Added operation DataConnectorsOperations.connect
  - Added operation DataConnectorsOperations.disconnect
  - Added operation IncidentCommentsOperations.create_or_update
  - Added operation IncidentCommentsOperations.delete
  - Added operation IncidentCommentsOperations.list
  - Added operation IncidentsOperations.create_team
  - Added operation IncidentsOperations.list_alerts
  - Added operation IncidentsOperations.list_bookmarks
  - Added operation IncidentsOperations.list_entities
  - Added operation IncidentsOperations.run_playbook
  - Added operation group AutomationRulesOperations
  - Added operation group BookmarkOperations
  - Added operation group BookmarkRelationsOperations
  - Added operation group DataConnectorsCheckRequirementsOperations
  - Added operation group DomainWhoisOperations
  - Added operation group EntitiesGetTimelineOperations
  - Added operation group EntitiesOperations
  - Added operation group EntitiesRelationsOperations
  - Added operation group EntityQueriesOperations
  - Added operation group EntityQueryTemplatesOperations
  - Added operation group EntityRelationsOperations
  - Added operation group IPGeodataOperations
  - Added operation group IncidentRelationsOperations
  - Added operation group MetadataOperations
  - Added operation group OfficeConsentsOperations
  - Added operation group ProductSettingsOperations
  - Added operation group SentinelOnboardingStatesOperations
  - Added operation group SourceControlOperations
  - Added operation group SourceControlsOperations
  - Added operation group ThreatIntelligenceIndicatorMetricsOperations
  - Added operation group ThreatIntelligenceIndicatorOperations
  - Added operation group ThreatIntelligenceIndicatorsOperations
  - Added operation group WatchlistItemsOperations
  - Added operation group WatchlistsOperations
  - Model AADDataConnector has a new parameter system_data
  - Model AATPDataConnector has a new parameter system_data
  - Model ASCDataConnector has a new parameter system_data
  - Model ActionRequest has a new parameter system_data
  - Model ActionResponse has a new parameter system_data
  - Model AlertRule has a new parameter system_data
  - Model AlertRuleTemplate has a new parameter system_data
  - Model AwsCloudTrailDataConnector has a new parameter system_data
  - Model Bookmark has a new parameter entity_mappings
  - Model Bookmark has a new parameter event_time
  - Model Bookmark has a new parameter query_end_time
  - Model Bookmark has a new parameter query_start_time
  - Model Bookmark has a new parameter system_data
  - Model Bookmark has a new parameter tactics
  - Model Bookmark has a new parameter techniques
  - Model DataConnector has a new parameter system_data
  - Model FusionAlertRule has a new parameter scenario_exclusion_patterns
  - Model FusionAlertRule has a new parameter source_settings
  - Model FusionAlertRule has a new parameter system_data
  - Model FusionAlertRule has a new parameter techniques
  - Model FusionAlertRuleTemplate has a new parameter last_updated_date_utc
  - Model FusionAlertRuleTemplate has a new parameter source_settings
  - Model FusionAlertRuleTemplate has a new parameter system_data
  - Model FusionAlertRuleTemplate has a new parameter techniques
  - Model Incident has a new parameter provider_incident_id
  - Model Incident has a new parameter provider_name
  - Model Incident has a new parameter system_data
  - Model Incident has a new parameter team_information
  - Model IncidentAdditionalData has a new parameter provider_incident_url
  - Model IncidentAdditionalData has a new parameter techniques
  - Model IncidentComment has a new parameter etag
  - Model IncidentComment has a new parameter last_modified_time_utc
  - Model IncidentComment has a new parameter system_data
  - Model IncidentOwnerInfo has a new parameter owner_type
  - Model MCASDataConnector has a new parameter system_data
  - Model MDATPDataConnector has a new parameter system_data
  - Model MicrosoftSecurityIncidentCreationAlertRule has a new parameter system_data
  - Model MicrosoftSecurityIncidentCreationAlertRuleTemplate has a new parameter last_updated_date_utc
  - Model MicrosoftSecurityIncidentCreationAlertRuleTemplate has a new parameter system_data
  - Model OfficeConsent has a new parameter consent_id
  - Model OfficeConsent has a new parameter system_data
  - Model OfficeDataConnector has a new parameter system_data
  - Model Operation has a new parameter is_data_action
  - Model Operation has a new parameter origin
  - Model Resource has a new parameter system_data
  - Model ResourceWithEtag has a new parameter system_data
  - Model ScheduledAlertRule has a new parameter alert_details_override
  - Model ScheduledAlertRule has a new parameter custom_details
  - Model ScheduledAlertRule has a new parameter entity_mappings
  - Model ScheduledAlertRule has a new parameter event_grouping_settings
  - Model ScheduledAlertRule has a new parameter incident_configuration
  - Model ScheduledAlertRule has a new parameter system_data
  - Model ScheduledAlertRule has a new parameter techniques
  - Model ScheduledAlertRule has a new parameter template_version
  - Model ScheduledAlertRuleCommonProperties has a new parameter alert_details_override
  - Model ScheduledAlertRuleCommonProperties has a new parameter custom_details
  - Model ScheduledAlertRuleCommonProperties has a new parameter entity_mappings
  - Model ScheduledAlertRuleCommonProperties has a new parameter event_grouping_settings
  - Model ScheduledAlertRuleProperties has a new parameter alert_details_override
  - Model ScheduledAlertRuleProperties has a new parameter custom_details
  - Model ScheduledAlertRuleProperties has a new parameter entity_mappings
  - Model ScheduledAlertRuleProperties has a new parameter event_grouping_settings
  - Model ScheduledAlertRuleProperties has a new parameter incident_configuration
  - Model ScheduledAlertRuleProperties has a new parameter techniques
  - Model ScheduledAlertRuleProperties has a new parameter template_version
  - Model ScheduledAlertRuleTemplate has a new parameter alert_details_override
  - Model ScheduledAlertRuleTemplate has a new parameter custom_details
  - Model ScheduledAlertRuleTemplate has a new parameter entity_mappings
  - Model ScheduledAlertRuleTemplate has a new parameter event_grouping_settings
  - Model ScheduledAlertRuleTemplate has a new parameter last_updated_date_utc
  - Model ScheduledAlertRuleTemplate has a new parameter system_data
  - Model ScheduledAlertRuleTemplate has a new parameter techniques
  - Model ScheduledAlertRuleTemplate has a new parameter version
  - Model Settings has a new parameter system_data
  - Model TIDataConnector has a new parameter system_data
  - Model TIDataConnector has a new parameter tip_lookback_period

**Breaking changes**

  - Model OfficeConsent no longer has parameter tenant_name
  - Model OfficeDataConnectorDataTypes has a new required parameter teams
  - Parameter alerts of model AlertsDataTypeOfDataConnector is now required
  - Parameter alerts of model MCASDataConnectorDataTypes is now required
  - Parameter exchange of model OfficeDataConnectorDataTypes is now required
  - Parameter exchange of model OfficeDataConnectorDataTypes is now required
  - Parameter indicators of model TIDataConnectorDataTypes is now required
  - Parameter indicators of model TIDataConnectorDataTypes is now required
  - Parameter logs of model AwsCloudTrailDataConnectorDataTypes is now required
  - Parameter logs of model AwsCloudTrailDataConnectorDataTypes is now required
  - Parameter share_point of model OfficeDataConnectorDataTypes is now required
  - Parameter share_point of model OfficeDataConnectorDataTypes is now required
  - Parameter state of model AwsCloudTrailDataConnectorDataTypesLogs is now required
  - Parameter state of model DataConnectorDataTypeCommon is now required
  - Parameter state of model OfficeDataConnectorDataTypesExchange is now required
  - Parameter state of model OfficeDataConnectorDataTypesSharePoint is now required
  - Parameter state of model TIDataConnectorDataTypesIndicators is now required
  - Parameter tenant_id of model DataConnectorTenantId is now required
  - Parameter trigger_uri of model ActionRequestProperties is now required
  - Removed operation AlertRulesOperations.create_or_update_action
  - Removed operation AlertRulesOperations.delete_action
  - Removed operation AlertRulesOperations.get_action
  - Removed operation IncidentCommentsOperations.create_comment
  - Removed operation IncidentCommentsOperations.list_by_incident

## 1.0.0b1 (2020-11-10)

* Initial Release
