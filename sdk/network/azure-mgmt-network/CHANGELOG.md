## tsp migration

## 30.3.0 (2026-03-05)

change log generation failed!!! You need to write it manually!!!

### Breaking Changes

// will push tsp changes after [tsp definitions](https://github.com/Azure/azure-rest-api-specs/pull/40226#discussion_r2877262040) fixed to unblock python generation.
- Method `IpamPoolsOperations.list` parameter `skip` changed default value from `int` to `none`
- Method `IpamPoolsOperations.list` parameter `top` changed default value from `int` to `none`
- Method `ReachabilityAnalysisIntentsOperations.list` parameter `skip` changed default value from `int` to `none`
- Method `ReachabilityAnalysisIntentsOperations.list` parameter `top` changed default value from `int` to `none`
- Method `ReachabilityAnalysisRunsOperations.list` parameter `skip` changed default value from `int` to `none`
- Method `ReachabilityAnalysisRunsOperations.list` parameter `top` changed default value from `int` to `none`
- Method `StaticCidrsOperations.list` parameter `skip` changed default value from `int` to `none`
- Method `StaticCidrsOperations.list` parameter `top` changed default value from `int` to `none`
- Method `VerifierWorkspacesOperations.list` parameter `skip` changed default value from `int` to `none`
- Method `VerifierWorkspacesOperations.list` parameter `top` changed default value from `int` to `none`

// in [swagger](https://github.com/mcgallan/azure-rest-api-specs/blob/Convert-Network-2025-05/specification/network/resource-manager/Microsoft.Network/Network/stable/2025-05-01/virtualNetwork.json#L13612), parameter `singleton_resource` is defined as required, but somehow in SDK generated from swagger it is not present.
- Method `VipSwapOperations.begin_create` inserted a `positional_or_keyword` parameter `singleton_resource`
- Method `VipSwapOperations.get` inserted a `positional_or_keyword` parameter `singleton_resource`

// failed to mitigate, enum value type changed from float to int in migration.
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureDirection.fromhex`
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureDirection.hex`
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureMode.fromhex`
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureMode.hex`
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureSeverity.fromhex`
- Deleted or renamed enum value `FirewallPolicyIDPSSignatureSeverity.hex`

// failed to mitigate, might because the property name `GLOBAL`and `CONTINUE` are illegal. Now the property names are shown as like GLOBALEnum.
- Deleted or renamed enum value `Geo.GLOBAL`
- Deleted or renamed enum value `LoadBalancerSkuTier.GLOBAL`
- Deleted or renamed enum value `NextStep.CONTINUE`
- Deleted or renamed enum value `PublicIPAddressSkuTier.GLOBAL`
- Deleted or renamed enum value `PublicIPPrefixSkuTier.GLOBAL`

// failed to mitigate for it will cause duplication failures between namespace Network and Compute.
- Deleted or renamed method `NetworkInterfacesOperations.get_virtual_machine_scale_set_ip_configuration`
- Deleted or renamed method `NetworkInterfacesOperations.list_virtual_machine_scale_set_ip_configurations`
- Deleted or renamed method `NetworkInterfacesOperations.list_virtual_machine_scale_set_network_interfaces`
- Deleted or renamed method `PublicIPAddressesOperations.list_virtual_machine_scale_set_public_ip_addresses`

// seems to be fake report.
- Client `NetworkManagementClient` deleted or renamed instance variable `url`
- Method `ExpressRouteConnectionsOperations.list` changed from `asynchronous` to `synchronous`
- Method `ExpressRouteGatewaysOperations.list_by_resource_group` changed from `asynchronous` to `synchronous`
- Method `ExpressRouteGatewaysOperations.list_by_subscription` changed from `asynchronous` to `synchronous`
- Method `FirewallPolicyIdpsSignaturesOverridesOperations.list` changed from `asynchronous` to `synchronous`
- Method `NetworkManagerDeploymentStatusOperations.list` changed from `asynchronous` to `synchronous`
- Method `VipSwapOperations.list` changed from `asynchronous` to `synchronous`

- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `description`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `connectivity_topology`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `hubs`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `is_global`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `connectivity_capabilities`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `applies_to_groups`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `delete_existing_peering`
- Model `ActiveConnectivityConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `description`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `flag`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `protocol`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `sources`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `destinations`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `access`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `priority`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `direction`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `ActiveDefaultSecurityAdminRule` deleted or renamed its instance variable `resource_guid`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `description`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `protocol`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `sources`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `destinations`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `access`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `priority`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `direction`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `ActiveSecurityAdminRule` deleted or renamed its instance variable `resource_guid`
- Model `AdminRule` deleted or renamed its instance variable `description`
- Model `AdminRule` deleted or renamed its instance variable `protocol`
- Model `AdminRule` deleted or renamed its instance variable `sources`
- Model `AdminRule` deleted or renamed its instance variable `destinations`
- Model `AdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `AdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `AdminRule` deleted or renamed its instance variable `access`
- Model `AdminRule` deleted or renamed its instance variable `priority`
- Model `AdminRule` deleted or renamed its instance variable `direction`
- Model `AdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `AdminRule` deleted or renamed its instance variable `resource_guid`
- Model `AdminRuleCollection` deleted or renamed its instance variable `description`
- Model `AdminRuleCollection` deleted or renamed its instance variable `applies_to_groups`
- Model `AdminRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `AdminRuleCollection` deleted or renamed its instance variable `resource_guid`
- Model `ApplicationGateway` deleted or renamed its instance variable `sku`
- Model `ApplicationGateway` deleted or renamed its instance variable `ssl_policy`
- Model `ApplicationGateway` deleted or renamed its instance variable `operational_state`
- Model `ApplicationGateway` deleted or renamed its instance variable `gateway_ip_configurations`
- Model `ApplicationGateway` deleted or renamed its instance variable `authentication_certificates`
- Model `ApplicationGateway` deleted or renamed its instance variable `trusted_root_certificates`
- Model `ApplicationGateway` deleted or renamed its instance variable `trusted_client_certificates`
- Model `ApplicationGateway` deleted or renamed its instance variable `ssl_certificates`
- Model `ApplicationGateway` deleted or renamed its instance variable `frontend_ip_configurations`
- Model `ApplicationGateway` deleted or renamed its instance variable `frontend_ports`
- Model `ApplicationGateway` deleted or renamed its instance variable `probes`
- Model `ApplicationGateway` deleted or renamed its instance variable `backend_address_pools`
- Model `ApplicationGateway` deleted or renamed its instance variable `backend_http_settings_collection`
- Model `ApplicationGateway` deleted or renamed its instance variable `backend_settings_collection`
- Model `ApplicationGateway` deleted or renamed its instance variable `http_listeners`
- Model `ApplicationGateway` deleted or renamed its instance variable `listeners`
- Model `ApplicationGateway` deleted or renamed its instance variable `ssl_profiles`
- Model `ApplicationGateway` deleted or renamed its instance variable `url_path_maps`
- Model `ApplicationGateway` deleted or renamed its instance variable `request_routing_rules`
- Model `ApplicationGateway` deleted or renamed its instance variable `routing_rules`
- Model `ApplicationGateway` deleted or renamed its instance variable `rewrite_rule_sets`
- Model `ApplicationGateway` deleted or renamed its instance variable `redirect_configurations`
- Model `ApplicationGateway` deleted or renamed its instance variable `web_application_firewall_configuration`
- Model `ApplicationGateway` deleted or renamed its instance variable `firewall_policy`
- Model `ApplicationGateway` deleted or renamed its instance variable `enable_http2`
- Model `ApplicationGateway` deleted or renamed its instance variable `enable_fips`
- Model `ApplicationGateway` deleted or renamed its instance variable `autoscale_configuration`
- Model `ApplicationGateway` deleted or renamed its instance variable `private_link_configurations`
- Model `ApplicationGateway` deleted or renamed its instance variable `private_endpoint_connections`
- Model `ApplicationGateway` deleted or renamed its instance variable `resource_guid`
- Model `ApplicationGateway` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGateway` deleted or renamed its instance variable `custom_error_configurations`
- Model `ApplicationGateway` deleted or renamed its instance variable `force_firewall_policy_association`
- Model `ApplicationGateway` deleted or renamed its instance variable `load_distribution_policies`
- Model `ApplicationGateway` deleted or renamed its instance variable `entra_jwt_validation_configs`
- Model `ApplicationGateway` deleted or renamed its instance variable `global_configuration`
- Model `ApplicationGateway` deleted or renamed its instance variable `default_predefined_ssl_policy`
- Model `ApplicationGatewayAuthenticationCertificate` deleted or renamed its instance variable `data`
- Model `ApplicationGatewayAuthenticationCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayAvailableSslOptions` deleted or renamed its instance variable `predefined_policies`
- Model `ApplicationGatewayAvailableSslOptions` deleted or renamed its instance variable `default_policy`
- Model `ApplicationGatewayAvailableSslOptions` deleted or renamed its instance variable `available_cipher_suites`
- Model `ApplicationGatewayAvailableSslOptions` deleted or renamed its instance variable `available_protocols`
- Model `ApplicationGatewayBackendAddressPool` deleted or renamed its instance variable `backend_ip_configurations`
- Model `ApplicationGatewayBackendAddressPool` deleted or renamed its instance variable `backend_addresses`
- Model `ApplicationGatewayBackendAddressPool` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `port`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `protocol`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `cookie_based_affinity`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `request_timeout`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `probe`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `authentication_certificates`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `trusted_root_certificates`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `connection_draining`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `host_name`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `pick_host_name_from_backend_address`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `affinity_cookie_name`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `probe_enabled`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `path`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `dedicated_backend_connection`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `validate_cert_chain_and_expiry`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `validate_sni`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `sni_name`
- Model `ApplicationGatewayBackendHttpSettings` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `port`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `protocol`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `timeout`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `probe`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `trusted_root_certificates`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `host_name`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `pick_host_name_from_backend_address`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `enable_l4_client_ip_preservation`
- Model `ApplicationGatewayBackendSettings` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayEntraJWTValidationConfig` deleted or renamed its instance variable `un_authorized_request_action`
- Model `ApplicationGatewayEntraJWTValidationConfig` deleted or renamed its instance variable `tenant_id`
- Model `ApplicationGatewayEntraJWTValidationConfig` deleted or renamed its instance variable `client_id`
- Model `ApplicationGatewayEntraJWTValidationConfig` deleted or renamed its instance variable `audiences`
- Model `ApplicationGatewayEntraJWTValidationConfig` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayFirewallRuleSet` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayFirewallRuleSet` deleted or renamed its instance variable `rule_set_type`
- Model `ApplicationGatewayFirewallRuleSet` deleted or renamed its instance variable `rule_set_version`
- Model `ApplicationGatewayFirewallRuleSet` deleted or renamed its instance variable `rule_groups`
- Model `ApplicationGatewayFirewallRuleSet` deleted or renamed its instance variable `tiers`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `private_link_configuration`
- Model `ApplicationGatewayFrontendIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayFrontendPort` deleted or renamed its instance variable `port`
- Model `ApplicationGatewayFrontendPort` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `frontend_ip_configuration`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `frontend_port`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `protocol`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `host_name`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `ssl_certificate`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `ssl_profile`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `require_server_name_indication`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `custom_error_configurations`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `firewall_policy`
- Model `ApplicationGatewayHttpListener` deleted or renamed its instance variable `host_names`
- Model `ApplicationGatewayIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `ApplicationGatewayIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `frontend_ip_configuration`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `frontend_port`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `protocol`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `ssl_certificate`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `ssl_profile`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayListener` deleted or renamed its instance variable `host_names`
- Model `ApplicationGatewayLoadDistributionPolicy` deleted or renamed its instance variable `load_distribution_targets`
- Model `ApplicationGatewayLoadDistributionPolicy` deleted or renamed its instance variable `load_distribution_algorithm`
- Model `ApplicationGatewayLoadDistributionPolicy` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayLoadDistributionTarget` deleted or renamed its instance variable `weight_per_server`
- Model `ApplicationGatewayLoadDistributionTarget` deleted or renamed its instance variable `backend_address_pool`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `paths`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `backend_address_pool`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `backend_http_settings`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `redirect_configuration`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `rewrite_rule_set`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `load_distribution_policy`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayPathRule` deleted or renamed its instance variable `firewall_policy`
- Model `ApplicationGatewayPrivateEndpointConnection` deleted or renamed its instance variable `private_endpoint`
- Model `ApplicationGatewayPrivateEndpointConnection` deleted or renamed its instance variable `private_link_service_connection_state`
- Model `ApplicationGatewayPrivateEndpointConnection` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayPrivateEndpointConnection` deleted or renamed its instance variable `link_identifier`
- Model `ApplicationGatewayPrivateLinkConfiguration` deleted or renamed its instance variable `ip_configurations`
- Model `ApplicationGatewayPrivateLinkConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayPrivateLinkIpConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `ApplicationGatewayPrivateLinkIpConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `ApplicationGatewayPrivateLinkIpConfiguration` deleted or renamed its instance variable `subnet`
- Model `ApplicationGatewayPrivateLinkIpConfiguration` deleted or renamed its instance variable `primary`
- Model `ApplicationGatewayPrivateLinkIpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayPrivateLinkResource` deleted or renamed its instance variable `group_id`
- Model `ApplicationGatewayPrivateLinkResource` deleted or renamed its instance variable `required_members`
- Model `ApplicationGatewayPrivateLinkResource` deleted or renamed its instance variable `required_zone_names`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `protocol`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `host`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `path`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `interval`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `timeout`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `unhealthy_threshold`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `pick_host_name_from_backend_http_settings`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `pick_host_name_from_backend_settings`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `min_servers`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `match`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `enable_probe_proxy_protocol_header`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayProbe` deleted or renamed its instance variable `port`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `redirect_type`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `target_listener`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `target_url`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `include_path`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `include_query_string`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `request_routing_rules`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `url_path_maps`
- Model `ApplicationGatewayRedirectConfiguration` deleted or renamed its instance variable `path_rules`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `rule_type`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `priority`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `backend_address_pool`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `backend_http_settings`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `http_listener`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `url_path_map`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `rewrite_rule_set`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `redirect_configuration`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `load_distribution_policy`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `entra_jwt_validation_config`
- Model `ApplicationGatewayRequestRoutingRule` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayRewriteRuleSet` deleted or renamed its instance variable `rewrite_rules`
- Model `ApplicationGatewayRewriteRuleSet` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `rule_type`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `priority`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `backend_address_pool`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `backend_settings`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `listener`
- Model `ApplicationGatewayRoutingRule` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewaySslCertificate` deleted or renamed its instance variable `data`
- Model `ApplicationGatewaySslCertificate` deleted or renamed its instance variable `password`
- Model `ApplicationGatewaySslCertificate` deleted or renamed its instance variable `public_cert_data`
- Model `ApplicationGatewaySslCertificate` deleted or renamed its instance variable `key_vault_secret_id`
- Model `ApplicationGatewaySslCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewaySslPredefinedPolicy` deleted or renamed its instance variable `cipher_suites`
- Model `ApplicationGatewaySslPredefinedPolicy` deleted or renamed its instance variable `min_protocol_version`
- Model `ApplicationGatewaySslProfile` deleted or renamed its instance variable `trusted_client_certificates`
- Model `ApplicationGatewaySslProfile` deleted or renamed its instance variable `ssl_policy`
- Model `ApplicationGatewaySslProfile` deleted or renamed its instance variable `client_auth_configuration`
- Model `ApplicationGatewaySslProfile` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayTrustedClientCertificate` deleted or renamed its instance variable `data`
- Model `ApplicationGatewayTrustedClientCertificate` deleted or renamed its instance variable `validated_cert_data`
- Model `ApplicationGatewayTrustedClientCertificate` deleted or renamed its instance variable `client_cert_issuer_dn`
- Model `ApplicationGatewayTrustedClientCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayTrustedRootCertificate` deleted or renamed its instance variable `data`
- Model `ApplicationGatewayTrustedRootCertificate` deleted or renamed its instance variable `key_vault_secret_id`
- Model `ApplicationGatewayTrustedRootCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `default_backend_address_pool`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `default_backend_http_settings`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `default_rewrite_rule_set`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `default_redirect_configuration`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `default_load_distribution_policy`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `path_rules`
- Model `ApplicationGatewayUrlPathMap` deleted or renamed its instance variable `provisioning_state`
- Model `ApplicationGatewayWafDynamicManifestResult` deleted or renamed its instance variable `available_rule_sets`
- Model `ApplicationGatewayWafDynamicManifestResult` deleted or renamed its instance variable `rule_set_type`
- Model `ApplicationGatewayWafDynamicManifestResult` deleted or renamed its instance variable `rule_set_version`
- Model `ApplicationSecurityGroup` deleted or renamed its instance variable `resource_guid`
- Model `ApplicationSecurityGroup` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewall` deleted or renamed its instance variable `application_rule_collections`
- Model `AzureFirewall` deleted or renamed its instance variable `nat_rule_collections`
- Model `AzureFirewall` deleted or renamed its instance variable `network_rule_collections`
- Model `AzureFirewall` deleted or renamed its instance variable `ip_configurations`
- Model `AzureFirewall` deleted or renamed its instance variable `management_ip_configuration`
- Model `AzureFirewall` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewall` deleted or renamed its instance variable `threat_intel_mode`
- Model `AzureFirewall` deleted or renamed its instance variable `virtual_hub`
- Model `AzureFirewall` deleted or renamed its instance variable `firewall_policy`
- Model `AzureFirewall` deleted or renamed its instance variable `hub_ip_addresses`
- Model `AzureFirewall` deleted or renamed its instance variable `ip_groups`
- Model `AzureFirewall` deleted or renamed its instance variable `sku`
- Model `AzureFirewall` deleted or renamed its instance variable `autoscale_configuration`
- Model `AzureFirewallApplicationRuleCollection` deleted or renamed its instance variable `priority`
- Model `AzureFirewallApplicationRuleCollection` deleted or renamed its instance variable `action`
- Model `AzureFirewallApplicationRuleCollection` deleted or renamed its instance variable `rules`
- Model `AzureFirewallApplicationRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewallFqdnTag` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewallFqdnTag` deleted or renamed its instance variable `fqdn_tag_name`
- Model `AzureFirewallIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `AzureFirewallIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `AzureFirewallIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `AzureFirewallIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewallNatRuleCollection` deleted or renamed its instance variable `priority`
- Model `AzureFirewallNatRuleCollection` deleted or renamed its instance variable `action`
- Model `AzureFirewallNatRuleCollection` deleted or renamed its instance variable `rules`
- Model `AzureFirewallNatRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `AzureFirewallNetworkRuleCollection` deleted or renamed its instance variable `priority`
- Model `AzureFirewallNetworkRuleCollection` deleted or renamed its instance variable `action`
- Model `AzureFirewallNetworkRuleCollection` deleted or renamed its instance variable `rules`
- Model `AzureFirewallNetworkRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `AzureWebCategory` deleted or renamed its instance variable `group`
- Model `BackendAddressPool` deleted or renamed its instance variable `location`
- Model `BackendAddressPool` deleted or renamed its instance variable `tunnel_interfaces`
- Model `BackendAddressPool` deleted or renamed its instance variable `load_balancer_backend_addresses`
- Model `BackendAddressPool` deleted or renamed its instance variable `backend_ip_configurations`
- Model `BackendAddressPool` deleted or renamed its instance variable `load_balancing_rules`
- Model `BackendAddressPool` deleted or renamed its instance variable `outbound_rule`
- Model `BackendAddressPool` deleted or renamed its instance variable `outbound_rules`
- Model `BackendAddressPool` deleted or renamed its instance variable `inbound_nat_rules`
- Model `BackendAddressPool` deleted or renamed its instance variable `provisioning_state`
- Model `BackendAddressPool` deleted or renamed its instance variable `drain_period_in_seconds`
- Model `BackendAddressPool` deleted or renamed its instance variable `virtual_network`
- Model `BackendAddressPool` deleted or renamed its instance variable `sync_mode`
- Model `BastionHost` deleted or renamed its instance variable `ip_configurations`
- Model `BastionHost` deleted or renamed its instance variable `dns_name`
- Model `BastionHost` deleted or renamed its instance variable `virtual_network`
- Model `BastionHost` deleted or renamed its instance variable `network_acls`
- Model `BastionHost` deleted or renamed its instance variable `provisioning_state`
- Model `BastionHost` deleted or renamed its instance variable `scale_units`
- Model `BastionHost` deleted or renamed its instance variable `disable_copy_paste`
- Model `BastionHost` deleted or renamed its instance variable `enable_file_copy`
- Model `BastionHost` deleted or renamed its instance variable `enable_ip_connect`
- Model `BastionHost` deleted or renamed its instance variable `enable_shareable_link`
- Model `BastionHost` deleted or renamed its instance variable `enable_tunneling`
- Model `BastionHost` deleted or renamed its instance variable `enable_kerberos`
- Model `BastionHost` deleted or renamed its instance variable `enable_session_recording`
- Model `BastionHost` deleted or renamed its instance variable `enable_private_only_bastion`
- Model `BastionHostIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `BastionHostIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `BastionHostIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `BastionHostIPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `BgpConnection` deleted or renamed its instance variable `peer_asn`
- Model `BgpConnection` deleted or renamed its instance variable `peer_ip`
- Model `BgpConnection` deleted or renamed its instance variable `hub_virtual_network_connection`
- Model `BgpConnection` deleted or renamed its instance variable `provisioning_state`
- Model `BgpConnection` deleted or renamed its instance variable `connection_state`
- Model `BgpServiceCommunity` deleted or renamed its instance variable `service_name`
- Model `BgpServiceCommunity` deleted or renamed its instance variable `bgp_communities`
- Model `ConfigurationGroup` deleted or renamed its instance variable `description`
- Model `ConfigurationGroup` deleted or renamed its instance variable `member_type`
- Model `ConfigurationGroup` deleted or renamed its instance variable `provisioning_state`
- Model `ConfigurationGroup` deleted or renamed its instance variable `resource_guid`
- Model `ConnectionMonitor` deleted or renamed its instance variable `source`
- Model `ConnectionMonitor` deleted or renamed its instance variable `destination`
- Model `ConnectionMonitor` deleted or renamed its instance variable `auto_start`
- Model `ConnectionMonitor` deleted or renamed its instance variable `monitoring_interval_in_seconds`
- Model `ConnectionMonitor` deleted or renamed its instance variable `endpoints`
- Model `ConnectionMonitor` deleted or renamed its instance variable `test_configurations`
- Model `ConnectionMonitor` deleted or renamed its instance variable `test_groups`
- Model `ConnectionMonitor` deleted or renamed its instance variable `outputs`
- Model `ConnectionMonitor` deleted or renamed its instance variable `notes`
- Model `ConnectionMonitorEndpointFilter` deleted or renamed its instance variable `items`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `source`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `destination`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `auto_start`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `monitoring_interval_in_seconds`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `endpoints`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `test_configurations`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `test_groups`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `outputs`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `notes`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `provisioning_state`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `start_time`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `monitoring_status`
- Model `ConnectionMonitorResult` deleted or renamed its instance variable `connection_monitor_type`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `description`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `connectivity_topology`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `hubs`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `is_global`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `connectivity_capabilities`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `applies_to_groups`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `delete_existing_peering`
- Model `ConnectivityConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `ContainerNetworkInterface` deleted or renamed its instance variable `container_network_interface_configuration`
- Model `ContainerNetworkInterface` deleted or renamed its instance variable `container`
- Model `ContainerNetworkInterface` deleted or renamed its instance variable `ip_configurations`
- Model `ContainerNetworkInterface` deleted or renamed its instance variable `provisioning_state`
- Model `ContainerNetworkInterfaceConfiguration` deleted or renamed its instance variable `ip_configurations`
- Model `ContainerNetworkInterfaceConfiguration` deleted or renamed its instance variable `container_network_interfaces`
- Model `ContainerNetworkInterfaceConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `ContainerNetworkInterfaceIpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `CustomIpPrefix` deleted or renamed its instance variable `asn`
- Model `CustomIpPrefix` deleted or renamed its instance variable `cidr`
- Model `CustomIpPrefix` deleted or renamed its instance variable `signed_message`
- Model `CustomIpPrefix` deleted or renamed its instance variable `authorization_message`
- Model `CustomIpPrefix` deleted or renamed its instance variable `custom_ip_prefix_parent`
- Model `CustomIpPrefix` deleted or renamed its instance variable `child_custom_ip_prefixes`
- Model `CustomIpPrefix` deleted or renamed its instance variable `commissioned_state`
- Model `CustomIpPrefix` deleted or renamed its instance variable `express_route_advertise`
- Model `CustomIpPrefix` deleted or renamed its instance variable `geo`
- Model `CustomIpPrefix` deleted or renamed its instance variable `no_internet_advertise`
- Model `CustomIpPrefix` deleted or renamed its instance variable `prefix_type`
- Model `CustomIpPrefix` deleted or renamed its instance variable `public_ip_prefixes`
- Model `CustomIpPrefix` deleted or renamed its instance variable `resource_guid`
- Model `CustomIpPrefix` deleted or renamed its instance variable `failed_reason`
- Model `CustomIpPrefix` deleted or renamed its instance variable `provisioning_state`
- Model `DdosCustomPolicy` deleted or renamed its instance variable `resource_guid`
- Model `DdosCustomPolicy` deleted or renamed its instance variable `provisioning_state`
- Model `DdosCustomPolicy` deleted or renamed its instance variable `detection_rules`
- Model `DdosCustomPolicy` deleted or renamed its instance variable `front_end_ip_configuration`
- Model `DdosDetectionRule` deleted or renamed its instance variable `provisioning_state`
- Model `DdosDetectionRule` deleted or renamed its instance variable `detection_mode`
- Model `DdosDetectionRule` deleted or renamed its instance variable `traffic_detection_rule`
- Model `DdosProtectionPlan` deleted or renamed its instance variable `resource_guid`
- Model `DdosProtectionPlan` deleted or renamed its instance variable `provisioning_state`
- Model `DdosProtectionPlan` deleted or renamed its instance variable `public_ip_addresses`
- Model `DdosProtectionPlan` deleted or renamed its instance variable `virtual_networks`
- Model `DefaultAdminRule` deleted or renamed its instance variable `description`
- Model `DefaultAdminRule` deleted or renamed its instance variable `flag`
- Model `DefaultAdminRule` deleted or renamed its instance variable `protocol`
- Model `DefaultAdminRule` deleted or renamed its instance variable `sources`
- Model `DefaultAdminRule` deleted or renamed its instance variable `destinations`
- Model `DefaultAdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `DefaultAdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `DefaultAdminRule` deleted or renamed its instance variable `access`
- Model `DefaultAdminRule` deleted or renamed its instance variable `priority`
- Model `DefaultAdminRule` deleted or renamed its instance variable `direction`
- Model `DefaultAdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `DefaultAdminRule` deleted or renamed its instance variable `resource_guid`
- Model `Delegation` deleted or renamed its instance variable `service_name`
- Model `Delegation` deleted or renamed its instance variable `actions`
- Model `Delegation` deleted or renamed its instance variable `provisioning_state`
- Model `DscpConfiguration` deleted or renamed its instance variable `markings`
- Model `DscpConfiguration` deleted or renamed its instance variable `source_ip_ranges`
- Model `DscpConfiguration` deleted or renamed its instance variable `destination_ip_ranges`
- Model `DscpConfiguration` deleted or renamed its instance variable `source_port_ranges`
- Model `DscpConfiguration` deleted or renamed its instance variable `destination_port_ranges`
- Model `DscpConfiguration` deleted or renamed its instance variable `protocol`
- Model `DscpConfiguration` deleted or renamed its instance variable `qos_definition_collection`
- Model `DscpConfiguration` deleted or renamed its instance variable `qos_collection_id`
- Model `DscpConfiguration` deleted or renamed its instance variable `associated_network_interfaces`
- Model `DscpConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `DscpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `description`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `connectivity_topology`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `hubs`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `is_global`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `connectivity_capabilities`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `applies_to_groups`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `delete_existing_peering`
- Model `EffectiveConnectivityConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `description`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `flag`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `protocol`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `sources`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `destinations`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `access`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `priority`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `direction`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `EffectiveDefaultSecurityAdminRule` deleted or renamed its instance variable `resource_guid`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `description`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `protocol`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `sources`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `destinations`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `source_port_ranges`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `access`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `priority`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `direction`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `provisioning_state`
- Model `EffectiveSecurityAdminRule` deleted or renamed its instance variable `resource_guid`
- Model `ExceptionEntry` deleted or renamed its instance variable `values`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `allow_classic_operations`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `circuit_provisioning_state`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `service_provider_provisioning_state`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `authorizations`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `peerings`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `service_key`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `service_provider_notes`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `service_provider_properties`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `express_route_port`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `bandwidth_in_gbps`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `stag`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `gateway_manager_etag`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `global_reach_enabled`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `authorization_key`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `authorization_status`
- Model `ExpressRouteCircuit` deleted or renamed its instance variable `enable_direct_port_rate_limit`
- Model `ExpressRouteCircuitAuthorization` deleted or renamed its instance variable `authorization_key`
- Model `ExpressRouteCircuitAuthorization` deleted or renamed its instance variable `authorization_use_status`
- Model `ExpressRouteCircuitAuthorization` deleted or renamed its instance variable `connection_resource_uri`
- Model `ExpressRouteCircuitAuthorization` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `express_route_circuit_peering`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `peer_express_route_circuit_peering`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `address_prefix`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `authorization_key`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `ipv6_circuit_connection_config`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `circuit_connection_status`
- Model `ExpressRouteCircuitConnection` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `peering_type`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `state`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `azure_asn`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `peer_asn`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `primary_peer_address_prefix`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `secondary_peer_address_prefix`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `primary_azure_port`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `secondary_azure_port`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `shared_key`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `vlan_id`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `microsoft_peering_config`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `stats`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `gateway_manager_etag`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `last_modified_by`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `route_filter`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `ipv6_peering_config`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `express_route_connection`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `connections`
- Model `ExpressRouteCircuitPeering` deleted or renamed its instance variable `peered_connections`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `express_route_circuit_peering`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `authorization_key`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `routing_weight`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `enable_internet_security`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `express_route_gateway_bypass`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `enable_private_link_fast_path`
- Model `ExpressRouteConnection` deleted or renamed its instance variable `routing_configuration`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `primary_azure_port`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `secondary_azure_port`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `s_tag`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `peering_location`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `bandwidth_in_mbps`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `express_route_circuit`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `service_provider_provisioning_state`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `service_provider_notes`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCrossConnection` deleted or renamed its instance variable `peerings`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `peering_type`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `state`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `azure_asn`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `peer_asn`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `primary_peer_address_prefix`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `secondary_peer_address_prefix`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `primary_azure_port`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `secondary_azure_port`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `shared_key`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `vlan_id`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `microsoft_peering_config`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `gateway_manager_etag`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `last_modified_by`
- Model `ExpressRouteCrossConnectionPeering` deleted or renamed its instance variable `ipv6_peering_config`
- Model `ExpressRouteGateway` deleted or renamed its instance variable `auto_scale_configuration`
- Model `ExpressRouteGateway` deleted or renamed its instance variable `express_route_connections`
- Model `ExpressRouteGateway` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteGateway` deleted or renamed its instance variable `virtual_hub`
- Model `ExpressRouteGateway` deleted or renamed its instance variable `allow_non_virtual_wan_traffic`
- Model `ExpressRouteLink` deleted or renamed its instance variable `router_name`
- Model `ExpressRouteLink` deleted or renamed its instance variable `interface_name`
- Model `ExpressRouteLink` deleted or renamed its instance variable `patch_panel_id`
- Model `ExpressRouteLink` deleted or renamed its instance variable `rack_id`
- Model `ExpressRouteLink` deleted or renamed its instance variable `colo_location`
- Model `ExpressRouteLink` deleted or renamed its instance variable `connector_type`
- Model `ExpressRouteLink` deleted or renamed its instance variable `admin_state`
- Model `ExpressRouteLink` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteLink` deleted or renamed its instance variable `mac_sec_config`
- Model `ExpressRoutePort` deleted or renamed its instance variable `peering_location`
- Model `ExpressRoutePort` deleted or renamed its instance variable `bandwidth_in_gbps`
- Model `ExpressRoutePort` deleted or renamed its instance variable `provisioned_bandwidth_in_gbps`
- Model `ExpressRoutePort` deleted or renamed its instance variable `mtu`
- Model `ExpressRoutePort` deleted or renamed its instance variable `encapsulation`
- Model `ExpressRoutePort` deleted or renamed its instance variable `ether_type`
- Model `ExpressRoutePort` deleted or renamed its instance variable `allocation_date`
- Model `ExpressRoutePort` deleted or renamed its instance variable `links`
- Model `ExpressRoutePort` deleted or renamed its instance variable `circuits`
- Model `ExpressRoutePort` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRoutePort` deleted or renamed its instance variable `resource_guid`
- Model `ExpressRoutePort` deleted or renamed its instance variable `billing_type`
- Model `ExpressRoutePortAuthorization` deleted or renamed its instance variable `authorization_key`
- Model `ExpressRoutePortAuthorization` deleted or renamed its instance variable `authorization_use_status`
- Model `ExpressRoutePortAuthorization` deleted or renamed its instance variable `circuit_resource_uri`
- Model `ExpressRoutePortAuthorization` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRoutePortsLocation` deleted or renamed its instance variable `address`
- Model `ExpressRoutePortsLocation` deleted or renamed its instance variable `contact`
- Model `ExpressRoutePortsLocation` deleted or renamed its instance variable `available_bandwidths`
- Model `ExpressRoutePortsLocation` deleted or renamed its instance variable `provisioning_state`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `port_pair_descriptor`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `primary_azure_port`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `secondary_azure_port`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `peering_location`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `overprovision_factor`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `port_bandwidth_in_mbps`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `used_bandwidth_in_mbps`
- Model `ExpressRouteProviderPort` deleted or renamed its instance variable `remaining_bandwidth_in_mbps`
- Model `ExpressRouteServiceProvider` deleted or renamed its instance variable `peering_locations`
- Model `ExpressRouteServiceProvider` deleted or renamed its instance variable `bandwidths_offered`
- Model `ExpressRouteServiceProvider` deleted or renamed its instance variable `provisioning_state`
- Model `FilterItems` deleted or renamed its instance variable `values`
- Model `FirewallPolicy` deleted or renamed its instance variable `size`
- Model `FirewallPolicy` deleted or renamed its instance variable `rule_collection_groups`
- Model `FirewallPolicy` deleted or renamed its instance variable `provisioning_state`
- Model `FirewallPolicy` deleted or renamed its instance variable `base_policy`
- Model `FirewallPolicy` deleted or renamed its instance variable `firewalls`
- Model `FirewallPolicy` deleted or renamed its instance variable `child_policies`
- Model `FirewallPolicy` deleted or renamed its instance variable `threat_intel_mode`
- Model `FirewallPolicy` deleted or renamed its instance variable `threat_intel_whitelist`
- Model `FirewallPolicy` deleted or renamed its instance variable `insights`
- Model `FirewallPolicy` deleted or renamed its instance variable `snat`
- Model `FirewallPolicy` deleted or renamed its instance variable `sql`
- Model `FirewallPolicy` deleted or renamed its instance variable `dns_settings`
- Model `FirewallPolicy` deleted or renamed its instance variable `explicit_proxy`
- Model `FirewallPolicy` deleted or renamed its instance variable `intrusion_detection`
- Model `FirewallPolicy` deleted or renamed its instance variable `transport_security`
- Model `FirewallPolicy` deleted or renamed its instance variable `sku`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `base_policy`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `threat_intel_mode`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `threat_intel_whitelist`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `insights`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `snat`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `sql`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `dns_settings`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `explicit_proxy`
- Model `FirewallPolicyDraft` deleted or renamed its instance variable `intrusion_detection`
- Model `FirewallPolicyRuleCollectionGroup` deleted or renamed its instance variable `size`
- Model `FirewallPolicyRuleCollectionGroup` deleted or renamed its instance variable `priority`
- Model `FirewallPolicyRuleCollectionGroup` deleted or renamed its instance variable `rule_collections`
- Model `FirewallPolicyRuleCollectionGroup` deleted or renamed its instance variable `provisioning_state`
- Model `FirewallPolicyRuleCollectionGroupDraft` deleted or renamed its instance variable `size`
- Model `FirewallPolicyRuleCollectionGroupDraft` deleted or renamed its instance variable `priority`
- Model `FirewallPolicyRuleCollectionGroupDraft` deleted or renamed its instance variable `rule_collections`
- Model `FlowLog` deleted or renamed its instance variable `target_resource_id`
- Model `FlowLog` deleted or renamed its instance variable `target_resource_guid`
- Model `FlowLog` deleted or renamed its instance variable `storage_id`
- Model `FlowLog` deleted or renamed its instance variable `enabled_filtering_criteria`
- Model `FlowLog` deleted or renamed its instance variable `record_types`
- Model `FlowLog` deleted or renamed its instance variable `enabled`
- Model `FlowLog` deleted or renamed its instance variable `retention_policy`
- Model `FlowLog` deleted or renamed its instance variable `format`
- Model `FlowLog` deleted or renamed its instance variable `flow_analytics_configuration`
- Model `FlowLog` deleted or renamed its instance variable `provisioning_state`
- Model `FlowLogInformation` deleted or renamed its instance variable `storage_id`
- Model `FlowLogInformation` deleted or renamed its instance variable `enabled_filtering_criteria`
- Model `FlowLogInformation` deleted or renamed its instance variable `record_types`
- Model `FlowLogInformation` deleted or renamed its instance variable `enabled`
- Model `FlowLogInformation` deleted or renamed its instance variable `retention_policy`
- Model `FlowLogInformation` deleted or renamed its instance variable `format`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `inbound_nat_rules`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `inbound_nat_pools`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `outbound_rules`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `load_balancing_rules`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `private_ip_address_version`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `public_ip_prefix`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `gateway_load_balancer`
- Model `FrontendIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `HopLink` deleted or renamed its instance variable `round_trip_time_min`
- Model `HopLink` deleted or renamed its instance variable `round_trip_time_avg`
- Model `HopLink` deleted or renamed its instance variable `round_trip_time_max`
- Model `HubIpConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `HubIpConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `HubIpConfiguration` deleted or renamed its instance variable `subnet`
- Model `HubIpConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `HubIpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `HubRouteTable` deleted or renamed its instance variable `routes`
- Model `HubRouteTable` deleted or renamed its instance variable `labels`
- Model `HubRouteTable` deleted or renamed its instance variable `associated_connections`
- Model `HubRouteTable` deleted or renamed its instance variable `propagating_connections`
- Model `HubRouteTable` deleted or renamed its instance variable `provisioning_state`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `remote_virtual_network`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `allow_hub_to_remote_vnet_transit`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `allow_remote_vnet_to_use_hub_vnet_gateways`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `enable_internet_security`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `routing_configuration`
- Model `HubVirtualNetworkConnection` deleted or renamed its instance variable `provisioning_state`
- Model `IPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `IPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `IPConfiguration` deleted or renamed its instance variable `subnet`
- Model `IPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `IPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `IPConfigurationProfile` deleted or renamed its instance variable `subnet`
- Model `IPConfigurationProfile` deleted or renamed its instance variable `provisioning_state`
- Model `InboundNatPool` deleted or renamed its instance variable `frontend_ip_configuration`
- Model `InboundNatPool` deleted or renamed its instance variable `protocol`
- Model `InboundNatPool` deleted or renamed its instance variable `frontend_port_range_start`
- Model `InboundNatPool` deleted or renamed its instance variable `frontend_port_range_end`
- Model `InboundNatPool` deleted or renamed its instance variable `backend_port`
- Model `InboundNatPool` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `InboundNatPool` deleted or renamed its instance variable `enable_floating_ip`
- Model `InboundNatPool` deleted or renamed its instance variable `enable_tcp_reset`
- Model `InboundNatPool` deleted or renamed its instance variable `provisioning_state`
- Model `InboundNatRule` deleted or renamed its instance variable `frontend_ip_configuration`
- Model `InboundNatRule` deleted or renamed its instance variable `backend_ip_configuration`
- Model `InboundNatRule` deleted or renamed its instance variable `protocol`
- Model `InboundNatRule` deleted or renamed its instance variable `frontend_port`
- Model `InboundNatRule` deleted or renamed its instance variable `backend_port`
- Model `InboundNatRule` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `InboundNatRule` deleted or renamed its instance variable `enable_floating_ip`
- Model `InboundNatRule` deleted or renamed its instance variable `enable_tcp_reset`
- Model `InboundNatRule` deleted or renamed its instance variable `frontend_port_range_start`
- Model `InboundNatRule` deleted or renamed its instance variable `frontend_port_range_end`
- Model `InboundNatRule` deleted or renamed its instance variable `backend_address_pool`
- Model `InboundNatRule` deleted or renamed its instance variable `provisioning_state`
- Model `InboundSecurityRule` deleted or renamed its instance variable `rule_type`
- Model `InboundSecurityRule` deleted or renamed its instance variable `rules`
- Model `InboundSecurityRule` deleted or renamed its instance variable `provisioning_state`
- Model `IpAllocation` deleted or renamed its instance variable `subnet`
- Model `IpAllocation` deleted or renamed its instance variable `virtual_network`
- Model `IpAllocation` deleted or renamed its instance variable `type_properties_type`
- Model `IpAllocation` deleted or renamed its instance variable `prefix`
- Model `IpAllocation` deleted or renamed its instance variable `prefix_length`
- Model `IpAllocation` deleted or renamed its instance variable `prefix_type`
- Model `IpAllocation` deleted or renamed its instance variable `ipam_allocation_id`
- Model `IpAllocation` deleted or renamed its instance variable `allocation_tags`
- Model `IpGroup` deleted or renamed its instance variable `provisioning_state`
- Model `IpGroup` deleted or renamed its instance variable `ip_addresses`
- Model `IpGroup` deleted or renamed its instance variable `firewalls`
- Model `IpGroup` deleted or renamed its instance variable `firewall_policies`
- Model `IpamPoolPrefixAllocation` deleted or renamed its instance variable `id`
- Model `LoadBalancer` deleted or renamed its instance variable `frontend_ip_configurations`
- Model `LoadBalancer` deleted or renamed its instance variable `backend_address_pools`
- Model `LoadBalancer` deleted or renamed its instance variable `load_balancing_rules`
- Model `LoadBalancer` deleted or renamed its instance variable `probes`
- Model `LoadBalancer` deleted or renamed its instance variable `inbound_nat_rules`
- Model `LoadBalancer` deleted or renamed its instance variable `inbound_nat_pools`
- Model `LoadBalancer` deleted or renamed its instance variable `outbound_rules`
- Model `LoadBalancer` deleted or renamed its instance variable `resource_guid`
- Model `LoadBalancer` deleted or renamed its instance variable `provisioning_state`
- Model `LoadBalancer` deleted or renamed its instance variable `scope`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `virtual_network`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `subnet`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `ip_address`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `network_interface_ip_configuration`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `load_balancer_frontend_ip_configuration`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `inbound_nat_rules_port_mapping`
- Model `LoadBalancerBackendAddress` deleted or renamed its instance variable `admin_state`
- Model `LoadBalancerVipSwapRequestFrontendIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `LoadBalancingRule` deleted or renamed its instance variable `frontend_ip_configuration`
- Model `LoadBalancingRule` deleted or renamed its instance variable `backend_address_pool`
- Model `LoadBalancingRule` deleted or renamed its instance variable `backend_address_pools`
- Model `LoadBalancingRule` deleted or renamed its instance variable `probe`
- Model `LoadBalancingRule` deleted or renamed its instance variable `protocol`
- Model `LoadBalancingRule` deleted or renamed its instance variable `load_distribution`
- Model `LoadBalancingRule` deleted or renamed its instance variable `frontend_port`
- Model `LoadBalancingRule` deleted or renamed its instance variable `backend_port`
- Model `LoadBalancingRule` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `LoadBalancingRule` deleted or renamed its instance variable `enable_floating_ip`
- Model `LoadBalancingRule` deleted or renamed its instance variable `enable_tcp_reset`
- Model `LoadBalancingRule` deleted or renamed its instance variable `disable_outbound_snat`
- Model `LoadBalancingRule` deleted or renamed its instance variable `enable_connection_tracking`
- Model `LoadBalancingRule` deleted or renamed its instance variable `provisioning_state`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `local_network_address_space`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `gateway_ip_address`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `fqdn`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `bgp_settings`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `resource_guid`
- Model `LocalNetworkGateway` deleted or renamed its instance variable `provisioning_state`
- Model `NatGateway` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `NatGateway` deleted or renamed its instance variable `public_ip_addresses`
- Model `NatGateway` deleted or renamed its instance variable `public_ip_addresses_v6`
- Model `NatGateway` deleted or renamed its instance variable `public_ip_prefixes`
- Model `NatGateway` deleted or renamed its instance variable `public_ip_prefixes_v6`
- Model `NatGateway` deleted or renamed its instance variable `subnets`
- Model `NatGateway` deleted or renamed its instance variable `source_virtual_network`
- Model `NatGateway` deleted or renamed its instance variable `service_gateway`
- Model `NatGateway` deleted or renamed its instance variable `resource_guid`
- Model `NatGateway` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkGroup` deleted or renamed its instance variable `description`
- Model `NetworkGroup` deleted or renamed its instance variable `member_type`
- Model `NetworkGroup` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkGroup` deleted or renamed its instance variable `resource_guid`
- Model `NetworkInterface` deleted or renamed its instance variable `virtual_machine`
- Model `NetworkInterface` deleted or renamed its instance variable `network_security_group`
- Model `NetworkInterface` deleted or renamed its instance variable `private_endpoint`
- Model `NetworkInterface` deleted or renamed its instance variable `ip_configurations`
- Model `NetworkInterface` deleted or renamed its instance variable `tap_configurations`
- Model `NetworkInterface` deleted or renamed its instance variable `dns_settings`
- Model `NetworkInterface` deleted or renamed its instance variable `mac_address`
- Model `NetworkInterface` deleted or renamed its instance variable `primary`
- Model `NetworkInterface` deleted or renamed its instance variable `vnet_encryption_supported`
- Model `NetworkInterface` deleted or renamed its instance variable `default_outbound_connectivity_enabled`
- Model `NetworkInterface` deleted or renamed its instance variable `enable_accelerated_networking`
- Model `NetworkInterface` deleted or renamed its instance variable `disable_tcp_state_tracking`
- Model `NetworkInterface` deleted or renamed its instance variable `enable_ip_forwarding`
- Model `NetworkInterface` deleted or renamed its instance variable `hosted_workloads`
- Model `NetworkInterface` deleted or renamed its instance variable `dscp_configuration`
- Model `NetworkInterface` deleted or renamed its instance variable `resource_guid`
- Model `NetworkInterface` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkInterface` deleted or renamed its instance variable `workload_type`
- Model `NetworkInterface` deleted or renamed its instance variable `nic_type`
- Model `NetworkInterface` deleted or renamed its instance variable `private_link_service`
- Model `NetworkInterface` deleted or renamed its instance variable `migration_phase`
- Model `NetworkInterface` deleted or renamed its instance variable `auxiliary_mode`
- Model `NetworkInterface` deleted or renamed its instance variable `auxiliary_sku`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `gateway_load_balancer`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `virtual_network_taps`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `application_gateway_backend_address_pools`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `load_balancer_backend_address_pools`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `load_balancer_inbound_nat_rules`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `private_ip_address_prefix_length`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `private_ip_address_version`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `primary`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `application_security_groups`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkInterfaceIPConfiguration` deleted or renamed its instance variable `private_link_connection_properties`
- Model `NetworkInterfaceTapConfiguration` deleted or renamed its instance variable `virtual_network_tap`
- Model `NetworkInterfaceTapConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkManager` deleted or renamed its instance variable `description`
- Model `NetworkManager` deleted or renamed its instance variable `network_manager_scopes`
- Model `NetworkManager` deleted or renamed its instance variable `network_manager_scope_accesses`
- Model `NetworkManager` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkManager` deleted or renamed its instance variable `resource_guid`
- Model `NetworkManagerConnection` deleted or renamed its instance variable `network_manager_id`
- Model `NetworkManagerConnection` deleted or renamed its instance variable `connection_state`
- Model `NetworkManagerConnection` deleted or renamed its instance variable `description`
- Model `NetworkManagerRoutingConfiguration` deleted or renamed its instance variable `description`
- Model `NetworkManagerRoutingConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkManagerRoutingConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `NetworkManagerRoutingConfiguration` deleted or renamed its instance variable `route_table_usage_mode`
- Model `NetworkProfile` deleted or renamed its instance variable `container_network_interfaces`
- Model `NetworkProfile` deleted or renamed its instance variable `container_network_interface_configurations`
- Model `NetworkProfile` deleted or renamed its instance variable `resource_guid`
- Model `NetworkProfile` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `flush_connection`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `security_rules`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `default_security_rules`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `network_interfaces`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `subnets`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `flow_logs`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `resource_guid`
- Model `NetworkSecurityGroup` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkSecurityPerimeter` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkSecurityPerimeter` deleted or renamed its instance variable `perimeter_guid`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `nva_sku`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `address_prefix`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `boot_strap_configuration_blobs`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `virtual_hub`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `cloud_init_configuration_blobs`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `cloud_init_configuration`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `virtual_appliance_asn`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `ssh_public_key`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `virtual_appliance_nics`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `network_profile`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `additional_nics`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `internet_ingress_public_ips`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `virtual_appliance_sites`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `virtual_appliance_connections`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `inbound_security_rules`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `deployment_type`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `delegation`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `partner_managed_resource`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `nva_interface_configurations`
- Model `NetworkVirtualAppliance` deleted or renamed its instance variable `private_ip_address`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `name_properties_name`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `provisioning_state`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `asn`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `tunnel_identifier`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `bgp_peer_address`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `enable_internet_security`
- Model `NetworkVirtualApplianceConnection` deleted or renamed its instance variable `routing_configuration`
- Model `NetworkVirtualApplianceSku` deleted or renamed its instance variable `vendor`
- Model `NetworkVirtualApplianceSku` deleted or renamed its instance variable `available_versions`
- Model `NetworkVirtualApplianceSku` deleted or renamed its instance variable `available_scale_units`
- Model `NetworkWatcher` deleted or renamed its instance variable `provisioning_state`
- Model `NspAccessRule` deleted or renamed its instance variable `provisioning_state`
- Model `NspAccessRule` deleted or renamed its instance variable `direction`
- Model `NspAccessRule` deleted or renamed its instance variable `address_prefixes`
- Model `NspAccessRule` deleted or renamed its instance variable `fully_qualified_domain_names`
- Model `NspAccessRule` deleted or renamed its instance variable `subscriptions`
- Model `NspAccessRule` deleted or renamed its instance variable `network_security_perimeters`
- Model `NspAccessRule` deleted or renamed its instance variable `email_addresses`
- Model `NspAccessRule` deleted or renamed its instance variable `phone_numbers`
- Model `NspAccessRule` deleted or renamed its instance variable `service_tags`
- Model `NspAssociation` deleted or renamed its instance variable `provisioning_state`
- Model `NspAssociation` deleted or renamed its instance variable `private_link_resource`
- Model `NspAssociation` deleted or renamed its instance variable `profile`
- Model `NspAssociation` deleted or renamed its instance variable `access_mode`
- Model `NspAssociation` deleted or renamed its instance variable `has_provisioning_issues`
- Model `NspLink` deleted or renamed its instance variable `provisioning_state`
- Model `NspLink` deleted or renamed its instance variable `auto_approved_remote_perimeter_resource_id`
- Model `NspLink` deleted or renamed its instance variable `remote_perimeter_guid`
- Model `NspLink` deleted or renamed its instance variable `remote_perimeter_location`
- Model `NspLink` deleted or renamed its instance variable `local_inbound_profiles`
- Model `NspLink` deleted or renamed its instance variable `local_outbound_profiles`
- Model `NspLink` deleted or renamed its instance variable `remote_inbound_profiles`
- Model `NspLink` deleted or renamed its instance variable `remote_outbound_profiles`
- Model `NspLink` deleted or renamed its instance variable `description`
- Model `NspLink` deleted or renamed its instance variable `status`
- Model `NspLinkReference` deleted or renamed its instance variable `provisioning_state`
- Model `NspLinkReference` deleted or renamed its instance variable `remote_perimeter_resource_id`
- Model `NspLinkReference` deleted or renamed its instance variable `remote_perimeter_guid`
- Model `NspLinkReference` deleted or renamed its instance variable `remote_perimeter_location`
- Model `NspLinkReference` deleted or renamed its instance variable `local_inbound_profiles`
- Model `NspLinkReference` deleted or renamed its instance variable `local_outbound_profiles`
- Model `NspLinkReference` deleted or renamed its instance variable `remote_inbound_profiles`
- Model `NspLinkReference` deleted or renamed its instance variable `remote_outbound_profiles`
- Model `NspLinkReference` deleted or renamed its instance variable `description`
- Model `NspLinkReference` deleted or renamed its instance variable `status`
- Model `NspLoggingConfiguration` deleted or renamed its instance variable `enabled_log_categories`
- Model `NspLoggingConfiguration` deleted or renamed its instance variable `version`
- Model `NspProfile` deleted or renamed its instance variable `access_rules_version`
- Model `NspProfile` deleted or renamed its instance variable `diagnostic_settings_version`
- Model `Operation` deleted or renamed its instance variable `service_specification`
- Model `OperationStatusResult` deleted or renamed its instance variable `resource_id`
- Model `OutboundRule` deleted or renamed its instance variable `allocated_outbound_ports`
- Model `OutboundRule` deleted or renamed its instance variable `frontend_ip_configurations`
- Model `OutboundRule` deleted or renamed its instance variable `backend_address_pool`
- Model `OutboundRule` deleted or renamed its instance variable `provisioning_state`
- Model `OutboundRule` deleted or renamed its instance variable `protocol`
- Model `OutboundRule` deleted or renamed its instance variable `enable_tcp_reset`
- Model `OutboundRule` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `vpn_client_address_pool`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `routing_configuration`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `enable_internet_security`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `configuration_policy_group_associations`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `previous_configuration_policy_group_associations`
- Model `P2SConnectionConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `P2SVpnGateway` deleted or renamed its instance variable `virtual_hub`
- Model `P2SVpnGateway` deleted or renamed its instance variable `p2_s_connection_configurations`
- Model `P2SVpnGateway` deleted or renamed its instance variable `provisioning_state`
- Model `P2SVpnGateway` deleted or renamed its instance variable `vpn_gateway_scale_unit`
- Model `P2SVpnGateway` deleted or renamed its instance variable `vpn_server_configuration`
- Model `P2SVpnGateway` deleted or renamed its instance variable `vpn_client_connection_health`
- Model `P2SVpnGateway` deleted or renamed its instance variable `custom_dns_servers`
- Model `P2SVpnGateway` deleted or renamed its instance variable `is_routing_preference_internet`
- Model `PacketCapture` deleted or renamed its instance variable `target`
- Model `PacketCapture` deleted or renamed its instance variable `scope`
- Model `PacketCapture` deleted or renamed its instance variable `target_type`
- Model `PacketCapture` deleted or renamed its instance variable `bytes_to_capture_per_packet`
- Model `PacketCapture` deleted or renamed its instance variable `total_bytes_per_session`
- Model `PacketCapture` deleted or renamed its instance variable `time_limit_in_seconds`
- Model `PacketCapture` deleted or renamed its instance variable `storage_location`
- Model `PacketCapture` deleted or renamed its instance variable `filters`
- Model `PacketCapture` deleted or renamed its instance variable `continuous_capture`
- Model `PacketCapture` deleted or renamed its instance variable `capture_settings`
- Model `PacketCaptureResult` deleted or renamed its instance variable `target`
- Model `PacketCaptureResult` deleted or renamed its instance variable `scope`
- Model `PacketCaptureResult` deleted or renamed its instance variable `target_type`
- Model `PacketCaptureResult` deleted or renamed its instance variable `bytes_to_capture_per_packet`
- Model `PacketCaptureResult` deleted or renamed its instance variable `total_bytes_per_session`
- Model `PacketCaptureResult` deleted or renamed its instance variable `time_limit_in_seconds`
- Model `PacketCaptureResult` deleted or renamed its instance variable `storage_location`
- Model `PacketCaptureResult` deleted or renamed its instance variable `filters`
- Model `PacketCaptureResult` deleted or renamed its instance variable `continuous_capture`
- Model `PacketCaptureResult` deleted or renamed its instance variable `capture_settings`
- Model `PacketCaptureResult` deleted or renamed its instance variable `provisioning_state`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `express_route_circuit_peering`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `peer_express_route_circuit_peering`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `address_prefix`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `circuit_connection_status`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `connection_name`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `auth_resource_guid`
- Model `PeerExpressRouteCircuitConnection` deleted or renamed its instance variable `provisioning_state`
- Model `PerimeterAssociableResource` deleted or renamed its instance variable `display_name`
- Model `PerimeterAssociableResource` deleted or renamed its instance variable `resource_type`
- Model `PerimeterAssociableResource` deleted or renamed its instance variable `public_dns_zones`
- Model `PrivateDnsZoneConfig` deleted or renamed its instance variable `private_dns_zone_id`
- Model `PrivateDnsZoneConfig` deleted or renamed its instance variable `record_sets`
- Model `PrivateDnsZoneGroup` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateDnsZoneGroup` deleted or renamed its instance variable `private_dns_zone_configs`
- Model `PrivateEndpoint` deleted or renamed its instance variable `subnet`
- Model `PrivateEndpoint` deleted or renamed its instance variable `network_interfaces`
- Model `PrivateEndpoint` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateEndpoint` deleted or renamed its instance variable `ip_version_type`
- Model `PrivateEndpoint` deleted or renamed its instance variable `private_link_service_connections`
- Model `PrivateEndpoint` deleted or renamed its instance variable `manual_private_link_service_connections`
- Model `PrivateEndpoint` deleted or renamed its instance variable `custom_dns_configs`
- Model `PrivateEndpoint` deleted or renamed its instance variable `application_security_groups`
- Model `PrivateEndpoint` deleted or renamed its instance variable `ip_configurations`
- Model `PrivateEndpoint` deleted or renamed its instance variable `custom_network_interface_name`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `private_endpoint`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `private_link_service_connection_state`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `link_identifier`
- Model `PrivateEndpointConnection` deleted or renamed its instance variable `private_endpoint_location`
- Model `PrivateEndpointIPConfiguration` deleted or renamed its instance variable `group_id`
- Model `PrivateEndpointIPConfiguration` deleted or renamed its instance variable `member_name`
- Model `PrivateEndpointIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `PrivateLinkService` deleted or renamed its instance variable `load_balancer_frontend_ip_configurations`
- Model `PrivateLinkService` deleted or renamed its instance variable `ip_configurations`
- Model `PrivateLinkService` deleted or renamed its instance variable `destination_ip_address`
- Model `PrivateLinkService` deleted or renamed its instance variable `access_mode`
- Model `PrivateLinkService` deleted or renamed its instance variable `network_interfaces`
- Model `PrivateLinkService` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateLinkService` deleted or renamed its instance variable `private_endpoint_connections`
- Model `PrivateLinkService` deleted or renamed its instance variable `visibility`
- Model `PrivateLinkService` deleted or renamed its instance variable `auto_approval`
- Model `PrivateLinkService` deleted or renamed its instance variable `fqdns`
- Model `PrivateLinkService` deleted or renamed its instance variable `alias`
- Model `PrivateLinkService` deleted or renamed its instance variable `enable_proxy_protocol`
- Model `PrivateLinkServiceConnection` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateLinkServiceConnection` deleted or renamed its instance variable `private_link_service_id`
- Model `PrivateLinkServiceConnection` deleted or renamed its instance variable `group_ids`
- Model `PrivateLinkServiceConnection` deleted or renamed its instance variable `request_message`
- Model `PrivateLinkServiceConnection` deleted or renamed its instance variable `private_link_service_connection_state`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `subnet`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `primary`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `PrivateLinkServiceIpConfiguration` deleted or renamed its instance variable `private_ip_address_version`
- Model `Probe` deleted or renamed its instance variable `load_balancing_rules`
- Model `Probe` deleted or renamed its instance variable `protocol`
- Model `Probe` deleted or renamed its instance variable `port`
- Model `Probe` deleted or renamed its instance variable `interval_in_seconds`
- Model `Probe` deleted or renamed its instance variable `no_healthy_backends_behavior`
- Model `Probe` deleted or renamed its instance variable `number_of_probes`
- Model `Probe` deleted or renamed its instance variable `probe_threshold`
- Model `Probe` deleted or renamed its instance variable `request_path`
- Model `Probe` deleted or renamed its instance variable `provisioning_state`
- Model `ProxyResource` deleted or renamed its instance variable `etag`
- Model `ProxyResourceAutoGenerated` deleted or renamed its instance variable `system_data`
- Model `PublicIPAddress` deleted or renamed its instance variable `public_ip_allocation_method`
- Model `PublicIPAddress` deleted or renamed its instance variable `public_ip_address_version`
- Model `PublicIPAddress` deleted or renamed its instance variable `ip_configuration`
- Model `PublicIPAddress` deleted or renamed its instance variable `dns_settings`
- Model `PublicIPAddress` deleted or renamed its instance variable `ddos_settings`
- Model `PublicIPAddress` deleted or renamed its instance variable `ip_tags`
- Model `PublicIPAddress` deleted or renamed its instance variable `ip_address`
- Model `PublicIPAddress` deleted or renamed its instance variable `public_ip_prefix`
- Model `PublicIPAddress` deleted or renamed its instance variable `idle_timeout_in_minutes`
- Model `PublicIPAddress` deleted or renamed its instance variable `resource_guid`
- Model `PublicIPAddress` deleted or renamed its instance variable `provisioning_state`
- Model `PublicIPAddress` deleted or renamed its instance variable `service_public_ip_address`
- Model `PublicIPAddress` deleted or renamed its instance variable `nat_gateway`
- Model `PublicIPAddress` deleted or renamed its instance variable `migration_phase`
- Model `PublicIPAddress` deleted or renamed its instance variable `linked_public_ip_address`
- Model `PublicIPAddress` deleted or renamed its instance variable `delete_option`
- Model `PublicIPPrefix` deleted or renamed its instance variable `public_ip_address_version`
- Model `PublicIPPrefix` deleted or renamed its instance variable `ip_tags`
- Model `PublicIPPrefix` deleted or renamed its instance variable `prefix_length`
- Model `PublicIPPrefix` deleted or renamed its instance variable `ip_prefix`
- Model `PublicIPPrefix` deleted or renamed its instance variable `public_ip_addresses`
- Model `PublicIPPrefix` deleted or renamed its instance variable `load_balancer_frontend_ip_configuration`
- Model `PublicIPPrefix` deleted or renamed its instance variable `custom_ip_prefix`
- Model `PublicIPPrefix` deleted or renamed its instance variable `resource_guid`
- Model `PublicIPPrefix` deleted or renamed its instance variable `provisioning_state`
- Model `PublicIPPrefix` deleted or renamed its instance variable `nat_gateway`
- Model `Resource` deleted or renamed its instance variable `location`
- Model `Resource` deleted or renamed its instance variable `tags`
- Model `ResourceNavigationLink` deleted or renamed its instance variable `linked_resource_type`
- Model `ResourceNavigationLink` deleted or renamed its instance variable `link`
- Model `ResourceNavigationLink` deleted or renamed its instance variable `provisioning_state`
- Model `Route` deleted or renamed its instance variable `address_prefix`
- Model `Route` deleted or renamed its instance variable `next_hop_type`
- Model `Route` deleted or renamed its instance variable `next_hop_ip_address`
- Model `Route` deleted or renamed its instance variable `provisioning_state`
- Model `Route` deleted or renamed its instance variable `has_bgp_override`
- Model `RouteFilter` deleted or renamed its instance variable `rules`
- Model `RouteFilter` deleted or renamed its instance variable `peerings`
- Model `RouteFilter` deleted or renamed its instance variable `ipv6_peerings`
- Model `RouteFilter` deleted or renamed its instance variable `provisioning_state`
- Model `RouteFilterRule` deleted or renamed its instance variable `access`
- Model `RouteFilterRule` deleted or renamed its instance variable `route_filter_rule_type`
- Model `RouteFilterRule` deleted or renamed its instance variable `communities`
- Model `RouteFilterRule` deleted or renamed its instance variable `provisioning_state`
- Model `RouteMap` deleted or renamed its instance variable `associated_inbound_connections`
- Model `RouteMap` deleted or renamed its instance variable `associated_outbound_connections`
- Model `RouteMap` deleted or renamed its instance variable `rules`
- Model `RouteMap` deleted or renamed its instance variable `provisioning_state`
- Model `RouteTable` deleted or renamed its instance variable `routes`
- Model `RouteTable` deleted or renamed its instance variable `subnets`
- Model `RouteTable` deleted or renamed its instance variable `disable_bgp_route_propagation`
- Model `RouteTable` deleted or renamed its instance variable `provisioning_state`
- Model `RouteTable` deleted or renamed its instance variable `resource_guid`
- Model `RoutingIntent` deleted or renamed its instance variable `routing_policies`
- Model `RoutingIntent` deleted or renamed its instance variable `provisioning_state`
- Model `RoutingRule` deleted or renamed its instance variable `description`
- Model `RoutingRule` deleted or renamed its instance variable `provisioning_state`
- Model `RoutingRule` deleted or renamed its instance variable `resource_guid`
- Model `RoutingRule` deleted or renamed its instance variable `destination`
- Model `RoutingRule` deleted or renamed its instance variable `next_hop`
- Model `RoutingRuleCollection` deleted or renamed its instance variable `description`
- Model `RoutingRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `RoutingRuleCollection` deleted or renamed its instance variable `resource_guid`
- Model `RoutingRuleCollection` deleted or renamed its instance variable `applies_to`
- Model `RoutingRuleCollection` deleted or renamed its instance variable `disable_bgp_route_propagation`
- Model `ScopeConnection` deleted or renamed its instance variable `tenant_id`
- Model `ScopeConnection` deleted or renamed its instance variable `resource_id`
- Model `ScopeConnection` deleted or renamed its instance variable `connection_state`
- Model `ScopeConnection` deleted or renamed its instance variable `description`
- Model `SecurityAdminConfiguration` deleted or renamed its instance variable `description`
- Model `SecurityAdminConfiguration` deleted or renamed its instance variable `apply_on_network_intent_policy_based_services`
- Model `SecurityAdminConfiguration` deleted or renamed its instance variable `network_group_address_space_aggregation_option`
- Model `SecurityAdminConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityAdminConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `SecurityPartnerProvider` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityPartnerProvider` deleted or renamed its instance variable `security_provider_name`
- Model `SecurityPartnerProvider` deleted or renamed its instance variable `connection_status`
- Model `SecurityPartnerProvider` deleted or renamed its instance variable `virtual_hub`
- Model `SecurityRule` deleted or renamed its instance variable `description`
- Model `SecurityRule` deleted or renamed its instance variable `protocol`
- Model `SecurityRule` deleted or renamed its instance variable `source_port_range`
- Model `SecurityRule` deleted or renamed its instance variable `destination_port_range`
- Model `SecurityRule` deleted or renamed its instance variable `source_address_prefix`
- Model `SecurityRule` deleted or renamed its instance variable `source_address_prefixes`
- Model `SecurityRule` deleted or renamed its instance variable `source_application_security_groups`
- Model `SecurityRule` deleted or renamed its instance variable `destination_address_prefix`
- Model `SecurityRule` deleted or renamed its instance variable `destination_address_prefixes`
- Model `SecurityRule` deleted or renamed its instance variable `destination_application_security_groups`
- Model `SecurityRule` deleted or renamed its instance variable `source_port_ranges`
- Model `SecurityRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `SecurityRule` deleted or renamed its instance variable `access`
- Model `SecurityRule` deleted or renamed its instance variable `priority`
- Model `SecurityRule` deleted or renamed its instance variable `direction`
- Model `SecurityRule` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityUserConfiguration` deleted or renamed its instance variable `description`
- Model `SecurityUserConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityUserConfiguration` deleted or renamed its instance variable `resource_guid`
- Model `SecurityUserRule` deleted or renamed its instance variable `description`
- Model `SecurityUserRule` deleted or renamed its instance variable `protocol`
- Model `SecurityUserRule` deleted or renamed its instance variable `sources`
- Model `SecurityUserRule` deleted or renamed its instance variable `destinations`
- Model `SecurityUserRule` deleted or renamed its instance variable `source_port_ranges`
- Model `SecurityUserRule` deleted or renamed its instance variable `destination_port_ranges`
- Model `SecurityUserRule` deleted or renamed its instance variable `direction`
- Model `SecurityUserRule` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityUserRule` deleted or renamed its instance variable `resource_guid`
- Model `SecurityUserRuleCollection` deleted or renamed its instance variable `description`
- Model `SecurityUserRuleCollection` deleted or renamed its instance variable `applies_to_groups`
- Model `SecurityUserRuleCollection` deleted or renamed its instance variable `provisioning_state`
- Model `SecurityUserRuleCollection` deleted or renamed its instance variable `resource_guid`
- Model `ServiceAssociationLink` deleted or renamed its instance variable `linked_resource_type`
- Model `ServiceAssociationLink` deleted or renamed its instance variable `link`
- Model `ServiceAssociationLink` deleted or renamed its instance variable `provisioning_state`
- Model `ServiceAssociationLink` deleted or renamed its instance variable `allow_delete`
- Model `ServiceAssociationLink` deleted or renamed its instance variable `locations`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `service_endpoint_policy_definitions`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `subnets`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `resource_guid`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `provisioning_state`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `service_alias`
- Model `ServiceEndpointPolicy` deleted or renamed its instance variable `contextual_service_endpoint_policies`
- Model `ServiceEndpointPolicyDefinition` deleted or renamed its instance variable `description`
- Model `ServiceEndpointPolicyDefinition` deleted or renamed its instance variable `service`
- Model `ServiceEndpointPolicyDefinition` deleted or renamed its instance variable `service_resources`
- Model `ServiceEndpointPolicyDefinition` deleted or renamed its instance variable `provisioning_state`
- Model `ServiceGateway` deleted or renamed its instance variable `virtual_network`
- Model `ServiceGateway` deleted or renamed its instance variable `route_target_address`
- Model `ServiceGateway` deleted or renamed its instance variable `route_target_address_v6`
- Model `ServiceGateway` deleted or renamed its instance variable `resource_guid`
- Model `ServiceGateway` deleted or renamed its instance variable `provisioning_state`
- Model `ServiceGatewayService` deleted or renamed its instance variable `service_type`
- Model `ServiceGatewayService` deleted or renamed its instance variable `is_default`
- Model `ServiceGatewayService` deleted or renamed its instance variable `load_balancer_backend_pools`
- Model `ServiceGatewayService` deleted or renamed its instance variable `public_nat_gateway_id`
- Model `ServiceTagsListResult` deleted or renamed its instance variable `values`
- Model `StaticMember` deleted or renamed its instance variable `resource_id`
- Model `StaticMember` deleted or renamed its instance variable `region`
- Model `StaticMember` deleted or renamed its instance variable `provisioning_state`
- Model `Subnet` deleted or renamed its instance variable `address_prefix`
- Model `Subnet` deleted or renamed its instance variable `address_prefixes`
- Model `Subnet` deleted or renamed its instance variable `network_security_group`
- Model `Subnet` deleted or renamed its instance variable `route_table`
- Model `Subnet` deleted or renamed its instance variable `nat_gateway`
- Model `Subnet` deleted or renamed its instance variable `service_endpoints`
- Model `Subnet` deleted or renamed its instance variable `service_endpoint_policies`
- Model `Subnet` deleted or renamed its instance variable `private_endpoints`
- Model `Subnet` deleted or renamed its instance variable `ip_configurations`
- Model `Subnet` deleted or renamed its instance variable `ip_configuration_profiles`
- Model `Subnet` deleted or renamed its instance variable `ip_allocations`
- Model `Subnet` deleted or renamed its instance variable `resource_navigation_links`
- Model `Subnet` deleted or renamed its instance variable `service_association_links`
- Model `Subnet` deleted or renamed its instance variable `delegations`
- Model `Subnet` deleted or renamed its instance variable `purpose`
- Model `Subnet` deleted or renamed its instance variable `provisioning_state`
- Model `Subnet` deleted or renamed its instance variable `private_endpoint_network_policies`
- Model `Subnet` deleted or renamed its instance variable `private_link_service_network_policies`
- Model `Subnet` deleted or renamed its instance variable `application_gateway_ip_configurations`
- Model `Subnet` deleted or renamed its instance variable `sharing_scope`
- Model `Subnet` deleted or renamed its instance variable `default_outbound_access`
- Model `Subnet` deleted or renamed its instance variable `ipam_pool_prefix_allocations`
- Model `Subnet` deleted or renamed its instance variable `service_gateway`
- Model `TroubleshootingParameters` deleted or renamed its instance variable `storage_id`
- Model `TroubleshootingParameters` deleted or renamed its instance variable `storage_path`
- Model `VirtualApplianceSite` deleted or renamed its instance variable `address_prefix`
- Model `VirtualApplianceSite` deleted or renamed its instance variable `o365_policy`
- Model `VirtualApplianceSite` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualHub` deleted or renamed its instance variable `virtual_wan`
- Model `VirtualHub` deleted or renamed its instance variable `vpn_gateway`
- Model `VirtualHub` deleted or renamed its instance variable `p2_s_vpn_gateway`
- Model `VirtualHub` deleted or renamed its instance variable `express_route_gateway`
- Model `VirtualHub` deleted or renamed its instance variable `azure_firewall`
- Model `VirtualHub` deleted or renamed its instance variable `security_partner_provider`
- Model `VirtualHub` deleted or renamed its instance variable `address_prefix`
- Model `VirtualHub` deleted or renamed its instance variable `route_table`
- Model `VirtualHub` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualHub` deleted or renamed its instance variable `security_provider_name`
- Model `VirtualHub` deleted or renamed its instance variable `virtual_hub_route_table_v2_s`
- Model `VirtualHub` deleted or renamed its instance variable `sku`
- Model `VirtualHub` deleted or renamed its instance variable `routing_state`
- Model `VirtualHub` deleted or renamed its instance variable `bgp_connections`
- Model `VirtualHub` deleted or renamed its instance variable `ip_configurations`
- Model `VirtualHub` deleted or renamed its instance variable `route_maps`
- Model `VirtualHub` deleted or renamed its instance variable `virtual_router_asn`
- Model `VirtualHub` deleted or renamed its instance variable `virtual_router_ips`
- Model `VirtualHub` deleted or renamed its instance variable `allow_branch_to_branch_traffic`
- Model `VirtualHub` deleted or renamed its instance variable `preferred_routing_gateway`
- Model `VirtualHub` deleted or renamed its instance variable `hub_routing_preference`
- Model `VirtualHub` deleted or renamed its instance variable `virtual_router_auto_scale_configuration`
- Model `VirtualHubRouteTableV2` deleted or renamed its instance variable `routes`
- Model `VirtualHubRouteTableV2` deleted or renamed its instance variable `attached_connections`
- Model `VirtualHubRouteTableV2` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetwork` deleted or renamed its instance variable `address_space`
- Model `VirtualNetwork` deleted or renamed its instance variable `dhcp_options`
- Model `VirtualNetwork` deleted or renamed its instance variable `flow_timeout_in_minutes`
- Model `VirtualNetwork` deleted or renamed its instance variable `subnets`
- Model `VirtualNetwork` deleted or renamed its instance variable `virtual_network_peerings`
- Model `VirtualNetwork` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetwork` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetwork` deleted or renamed its instance variable `enable_ddos_protection`
- Model `VirtualNetwork` deleted or renamed its instance variable `enable_vm_protection`
- Model `VirtualNetwork` deleted or renamed its instance variable `ddos_protection_plan`
- Model `VirtualNetwork` deleted or renamed its instance variable `bgp_communities`
- Model `VirtualNetwork` deleted or renamed its instance variable `encryption`
- Model `VirtualNetwork` deleted or renamed its instance variable `ip_allocations`
- Model `VirtualNetwork` deleted or renamed its instance variable `flow_logs`
- Model `VirtualNetwork` deleted or renamed its instance variable `private_endpoint_v_net_policies`
- Model `VirtualNetwork` deleted or renamed its instance variable `default_public_nat_gateway`
- Model `VirtualNetworkAppliance` deleted or renamed its instance variable `bandwidth_in_gbps`
- Model `VirtualNetworkAppliance` deleted or renamed its instance variable `ip_configurations`
- Model `VirtualNetworkAppliance` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkAppliance` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkAppliance` deleted or renamed its instance variable `subnet`
- Model `VirtualNetworkApplianceIpConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `VirtualNetworkApplianceIpConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `VirtualNetworkApplianceIpConfiguration` deleted or renamed its instance variable `primary`
- Model `VirtualNetworkApplianceIpConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkApplianceIpConfiguration` deleted or renamed its instance variable `private_ip_address_version`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `auto_scale_configuration`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `ip_configurations`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `gateway_type`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `vpn_type`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `vpn_gateway_generation`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `enable_bgp`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `enable_private_ip_address`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `virtual_network_gateway_migration_status`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `active`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `enable_high_bandwidth_vpn_gateway`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `disable_ip_sec_replay_protection`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `gateway_default_site`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `sku`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `vpn_client_configuration`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `virtual_network_gateway_policy_groups`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `bgp_settings`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `custom_routes`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `enable_dns_forwarding`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `inbound_dns_forwarding_endpoint`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `v_net_extended_location_resource_id`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `nat_rules`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `enable_bgp_route_translation_for_nat`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `allow_virtual_wan_traffic`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `allow_remote_vnet_traffic`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `admin_state`
- Model `VirtualNetworkGateway` deleted or renamed its instance variable `resiliency_model`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `authorization_key`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `virtual_network_gateway1`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `virtual_network_gateway2`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `local_network_gateway2`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `ingress_nat_rules`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `egress_nat_rules`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `connection_type`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `connection_protocol`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `routing_weight`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `dpd_timeout_seconds`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `connection_mode`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `tunnel_properties`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `shared_key`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `connection_status`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `tunnel_connection_status`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `egress_bytes_transferred`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `ingress_bytes_transferred`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `peer`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `enable_bgp`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `gateway_custom_bgp_ip_addresses`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `use_local_azure_ip_address`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `use_policy_based_traffic_selectors`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `ipsec_policies`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `traffic_selector_policies`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `express_route_gateway_bypass`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `enable_private_link_fast_path`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `authentication_type`
- Model `VirtualNetworkGatewayConnection` deleted or renamed its instance variable `certificate_authentication`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `authorization_key`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `virtual_network_gateway1`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `virtual_network_gateway2`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `local_network_gateway2`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `connection_type`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `connection_protocol`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `routing_weight`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `connection_mode`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `shared_key`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `connection_status`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `tunnel_connection_status`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `egress_bytes_transferred`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `ingress_bytes_transferred`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `peer`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `enable_bgp`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `gateway_custom_bgp_ip_addresses`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `use_policy_based_traffic_selectors`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `ipsec_policies`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `traffic_selector_policies`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `express_route_gateway_bypass`
- Model `VirtualNetworkGatewayConnectionListEntity` deleted or renamed its instance variable `enable_private_link_fast_path`
- Model `VirtualNetworkGatewayIPConfiguration` deleted or renamed its instance variable `private_ip_allocation_method`
- Model `VirtualNetworkGatewayIPConfiguration` deleted or renamed its instance variable `subnet`
- Model `VirtualNetworkGatewayIPConfiguration` deleted or renamed its instance variable `public_ip_address`
- Model `VirtualNetworkGatewayIPConfiguration` deleted or renamed its instance variable `private_ip_address`
- Model `VirtualNetworkGatewayIPConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `type_properties_type`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `mode`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `internal_mappings`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `external_mappings`
- Model `VirtualNetworkGatewayNatRule` deleted or renamed its instance variable `ip_configuration_id`
- Model `VirtualNetworkGatewayPolicyGroup` deleted or renamed its instance variable `is_default`
- Model `VirtualNetworkGatewayPolicyGroup` deleted or renamed its instance variable `priority`
- Model `VirtualNetworkGatewayPolicyGroup` deleted or renamed its instance variable `policy_members`
- Model `VirtualNetworkGatewayPolicyGroup` deleted or renamed its instance variable `vng_client_connection_configurations`
- Model `VirtualNetworkGatewayPolicyGroup` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `allow_virtual_network_access`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `allow_forwarded_traffic`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `allow_gateway_transit`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `use_remote_gateways`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_virtual_network`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `local_address_space`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `local_virtual_network_address_space`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_address_space`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_virtual_network_address_space`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_bgp_communities`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_virtual_network_encryption`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `peering_state`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `peering_sync_level`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `do_not_verify_remote_gateways`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `peer_complete_vnets`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `enable_only_i_pv6_peering`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `local_subnet_names`
- Model `VirtualNetworkPeering` deleted or renamed its instance variable `remote_subnet_names`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `network_interface_tap_configurations`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `resource_guid`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `destination_network_interface_ip_configuration`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `destination_load_balancer_front_end_ip_configuration`
- Model `VirtualNetworkTap` deleted or renamed its instance variable `destination_port`
- Model `VirtualRouter` deleted or renamed its instance variable `virtual_router_asn`
- Model `VirtualRouter` deleted or renamed its instance variable `virtual_router_ips`
- Model `VirtualRouter` deleted or renamed its instance variable `hosted_subnet`
- Model `VirtualRouter` deleted or renamed its instance variable `hosted_gateway`
- Model `VirtualRouter` deleted or renamed its instance variable `peerings`
- Model `VirtualRouter` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualRouterPeering` deleted or renamed its instance variable `peer_asn`
- Model `VirtualRouterPeering` deleted or renamed its instance variable `peer_ip`
- Model `VirtualRouterPeering` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualWAN` deleted or renamed its instance variable `disable_vpn_encryption`
- Model `VirtualWAN` deleted or renamed its instance variable `virtual_hubs`
- Model `VirtualWAN` deleted or renamed its instance variable `vpn_sites`
- Model `VirtualWAN` deleted or renamed its instance variable `allow_branch_to_branch_traffic`
- Model `VirtualWAN` deleted or renamed its instance variable `allow_vnet_to_vnet_traffic`
- Model `VirtualWAN` deleted or renamed its instance variable `office365_local_breakout_category`
- Model `VirtualWAN` deleted or renamed its instance variable `provisioning_state`
- Model `VirtualWAN` deleted or renamed its instance variable `type_properties_type`
- Model `VngClientConnectionConfiguration` deleted or renamed its instance variable `vpn_client_address_pool`
- Model `VngClientConnectionConfiguration` deleted or renamed its instance variable `virtual_network_gateway_policy_groups`
- Model `VngClientConnectionConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `VpnClientRevokedCertificate` deleted or renamed its instance variable `thumbprint`
- Model `VpnClientRevokedCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `VpnClientRootCertificate` deleted or renamed its instance variable `public_cert_data`
- Model `VpnClientRootCertificate` deleted or renamed its instance variable `provisioning_state`
- Model `VpnConnection` deleted or renamed its instance variable `remote_vpn_site`
- Model `VpnConnection` deleted or renamed its instance variable `routing_weight`
- Model `VpnConnection` deleted or renamed its instance variable `dpd_timeout_seconds`
- Model `VpnConnection` deleted or renamed its instance variable `connection_status`
- Model `VpnConnection` deleted or renamed its instance variable `vpn_connection_protocol_type`
- Model `VpnConnection` deleted or renamed its instance variable `ingress_bytes_transferred`
- Model `VpnConnection` deleted or renamed its instance variable `egress_bytes_transferred`
- Model `VpnConnection` deleted or renamed its instance variable `connection_bandwidth`
- Model `VpnConnection` deleted or renamed its instance variable `shared_key`
- Model `VpnConnection` deleted or renamed its instance variable `enable_bgp`
- Model `VpnConnection` deleted or renamed its instance variable `use_policy_based_traffic_selectors`
- Model `VpnConnection` deleted or renamed its instance variable `ipsec_policies`
- Model `VpnConnection` deleted or renamed its instance variable `traffic_selector_policies`
- Model `VpnConnection` deleted or renamed its instance variable `enable_rate_limiting`
- Model `VpnConnection` deleted or renamed its instance variable `enable_internet_security`
- Model `VpnConnection` deleted or renamed its instance variable `use_local_azure_ip_address`
- Model `VpnConnection` deleted or renamed its instance variable `provisioning_state`
- Model `VpnConnection` deleted or renamed its instance variable `vpn_link_connections`
- Model `VpnConnection` deleted or renamed its instance variable `routing_configuration`
- Model `VpnGateway` deleted or renamed its instance variable `virtual_hub`
- Model `VpnGateway` deleted or renamed its instance variable `connections`
- Model `VpnGateway` deleted or renamed its instance variable `bgp_settings`
- Model `VpnGateway` deleted or renamed its instance variable `provisioning_state`
- Model `VpnGateway` deleted or renamed its instance variable `vpn_gateway_scale_unit`
- Model `VpnGateway` deleted or renamed its instance variable `ip_configurations`
- Model `VpnGateway` deleted or renamed its instance variable `enable_bgp_route_translation_for_nat`
- Model `VpnGateway` deleted or renamed its instance variable `is_routing_preference_internet`
- Model `VpnGateway` deleted or renamed its instance variable `nat_rules`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `provisioning_state`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `type_properties_type`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `mode`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `internal_mappings`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `external_mappings`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `ip_configuration_id`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `egress_vpn_site_link_connections`
- Model `VpnGatewayNatRule` deleted or renamed its instance variable `ingress_vpn_site_link_connections`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `name_properties_name`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `vpn_protocols`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `vpn_authentication_types`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `vpn_client_root_certificates`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `vpn_client_revoked_certificates`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `radius_server_root_certificates`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `radius_client_root_certificates`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `vpn_client_ipsec_policies`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `radius_server_address`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `radius_server_secret`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `radius_servers`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `aad_authentication_parameters`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `provisioning_state`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `p2_s_vpn_gateways`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `configuration_policy_groups`
- Model `VpnServerConfiguration` deleted or renamed its instance variable `etag_properties_etag`
- Model `VpnServerConfigurationPolicyGroup` deleted or renamed its instance variable `is_default`
- Model `VpnServerConfigurationPolicyGroup` deleted or renamed its instance variable `priority`
- Model `VpnServerConfigurationPolicyGroup` deleted or renamed its instance variable `policy_members`
- Model `VpnServerConfigurationPolicyGroup` deleted or renamed its instance variable `p2_s_connection_configurations`
- Model `VpnServerConfigurationPolicyGroup` deleted or renamed its instance variable `provisioning_state`
- Model `VpnSite` deleted or renamed its instance variable `virtual_wan`
- Model `VpnSite` deleted or renamed its instance variable `device_properties`
- Model `VpnSite` deleted or renamed its instance variable `ip_address`
- Model `VpnSite` deleted or renamed its instance variable `site_key`
- Model `VpnSite` deleted or renamed its instance variable `address_space`
- Model `VpnSite` deleted or renamed its instance variable `bgp_properties`
- Model `VpnSite` deleted or renamed its instance variable `provisioning_state`
- Model `VpnSite` deleted or renamed its instance variable `is_security_site`
- Model `VpnSite` deleted or renamed its instance variable `vpn_site_links`
- Model `VpnSite` deleted or renamed its instance variable `o365_policy`
- Model `VpnSiteLink` deleted or renamed its instance variable `link_properties`
- Model `VpnSiteLink` deleted or renamed its instance variable `ip_address`
- Model `VpnSiteLink` deleted or renamed its instance variable `fqdn`
- Model `VpnSiteLink` deleted or renamed its instance variable `bgp_properties`
- Model `VpnSiteLink` deleted or renamed its instance variable `provisioning_state`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `vpn_site_link`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `routing_weight`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `vpn_link_connection_mode`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `connection_status`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `vpn_connection_protocol_type`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `ingress_bytes_transferred`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `egress_bytes_transferred`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `connection_bandwidth`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `shared_key`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `enable_bgp`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `vpn_gateway_custom_bgp_addresses`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `use_policy_based_traffic_selectors`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `ipsec_policies`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `enable_rate_limiting`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `use_local_azure_ip_address`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `provisioning_state`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `ingress_nat_rules`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `egress_nat_rules`
- Model `VpnSiteLinkConnection` deleted or renamed its instance variable `dpd_timeout_seconds`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `policy_settings`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `custom_rules`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `application_gateways`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `provisioning_state`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `resource_state`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `managed_rules`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `http_listeners`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `path_based_rules`
- Model `WebApplicationFirewallPolicy` deleted or renamed its instance variable `application_gateway_for_containers`

### Other Changes

  - Deleted model `ApplicationGatewayAvailableSslPredefinedPolicies`/`PatchRouteFilter`/`PatchRouteFilterRule`/`ApplicationGatewayBackendAddressPoolAutoGenerated`/`ApplicationGatewayIPConfigurationAutoGenerated`/`ApplicationGatewayWafDynamicManifestResultList`/`ApplicationSecurityGroupAutoGenerated`/`AutoApprovedPrivateLinkServicesResult`/`AvailableDelegationsResult`/`AvailablePrivateEndpointTypesResult`/`AvailableServiceAliasesResult`/`BackendAddressPoolAutoGenerated`/`BastionSessionDeleteResult`/`CloudErrorAutoGenerated`/`CloudErrorBodyAutoGenerated`/`ConnectionSharedKeyResultList`/`DelegationAutoGenerated`/`EffectiveRouteMapRouteList`/`ExpressRouteConnectionList`/`ExpressRouteCrossConnectionPeeringList`/`ExpressRouteGatewayList`/`FlowLogAutoGenerated`/`FlowLogFormatParametersAutoGenerated`/`FrontendIPConfigurationAutoGenerated`/`GetServiceGatewayAddressLocationsResult`/`GetServiceGatewayServicesResult`/`IPConfigurationAutoGenerated`/`IPConfigurationProfileAutoGenerated`/`InboundNatRuleAutoGenerated`/`IpamPoolList`/`ListHubRouteTablesResult`/`ListHubVirtualNetworkConnectionsResult`/`ListP2SVpnGatewaysResult`/`ListRouteMapsResult`/`ListRoutingIntentResult`/`ListVirtualHubBgpConnectionResults`/`ListVirtualHubIpConfigurationResults`/`ListVirtualHubRouteTableV2SResult`/`ListVirtualHubsResult`/`ListVirtualNetworkGatewayNatRulesResult`/`ListVirtualWANsResult`/`ListVpnConnectionsResult`/`ListVpnGatewayNatRulesResult`/`ListVpnGatewaysResult`/`ListVpnServerConfigurationPolicyGroupsResult`/`ListVpnServerConfigurationsResult`/`ListVpnSiteLinkConnectionsResult`/`ListVpnSiteLinksResult`/`ListVpnSitesResult`/`NatGatewayAutoGenerated`/`NetworkInterfaceAutoGenerated`/`NetworkInterfaceIPConfigurationAutoGenerated`/`NetworkInterfaceIPConfigurationListResultAutoGenerated`/`NetworkInterfaceListResultAutoGenerated`/`NetworkInterfaceTapConfigurationAutoGenerated`/`NetworkSecurityGroupAutoGenerated`/`NetworkVirtualApplianceConnectionList`/`PoolAssociationList`/`PrivateEndpointAutoGenerated`/`PrivateEndpointConnectionAutoGenerated`/`PrivateLinkServiceAutoGenerated`/`PrivateLinkServiceConnectionAutoGenerated`/`PrivateLinkServiceIpConfigurationAutoGenerated`/`PublicIPAddressAutoGenerated`/`PublicIPAddressListResultAutoGenerated`/`ResourceAutoGenerated2`/`ResourceNavigationLinkAutoGenerated`/`RouteAutoGenerated`/`RouteTableAutoGenerated`/`SecurityRuleAutoGenerated`/`ServiceAssociationLinkAutoGenerated`/`ServiceEndpointPolicyAutoGenerated`/`ServiceEndpointPolicyDefinitionAutoGenerated`/`ServiceEndpointPropertiesFormatAutoGenerated`/`SignaturesOverridesList`/`StaticCidrList`/`SubnetAutoGenerated`/`VirtualHubEffectiveRouteList`/`VirtualNetworkDdosProtectionStatusResult`/`VirtualNetworkGatewayListConnectionsResult`/`VirtualNetworkListUsageResult`/`VirtualNetworkTapAutoGenerated` which actually were not used by SDK users

# Release History

## 31.0.0 (2026-03-02)

### Features Added

  - Model ConnectionMonitorListResult has a new parameter next_link
  - Model NetworkWatcherListResult has a new parameter next_link
  - Model PacketCaptureListResult has a new parameter next_link

### Breaking Changes

  - Parameter location of model P2SVpnGateway is now required
  - Parameter location of model RouteFilter is now required
  - Parameter location of model VirtualHub is now required
  - Parameter location of model VirtualWAN is now required
  - Parameter location of model VpnGateway is now required
  - Parameter location of model VpnSite is now required
  - Parameter value of model AdminRuleCollectionListResult is now required
  - Parameter value of model AdminRuleListResult is now required
  - Parameter value of model ApplicationGatewayAvailableSslPredefinedPolicies is now required
  - Parameter value of model ApplicationGatewayListResult is now required
  - Parameter value of model ApplicationGatewayPrivateEndpointConnectionListResult is now required
  - Parameter value of model ApplicationGatewayPrivateLinkResourceListResult is now required
  - Parameter value of model ApplicationGatewayWafDynamicManifestResultList is now required
  - Parameter value of model ApplicationSecurityGroupListResult is now required
  - Parameter value of model AuthorizationListResult is now required
  - Parameter value of model AutoApprovedPrivateLinkServicesResult is now required
  - Parameter value of model AvailableDelegationsResult is now required
  - Parameter value of model AvailablePrivateEndpointTypesResult is now required
  - Parameter value of model AvailableServiceAliasesResult is now required
  - Parameter value of model AzureFirewallFqdnTagListResult is now required
  - Parameter value of model AzureFirewallListResult is now required
  - Parameter value of model AzureWebCategoryListResult is now required
  - Parameter value of model BastionActiveSessionListResult is now required
  - Parameter value of model BastionHostListResult is now required
  - Parameter value of model BastionSessionDeleteResult is now required
  - Parameter value of model BastionShareableLinkListResult is now required
  - Parameter value of model BgpServiceCommunityListResult is now required
  - Parameter value of model ConnectionSharedKeyResultList is now required
  - Parameter value of model ConnectivityConfigurationListResult is now required
  - Parameter value of model CustomIpPrefixListResult is now required
  - Parameter value of model DdosProtectionPlanListResult is now required
  - Parameter value of model DscpConfigurationListResult is now required
  - Parameter value of model EffectiveNetworkSecurityGroupListResult is now required
  - Parameter value of model EffectiveRouteListResult is now required
  - Parameter value of model EndpointServicesListResult is now required
  - Parameter value of model ExpressRouteCircuitConnectionListResult is now required
  - Parameter value of model ExpressRouteCircuitListResult is now required
  - Parameter value of model ExpressRouteCircuitPeeringListResult is now required
  - Parameter value of model ExpressRouteCircuitsArpTableListResult is now required
  - Parameter value of model ExpressRouteCircuitsRoutesTableListResult is now required
  - Parameter value of model ExpressRouteCircuitsRoutesTableSummaryListResult is now required
  - Parameter value of model ExpressRouteCrossConnectionListResult is now required
  - Parameter value of model ExpressRouteCrossConnectionPeeringList is now required
  - Parameter value of model ExpressRouteCrossConnectionsRoutesTableSummaryListResult is now required
  - Parameter value of model ExpressRouteLinkListResult is now required
  - Parameter value of model ExpressRoutePortAuthorizationListResult is now required
  - Parameter value of model ExpressRoutePortListResult is now required
  - Parameter value of model ExpressRoutePortsLocationListResult is now required
  - Parameter value of model ExpressRouteProviderPortListResult is now required
  - Parameter value of model ExpressRouteServiceProviderListResult is now required
  - Parameter value of model FirewallPolicyListResult is now required
  - Parameter value of model FirewallPolicyRuleCollectionGroupListResult is now required
  - Parameter value of model FlowLogListResult is now required
  - Parameter value of model GetServiceGatewayAddressLocationsResult is now required
  - Parameter value of model GetServiceGatewayServicesResult is now required
  - Parameter value of model InboundNatRuleListResult is now required
  - Parameter value of model IpAllocationListResult is now required
  - Parameter value of model IpGroupListResult is now required
  - Parameter value of model IpamPoolList is now required
  - Parameter value of model ListHubRouteTablesResult is now required
  - Parameter value of model ListHubVirtualNetworkConnectionsResult is now required
  - Parameter value of model ListP2SVpnGatewaysResult is now required
  - Parameter value of model ListRouteMapsResult is now required
  - Parameter value of model ListRoutingIntentResult is now required
  - Parameter value of model ListVirtualHubBgpConnectionResults is now required
  - Parameter value of model ListVirtualHubIpConfigurationResults is now required
  - Parameter value of model ListVirtualHubRouteTableV2SResult is now required
  - Parameter value of model ListVirtualHubsResult is now required
  - Parameter value of model ListVirtualNetworkGatewayNatRulesResult is now required
  - Parameter value of model ListVirtualWANsResult is now required
  - Parameter value of model ListVpnConnectionsResult is now required
  - Parameter value of model ListVpnGatewayNatRulesResult is now required
  - Parameter value of model ListVpnGatewaysResult is now required
  - Parameter value of model ListVpnServerConfigurationPolicyGroupsResult is now required
  - Parameter value of model ListVpnServerConfigurationsResult is now required
  - Parameter value of model ListVpnSiteLinkConnectionsResult is now required
  - Parameter value of model ListVpnSiteLinksResult is now required
  - Parameter value of model ListVpnSitesResult is now required
  - Parameter value of model LoadBalancerBackendAddressPoolListResult is now required
  - Parameter value of model LoadBalancerFrontendIPConfigurationListResult is now required
  - Parameter value of model LoadBalancerListResult is now required
  - Parameter value of model LoadBalancerLoadBalancingRuleListResult is now required
  - Parameter value of model LoadBalancerOutboundRuleListResult is now required
  - Parameter value of model LoadBalancerProbeListResult is now required
  - Parameter value of model LocalNetworkGatewayListResult is now required
  - Parameter value of model NatGatewayListResult is now required
  - Parameter value of model NetworkGroupListResult is now required
  - Parameter value of model NetworkInterfaceIPConfigurationListResult is now required
  - Parameter value of model NetworkInterfaceListResult is now required
  - Parameter value of model NetworkInterfaceLoadBalancerListResult is now required
  - Parameter value of model NetworkInterfaceTapConfigurationListResult is now required
  - Parameter value of model NetworkManagerConnectionListResult is now required
  - Parameter value of model NetworkManagerListResult is now required
  - Parameter value of model NetworkManagerRoutingConfigurationListResult is now required
  - Parameter value of model NetworkProfileListResult is now required
  - Parameter value of model NetworkSecurityGroupListResult is now required
  - Parameter value of model NetworkSecurityPerimeterListResult is now required
  - Parameter value of model NetworkVirtualApplianceConnectionList is now required
  - Parameter value of model NetworkVirtualApplianceListResult is now required
  - Parameter value of model NetworkVirtualApplianceSiteListResult is now required
  - Parameter value of model NetworkVirtualApplianceSkuListResult is now required
  - Parameter value of model NspAccessRuleListResult is now required
  - Parameter value of model NspAssociationsListResult is now required
  - Parameter value of model NspLinkListResult is now required
  - Parameter value of model NspLinkReferenceListResult is now required
  - Parameter value of model NspLoggingConfigurationListResult is now required
  - Parameter value of model NspProfileListResult is now required
  - Parameter value of model NspServiceTagsListResult is now required
  - Parameter value of model OperationListResult is now required
  - Parameter value of model PeerExpressRouteCircuitConnectionListResult is now required
  - Parameter value of model PerimeterAssociableResourcesListResult is now required
  - Parameter value of model PoolAssociationList is now required
  - Parameter value of model PrivateDnsZoneGroupListResult is now required
  - Parameter value of model PrivateEndpointConnectionListResult is now required
  - Parameter value of model PrivateEndpointListResult is now required
  - Parameter value of model PrivateLinkServiceListResult is now required
  - Parameter value of model PublicIPAddressListResult is now required
  - Parameter value of model PublicIPPrefixListResult is now required
  - Parameter value of model RadiusAuthServerListResult is now required
  - Parameter value of model ReachabilityAnalysisIntentListResult is now required
  - Parameter value of model ReachabilityAnalysisRunListResult is now required
  - Parameter value of model ResourceNavigationLinksListResult is now required
  - Parameter value of model RouteFilterListResult is now required
  - Parameter value of model RouteFilterRuleListResult is now required
  - Parameter value of model RouteListResult is now required
  - Parameter value of model RouteTableListResult is now required
  - Parameter value of model RoutingRuleCollectionListResult is now required
  - Parameter value of model RoutingRuleListResult is now required
  - Parameter value of model ScopeConnectionListResult is now required
  - Parameter value of model SecurityAdminConfigurationListResult is now required
  - Parameter value of model SecurityPartnerProviderListResult is now required
  - Parameter value of model SecurityRuleListResult is now required
  - Parameter value of model SecurityUserConfigurationListResult is now required
  - Parameter value of model SecurityUserRuleCollectionListResult is now required
  - Parameter value of model SecurityUserRuleListResult is now required
  - Parameter value of model ServiceAssociationLinksListResult is now required
  - Parameter value of model ServiceEndpointPolicyDefinitionListResult is now required
  - Parameter value of model ServiceEndpointPolicyListResult is now required
  - Parameter value of model ServiceGatewayListResult is now required
  - Parameter value of model ServiceTagInformationListResult is now required
  - Parameter value of model StaticCidrList is now required
  - Parameter value of model StaticMemberListResult is now required
  - Parameter value of model SubnetListResult is now required
  - Parameter value of model UsagesListResult is now required
  - Parameter value of model VerifierWorkspaceListResult is now required
  - Parameter value of model VirtualNetworkApplianceListResult is now required
  - Parameter value of model VirtualNetworkDdosProtectionStatusResult is now required
  - Parameter value of model VirtualNetworkGatewayConnectionListResult is now required
  - Parameter value of model VirtualNetworkGatewayListConnectionsResult is now required
  - Parameter value of model VirtualNetworkGatewayListResult is now required
  - Parameter value of model VirtualNetworkListResult is now required
  - Parameter value of model VirtualNetworkListUsageResult is now required
  - Parameter value of model VirtualNetworkPeeringListResult is now required
  - Parameter value of model VirtualNetworkTapListResult is now required
  - Parameter value of model VirtualRouterListResult is now required
  - Parameter value of model VirtualRouterPeeringListResult is now required
  - Parameter value of model WebApplicationFirewallPolicyListResult is now required

## 30.2.0 (2026-02-11)

### Features Added

  - Client `NetworkManagementClient` added operation group `service_gateways`
  - Client `NetworkManagementClient` added operation group `virtual_network_appliances`
  - Enum `ActionType` added member `CAPTCHA`
  - Enum `FirewallPolicyIntrusionDetectionProfileType` added member `CORE`
  - Enum `FirewallPolicyIntrusionDetectionProfileType` added member `EMERGING`
  - Enum `FirewallPolicyIntrusionDetectionProfileType` added member `OFF`
  - Model `NatGateway` added property `service_gateway`
  - Model `PolicySettings` added property `captcha_cookie_expiration_in_mins`
  - Model `Subnet` added property `service_gateway`
  - Enum `WebApplicationFirewallAction` added member `CAPTCHA`
  - Added enum `AddressUpdateAction`
  - Added model `GetServiceGatewayAddressLocationsResult`
  - Added model `GetServiceGatewayServicesResult`
  - Added model `RouteTargetAddressPropertiesFormat`
  - Added model `ServiceGateway`
  - Added model `ServiceGatewayAddress`
  - Added model `ServiceGatewayAddressLocation`
  - Added model `ServiceGatewayAddressLocationResponse`
  - Added model `ServiceGatewayListResult`
  - Added model `ServiceGatewayService`
  - Added model `ServiceGatewayServiceRequest`
  - Added model `ServiceGatewaySku`
  - Added enum `ServiceGatewaySkuName`
  - Added enum `ServiceGatewaySkuTier`
  - Added model `ServiceGatewayUpdateAddressLocationsRequest`
  - Added model `ServiceGatewayUpdateServicesRequest`
  - Added enum `ServiceType`
  - Added enum `ServiceUpdateAction`
  - Added enum `UpdateAction`
  - Added model `VirtualNetworkAppliance`
  - Added model `VirtualNetworkApplianceIpConfiguration`
  - Added model `VirtualNetworkApplianceListResult`
  - Added operation group `ServiceGatewaysOperations`
  - Added operation group `VirtualNetworkAppliancesOperations`

### Breaking Changes

  - Deleted or renamed enum value `FirewallPolicyIntrusionDetectionProfileType.ADVANCED`
  - Deleted or renamed enum value `FirewallPolicyIntrusionDetectionProfileType.BASIC`
  - Deleted or renamed enum value `FirewallPolicyIntrusionDetectionProfileType.STANDARD`

## 30.1.0 (2025-11-19)

### Features Added

  - Added operation PublicIPAddressesOperations.begin_disassociate_cloud_service_reserved_public_ip
  - Added operation PublicIPAddressesOperations.begin_reserve_cloud_service_public_ip_address
  - Model ApplicationGateway has a new parameter entra_jwt_validation_configs
  - Model ApplicationGatewayBackendSettings has a new parameter enable_l4_client_ip_preservation
  - Model ApplicationGatewayClientAuthConfiguration has a new parameter verify_client_auth_mode
  - Model ApplicationGatewayOnDemandProbe has a new parameter enable_probe_proxy_protocol_header
  - Model ApplicationGatewayProbe has a new parameter enable_probe_proxy_protocol_header
  - Model ApplicationGatewayRequestRoutingRule has a new parameter entra_jwt_validation_config
  - Model DdosCustomPolicy has a new parameter detection_rules
  - Model DdosCustomPolicy has a new parameter front_end_ip_configuration
  - Model FlowLog has a new parameter record_types
  - Model FlowLogInformation has a new parameter record_types
  - Model LoadBalancer has a new parameter scope
  - Model NetworkManagerRoutingConfiguration has a new parameter route_table_usage_mode
  - Model PrivateEndpoint has a new parameter ip_version_type
  - Model PrivateLinkService has a new parameter access_mode
  - Model VirtualNetworkGatewayConnection has a new parameter authentication_type
  - Model VirtualNetworkGatewayConnection has a new parameter certificate_authentication

## 30.0.0 (2025-10-24)

### Features Added

  - Added operation AzureFirewallsOperations.begin_packet_capture_operation
  - Added operation VirtualNetworkGatewaysOperations.list_radius_secrets
  - Added operation VpnServerConfigurationsOperations.list_radius_secrets
  - Added operation group NetworkSecurityPerimeterServiceTagsOperations
  - Model ApplicationGatewayBackendHttpSettings has a new parameter dedicated_backend_connection
  - Model ApplicationGatewayBackendHttpSettings has a new parameter sni_name
  - Model ApplicationGatewayBackendHttpSettings has a new parameter validate_cert_chain_and_expiry
  - Model ApplicationGatewayBackendHttpSettings has a new parameter validate_sni
  - Model AzureFirewall has a new parameter extended_location
  - Model FirewallPacketCaptureParameters has a new parameter operation
  - Model NetworkVirtualAppliance has a new parameter nva_interface_configurations
  - Model NetworkVirtualAppliance has a new parameter private_ip_address

### Breaking Changes

  - Removed operation group NetworkManagementClientOperationsMixin

## 29.0.0 (2025-05-22)

### Features Added

  - Added operation NetworkVirtualAppliancesOperations.begin_get_boot_diagnostic_logs
  - Added operation NetworkVirtualAppliancesOperations.begin_reimage
  - Added operation VirtualNetworkGatewaysOperations.begin_get_resiliency_information
  - Added operation VirtualNetworkGatewaysOperations.begin_get_routes_information
  - Added operation VirtualNetworkGatewaysOperations.begin_invoke_abort_migration
  - Added operation VirtualNetworkGatewaysOperations.begin_invoke_commit_migration
  - Added operation VirtualNetworkGatewaysOperations.begin_invoke_execute_migration
  - Added operation VirtualNetworkGatewaysOperations.begin_invoke_prepare_migration
  - Added operation group NetworkSecurityPerimeterAccessRulesOperations
  - Added operation group NetworkSecurityPerimeterAssociableResourceTypesOperations
  - Added operation group NetworkSecurityPerimeterAssociationsOperations
  - Added operation group NetworkSecurityPerimeterLinkReferencesOperations
  - Added operation group NetworkSecurityPerimeterLinksOperations
  - Added operation group NetworkSecurityPerimeterLoggingConfigurationsOperations
  - Added operation group NetworkSecurityPerimeterOperationStatusesOperations
  - Added operation group NetworkSecurityPerimeterProfilesOperations
  - Added operation group NetworkSecurityPerimetersOperations
  - Model ActiveConnectivityConfiguration has a new parameter connectivity_capabilities
  - Model ConnectivityConfiguration has a new parameter connectivity_capabilities
  - Model EffectiveConnectivityConfiguration has a new parameter connectivity_capabilities
  - Model ExpressRouteCircuitPeeringConfig has a new parameter advertised_public_prefix_info
  - Model IpamPool has a new parameter etag
  - Model LoadBalancingRule has a new parameter enable_connection_tracking
  - Model ManagedRuleSet has a new parameter computed_disabled_rules
  - Model NatGateway has a new parameter public_ip_addresses_v6
  - Model NatGateway has a new parameter public_ip_prefixes_v6
  - Model NatGateway has a new parameter source_virtual_network
  - Model VerifierWorkspace has a new parameter etag
  - Model VirtualNetwork has a new parameter default_public_nat_gateway
  - Model VirtualNetworkGateway has a new parameter enable_high_bandwidth_vpn_gateway
  - Model VirtualNetworkGateway has a new parameter virtual_network_gateway_migration_status
  - Model VirtualNetworkGatewayConnection has a new parameter tunnel_properties
  - Operation IpamPoolsOperations.begin_create has a new optional parameter if_match
  - Operation IpamPoolsOperations.begin_delete has a new optional parameter if_match
  - Operation IpamPoolsOperations.update has a new optional parameter if_match
  - Operation VerifierWorkspacesOperations.begin_delete has a new optional parameter if_match
  - Operation VerifierWorkspacesOperations.create has a new optional parameter if_match
  - Operation VerifierWorkspacesOperations.update has a new optional parameter if_match

### Breaking Changes

  - Removed operation ConnectionMonitorsOperations.begin_query
  - Removed operation ConnectionMonitorsOperations.begin_start

## 28.1.0 (2024-12-20)

### Features Added

  - Client `NetworkManagementClient` added operation group `ipam_pools`
  - Client `NetworkManagementClient` added operation group `static_cidrs`
  - Client `NetworkManagementClient` added operation group `reachability_analysis_intents`
  - Client `NetworkManagementClient` added operation group `reachability_analysis_runs`
  - Client `NetworkManagementClient` added operation group `verifier_workspaces`
  - Enum `AddressPrefixType` added member `NETWORK_GROUP`
  - Model `AddressSpace` added property `ipam_pool_prefix_allocations`
  - Model `BastionHost` added property `enable_private_only_bastion`
  - Enum `FirewallPolicyIDPSSignatureDirection` added member `FIVE`
  - Model `NetworkInterface` added property `default_outbound_connectivity_enabled`
  - Enum `ProvisioningState` added member `CANCELED`
  - Enum `ProvisioningState` added member `CREATING`
  - Model `SecurityAdminConfiguration` added property `network_group_address_space_aggregation_option`
  - Model `Subnet` added property `ipam_pool_prefix_allocations`
  - Added enum `AddressSpaceAggregationOption`
  - Added model `CommonErrorAdditionalInfo`
  - Added model `CommonErrorDetail`
  - Added model `CommonErrorResponse`
  - Added model `CommonProxyResource`
  - Added model `CommonResource`
  - Added model `CommonTrackedResource`
  - Added model `ExpressRouteFailoverCircuitResourceDetails`
  - Added model `ExpressRouteFailoverConnectionResourceDetails`
  - Added model `ExpressRouteFailoverRedundantRoute`
  - Added model `ExpressRouteFailoverSingleTestDetails`
  - Added model `ExpressRouteFailoverStopApiParameters`
  - Added model `ExpressRouteFailoverTestDetails`
  - Added model `FailoverConnectionDetails`
  - Added enum `FailoverConnectionStatus`
  - Added enum `FailoverTestStatus`
  - Added enum `FailoverTestStatusForSingleTest`
  - Added enum `FailoverTestType`
  - Added model `IPTraffic`
  - Added model `IntentContent`
  - Added enum `IpType`
  - Added model `IpamPool`
  - Added model `IpamPoolList`
  - Added model `IpamPoolPrefixAllocation`
  - Added model `IpamPoolProperties`
  - Added model `IpamPoolUpdate`
  - Added model `IpamPoolUpdateProperties`
  - Added model `LoadBalancerHealthPerRule`
  - Added model `LoadBalancerHealthPerRulePerBackendAddress`
  - Added enum `NetworkProtocol`
  - Added model `PoolAssociation`
  - Added model `PoolAssociationList`
  - Added model `PoolUsage`
  - Added model `ReachabilityAnalysisIntent`
  - Added model `ReachabilityAnalysisIntentListResult`
  - Added model `ReachabilityAnalysisIntentProperties`
  - Added model `ReachabilityAnalysisRun`
  - Added model `ReachabilityAnalysisRunListResult`
  - Added model `ReachabilityAnalysisRunProperties`
  - Added model `ResourceBasics`
  - Added model `StaticCidr`
  - Added model `StaticCidrList`
  - Added model `StaticCidrProperties`
  - Added model `VerifierWorkspace`
  - Added model `VerifierWorkspaceListResult`
  - Added model `VerifierWorkspaceProperties`
  - Added model `VerifierWorkspaceUpdate`
  - Added model `VerifierWorkspaceUpdateProperties`
  - Operation group `LoadBalancerLoadBalancingRulesOperations` added method `begin_health`
  - Operation group `VirtualNetworkGatewaysOperations` added method `begin_get_failover_all_test_details`
  - Operation group `VirtualNetworkGatewaysOperations` added method `begin_get_failover_single_test_details`
  - Operation group `VirtualNetworkGatewaysOperations` added method `begin_start_express_route_site_failover_simulation`
  - Operation group `VirtualNetworkGatewaysOperations` added method `begin_stop_express_route_site_failover_simulation`
  - Added operation group `IpamPoolsOperations`
  - Added operation group `ReachabilityAnalysisIntentsOperations`
  - Added operation group `ReachabilityAnalysisRunsOperations`
  - Added operation group `StaticCidrsOperations`
  - Added operation group `VerifierWorkspacesOperations`

## 28.0.0 (2024-11-01)

### Breaking Changes

- This package now only targets the latest Api-Version available on Azure and removes APIs of other Api-Version. After this change, the package can have much smaller size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.

## 27.0.0 (2024-09-22)

### Features Added

  - Added operation SecurityUserConfigurationsOperations.begin_delete
  - Added operation VpnLinkConnectionsOperations.begin_set_or_init_default_shared_key
  - Added operation VpnLinkConnectionsOperations.get_all_shared_keys
  - Added operation VpnLinkConnectionsOperations.get_default_shared_key
  - Added operation VpnLinkConnectionsOperations.list_default_shared_key
  - Added operation group NetworkManagerRoutingConfigurationsOperations
  - Added operation group RoutingRuleCollectionsOperations
  - Added operation group RoutingRulesOperations
  - Added operation group SecurityUserRuleCollectionsOperations
  - Added operation group SecurityUserRulesOperations
  - Model ApplicationGatewayFirewallRule has a new parameter sensitivity
  - Model AzureFirewall has a new parameter autoscale_configuration
  - Model ConfigurationGroup has a new parameter member_type
  - Model ConnectionSharedKeyResult has a new parameter id
  - Model ConnectionSharedKeyResult has a new parameter name
  - Model ConnectionSharedKeyResult has a new parameter properties
  - Model ConnectionSharedKeyResult has a new parameter type
  - Model FlowLog has a new parameter enabled_filtering_criteria
  - Model FlowLogInformation has a new parameter enabled_filtering_criteria
  - Model ManagedRuleOverride has a new parameter sensitivity
  - Model ManagedRulesDefinition has a new parameter exceptions
  - Model NetworkGroup has a new parameter member_type
  - Model PrivateLinkService has a new parameter destination_ip_address
  - Model VirtualNetwork has a new parameter private_endpoint_v_net_policies
  - Model VirtualNetworkGateway has a new parameter resiliency_model
  - Model WebApplicationFirewallPolicy has a new parameter application_gateway_for_containers

### Breaking Changes

  - Model ConnectionSharedKeyResult no longer has parameter value

## 26.0.0 (2024-07-21)

### Features Added

  - Added operation InboundSecurityRuleOperations.get
  - Model BastionHost has a new parameter enable_session_recording
  - Model ExpressRouteCircuitAuthorization has a new parameter connection_resource_uri
  - Model FlowLog has a new parameter identity
  - Model FlowLogInformation has a new parameter identity
  - Model Probe has a new parameter no_healthy_backends_behavior
  - Model ServiceEndpointPropertiesFormat has a new parameter network_identifier
  - Model VirtualNetworkGateway has a new parameter identity
  - Operation ExpressRouteCrossConnectionsOperations.list has a new optional parameter filter

### Breaking Changes

  - Model FirewallPacketCaptureParameters no longer has parameter id

## 25.4.0 (2024-05-27)

### Features Added

  - Added operation NetworkVirtualAppliancesOperations.begin_restart
  - Added operation group FirewallPolicyDeploymentsOperations
  - Added operation group FirewallPolicyDraftsOperations
  - Added operation group FirewallPolicyRuleCollectionGroupDraftsOperations
  - Model ApplicationGatewayHeaderConfiguration has a new parameter header_value_matcher
  - Model ApplicationGatewaySku has a new parameter family
  - Model ConnectionMonitorEndpoint has a new parameter location_details
  - Model ConnectionMonitorEndpoint has a new parameter subscription_id
  - Model ExpressRouteCircuit has a new parameter enable_direct_port_rate_limit
  - Model InboundSecurityRule has a new parameter rule_type
  - Model InboundSecurityRules has a new parameter applies_on
  - Model InboundSecurityRules has a new parameter destination_port_ranges
  - Model InboundSecurityRules has a new parameter name
  - Model NetworkInterfaceIPConfiguration has a new parameter private_ip_address_prefix_length
  - Model NetworkVirtualAppliance has a new parameter network_profile
  - Model PacketCapture has a new parameter capture_settings
  - Model PacketCapture has a new parameter continuous_capture
  - Model PacketCaptureParameters has a new parameter capture_settings
  - Model PacketCaptureParameters has a new parameter continuous_capture
  - Model PacketCaptureResult has a new parameter capture_settings
  - Model PacketCaptureResult has a new parameter continuous_capture
  - Model PacketCaptureResultProperties has a new parameter capture_settings
  - Model PacketCaptureResultProperties has a new parameter continuous_capture
  - Model PacketCaptureStorageLocation has a new parameter local_path
  - Model PolicySettings has a new parameter js_challenge_cookie_expiration_in_mins
  - Model Subnet has a new parameter sharing_scope
  - Model VirtualApplianceNicProperties has a new parameter nic_type
  - Model VirtualNetworkPeering has a new parameter enable_only_i_pv6_peering
  - Model VirtualNetworkPeering has a new parameter local_address_space
  - Model VirtualNetworkPeering has a new parameter local_subnet_names
  - Model VirtualNetworkPeering has a new parameter local_virtual_network_address_space
  - Model VirtualNetworkPeering has a new parameter peer_complete_vnets
  - Model VirtualNetworkPeering has a new parameter remote_subnet_names
  - Model VpnSiteLinkConnection has a new parameter dpd_timeout_seconds

## 25.3.0 (2024-02-22)

### Features Added

  - Model BastionHost has a new parameter zones

## 25.2.0 (2023-12-18)

### Features Added

  - Added operation NetworkManagementClientOperationsMixin.begin_delete_bastion_shareable_link_by_token
  - Added operation NetworkSecurityPerimetersOperations.patch
  - Model ApplicationGatewayListener has a new parameter host_names
  - Model FirewallPolicyIntrusionDetection has a new parameter profile
  - Model NetworkVirtualAppliance has a new parameter internet_ingress_public_ips

## 25.1.0 (2023-09-15)

### Features Added

  - Model BastionHost has a new parameter network_acls
  - Model BastionHost has a new parameter virtual_network
  - Model FirewallPolicy has a new parameter size
  - Model FirewallPolicyRuleCollectionGroup has a new parameter size
  - Model Subnet has a new parameter default_outbound_access
  - Model VirtualNetworkGateway has a new parameter auto_scale_configuration

## 25.0.0 (2023-08-18)

### Features Added

  - Added operation LoadBalancersOperations.migrate_to_ip_based
  - Model BackendAddressPool has a new parameter sync_mode

### Breaking Changes

  - Removed operation group NspLinkReconcileOperations
  - Removed operation group NspLinkReferenceReconcileOperations

## 24.0.0 (2023-07-21)

### Breaking Changes

  - Removed `HTTP_STATUS499` from enum `ApplicationGatewayCustomErrorStatusCode`

### Features Added

  - Added enum `AdminState`
  - Model ActiveConnectivityConfiguration has a new parameter resource_guid
  - Model ActiveDefaultSecurityAdminRule has a new parameter resource_guid
  - Model ActiveSecurityAdminRule has a new parameter resource_guid
  - Model AdminRule has a new parameter resource_guid
  - Model AdminRuleCollection has a new parameter resource_guid
  - Model ApplicationGateway has a new parameter default_predefined_ssl_policy
  - Model ConfigurationGroup has a new parameter resource_guid
  - Model ConnectivityConfiguration has a new parameter resource_guid
  - Model DefaultAdminRule has a new parameter resource_guid
  - Model EffectiveConnectivityConfiguration has a new parameter resource_guid
  - Model EffectiveDefaultSecurityAdminRule has a new parameter resource_guid
  - Model EffectiveSecurityAdminRule has a new parameter resource_guid
  - Model NetworkGroup has a new parameter resource_guid
  - Model NetworkManager has a new parameter resource_guid
  - Model SecurityAdminConfiguration has a new parameter resource_guid
  - Model VirtualNetworkGateway has a new parameter admin_state

## 23.1.0 (2023-05-20)

### Features Added

  - Added operation AzureFirewallsOperations.begin_packet_capture
  - Added operation group NetworkVirtualApplianceConnectionsOperations
  - Model ApplicationRule has a new parameter http_headers_to_insert
  - Model BastionHost has a new parameter enable_kerberos
  - Model NetworkInterface has a new parameter auxiliary_sku
  - Model NetworkVirtualAppliance has a new parameter additional_nics
  - Model NetworkVirtualAppliance has a new parameter virtual_appliance_connections
  - Model PolicySettings has a new parameter file_upload_enforcement
  - Model PolicySettings has a new parameter log_scrubbing
  - Model PolicySettings has a new parameter request_body_enforcement
  - Model PolicySettings has a new parameter request_body_inspect_limit_in_kb
  - Model PrivateEndpointConnection has a new parameter private_endpoint_location
  - Model PublicIPAddressDnsSettings has a new parameter domain_name_label_scope
  - Model VirtualApplianceNicProperties has a new parameter instance_name
  - Model WebApplicationFirewallCustomRule has a new parameter group_by_user_session
  - Model WebApplicationFirewallCustomRule has a new parameter rate_limit_duration
  - Model WebApplicationFirewallCustomRule has a new parameter rate_limit_threshold

## 23.0.1 (2023-04-26)

### Bugs Fixed

  - Fix calling failure for those operations which could be called by client directly #30057

## 23.0.0 (2023-03-29)

### Other Changes

  - Initial stable release with our new combined multiapi package. Package size is now 5% of what it used to be.

### Breaking Changes

  - All query and header parameters are now keyword-only
  - Removed api version subfolders. This means you can no longer access any `azure.mgmt.network.v20xx_xx_xx` modules.
  - Removed `.models` method from `NetworkManagementClient`. Instead, import models from `azure.mgmt.network.models`.

## 22.3.0 (2023-03-20)

### Features Added

  - Model ExpressRouteCircuit has a new parameter authorization_status
  - Model NspAccessRule has a new parameter email_addresses
  - Model NspAccessRule has a new parameter phone_numbers
  - Model NspLink has a new parameter remote_perimeter_location
  - Model NspLinkReference has a new parameter remote_perimeter_location
  - Model VirtualNetwork has a new parameter flow_logs
  - Model WebApplicationFirewallCustomRule has a new parameter state
  - Operation VpnGatewaysOperations.begin_reset has a new optional parameter ip_configuration_id

## 23.0.0b2 (2023-02-20)

### Other Changes

  - Continued package size improvements. The whole package is now 5% of the latest stable release

### Breaking Changes

  - Removed api version subfolders. This means you can no longer access any `azure.mgmt.network.v20xx_xx_xx` modules
  - Removed `.models` method from `NetworkManagementClient`

## 23.0.0b1 (2022-12-19)

### Other Changes

  - Preview package with the same multiapi support but much reduced package size.

### Breaking Changes

  - All query and header parameters are now keyword-only
  - Can not individually access each API version's client and operations

## 22.2.0 (2022-12-15)

### Features Added

  - Model BackendAddressPool has a new parameter virtual_network
  - Model NetworkVirtualAppliance has a new parameter delegation
  - Model NetworkVirtualAppliance has a new parameter deployment_type
  - Model NetworkVirtualAppliance has a new parameter partner_managed_resource
  - Model PolicySettings has a new parameter custom_block_response_body
  - Model PolicySettings has a new parameter custom_block_response_status_code

## 22.1.0 (2022-10-24)

### Features Added

  - Added operation group NspLinkReconcileOperations
  - Added operation group NspLinkReferenceReconcileOperations
  - Added operation group NspLinkReferencesOperations
  - Added operation group NspLinksOperations

## 22.0.0 (2022-10-12)

### Features Added

  - Added operation PublicIPAddressesOperations.begin_ddos_protection_status
  - Added operation VirtualHubsOperations.begin_get_inbound_routes
  - Added operation VirtualHubsOperations.begin_get_outbound_routes
  - Added operation VirtualNetworksOperations.begin_list_ddos_protection_status
  - Added operation group ApplicationGatewayWafDynamicManifestsDefaultOperations
  - Added operation group ApplicationGatewayWafDynamicManifestsOperations
  - Added operation group NspAssociationReconcileOperations
  - Added operation group RouteMapsOperations
  - Added operation group VipSwapOperations
  - Model ApplicationGatewayClientAuthConfiguration has a new parameter verify_client_revocation
  - Model ApplicationGatewayFirewallRule has a new parameter action
  - Model ApplicationGatewayFirewallRule has a new parameter rule_id_string
  - Model ApplicationGatewayFirewallRule has a new parameter state
  - Model ApplicationGatewayFirewallRuleSet has a new parameter tiers
  - Model CustomIpPrefix has a new parameter asn
  - Model CustomIpPrefix has a new parameter express_route_advertise
  - Model CustomIpPrefix has a new parameter geo
  - Model CustomIpPrefix has a new parameter prefix_type
  - Model DdosProtectionPlan has a new parameter public_ip_addresses
  - Model DdosSettings has a new parameter ddos_protection_plan
  - Model DdosSettings has a new parameter protection_mode
  - Model ExpressRouteConnection has a new parameter enable_private_link_fast_path
  - Model ExpressRouteGateway has a new parameter allow_non_virtual_wan_traffic
  - Model ExpressRouteLink has a new parameter colo_location
  - Model ExpressRoutePort has a new parameter billing_type
  - Model ManagedRuleOverride has a new parameter action
  - Model NetworkInterface has a new parameter disable_tcp_state_tracking
  - Model NspProfile has a new parameter diagnostic_settings_version
  - Model Probe has a new parameter probe_threshold
  - Model RoutingConfiguration has a new parameter inbound_route_map
  - Model RoutingConfiguration has a new parameter outbound_route_map
  - Model VirtualHub has a new parameter route_maps
  - Model VirtualNetworkGateway has a new parameter allow_remote_vnet_traffic
  - Model VirtualNetworkGateway has a new parameter allow_virtual_wan_traffic
  - Model VirtualNetworkGateway has a new parameter virtual_network_gateway_policy_groups
  - Model VirtualNetworkGatewayConnection has a new parameter enable_private_link_fast_path
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter enable_private_link_fast_path
  - Model VnetRoute has a new parameter static_routes_config
  - Model VpnClientConfiguration has a new parameter vng_client_connection_configurations

### Breaking Changes

  - Model DdosCustomPolicy no longer has parameter protocol_custom_settings
  - Model DdosCustomPolicy no longer has parameter public_ip_addresses
  - Model DdosSettings no longer has parameter ddos_custom_policy
  - Model DdosSettings no longer has parameter protected_ip
  - Model DdosSettings no longer has parameter protection_coverage
  - Operation NetworkManagementClientOperationsMixin.list_active_connectivity_configurations has a new parameter top
  - Operation NetworkManagementClientOperationsMixin.list_active_security_admin_rules has a new parameter top
  - Operation NetworkManagementClientOperationsMixin.list_network_manager_effective_connectivity_configurations has a new parameter top
  - Operation NetworkManagementClientOperationsMixin.list_network_manager_effective_security_admin_rules has a new parameter top
  - Operation NetworkManagerDeploymentStatusOperations.list has a new parameter top
  - Removed operation NetworkSecurityPerimetersOperations.check_members
  - Removed operation NetworkSecurityPerimetersOperations.query
  - Removed operation group NspAssociationsProxyOperations

## 21.0.1 (2022-08-17)

### Bugs Fixed

  - Add `__version__` to `__init__.py` for package

## 21.0.0 (2022-08-05)

**Features**

  - Added operation AdminRuleCollectionsOperations.begin_delete
  - Added operation AdminRulesOperations.begin_delete
  - Added operation AzureFirewallsOperations.begin_list_learned_prefixes
  - Added operation ConnectivityConfigurationsOperations.begin_delete
  - Added operation NetworkGroupsOperations.begin_delete
  - Added operation NetworkManagementClientOperationsMixin.express_route_provider_port
  - Added operation NetworkManagementClientOperationsMixin.list_active_connectivity_configurations
  - Added operation NetworkManagementClientOperationsMixin.list_active_security_admin_rules
  - Added operation NetworkManagementClientOperationsMixin.list_network_manager_effective_connectivity_configurations
  - Added operation NetworkManagementClientOperationsMixin.list_network_manager_effective_security_admin_rules
  - Added operation NetworkManagerCommitsOperations.begin_post
  - Added operation NetworkManagersOperations.begin_delete
  - Added operation NetworkManagersOperations.patch
  - Added operation NetworkSecurityPerimetersOperations.check_members
  - Added operation NetworkSecurityPerimetersOperations.query
  - Added operation SecurityAdminConfigurationsOperations.begin_delete
  - Added operation group ExpressRouteProviderPortsLocationOperations
  - Added operation group ManagementGroupNetworkManagerConnectionsOperations
  - Added operation group NspAccessRulesReconcileOperations
  - Added operation group NspAssociationsProxyOperations
  - Added operation group ScopeConnectionsOperations
  - Added operation group StaticMembersOperations
  - Added operation group SubscriptionNetworkManagerConnectionsOperations
  - Model ApplicationGatewayRoutingRule has a new parameter priority
  - Model CustomIpPrefix has a new parameter no_internet_advertise
  - Model FirewallPolicy has a new parameter explicit_proxy
  - Model FirewallPolicySNAT has a new parameter auto_learn_private_ranges
  - Model NetworkManagerPropertiesNetworkManagerScopes has a new parameter cross_tenant_scopes
  - Model NetworkSecurityGroup has a new parameter flush_connection
  - Model NetworkSecurityPerimeter has a new parameter perimeter_guid
  - Model PacketCapture has a new parameter scope
  - Model PacketCapture has a new parameter target_type
  - Model PacketCaptureParameters has a new parameter scope
  - Model PacketCaptureParameters has a new parameter target_type
  - Model PacketCaptureResult has a new parameter scope
  - Model PacketCaptureResult has a new parameter target_type
  - Model PacketCaptureResultProperties has a new parameter scope
  - Model PacketCaptureResultProperties has a new parameter target_type
  - Model VirtualHub has a new parameter virtual_router_auto_scale_configuration

**Breaking changes**

  - Model ActiveBaseSecurityAdminRule no longer has parameter configuration_display_name
  - Model ActiveBaseSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model ActiveConnectivityConfiguration no longer has parameter display_name
  - Model ActiveDefaultSecurityAdminRule no longer has parameter configuration_display_name
  - Model ActiveDefaultSecurityAdminRule no longer has parameter display_name
  - Model ActiveDefaultSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model ActiveSecurityAdminRule no longer has parameter configuration_display_name
  - Model ActiveSecurityAdminRule no longer has parameter display_name
  - Model ActiveSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model AdminRule no longer has parameter display_name
  - Model ConfigurationGroup no longer has parameter conditional_membership
  - Model ConfigurationGroup no longer has parameter display_name
  - Model ConfigurationGroup no longer has parameter group_members
  - Model ConfigurationGroup no longer has parameter member_type
  - Model ConnectivityConfiguration no longer has parameter display_name
  - Model DefaultAdminRule no longer has parameter display_name
  - Model EffectiveBaseSecurityAdminRule no longer has parameter configuration_display_name
  - Model EffectiveBaseSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model EffectiveConnectivityConfiguration no longer has parameter display_name
  - Model EffectiveDefaultSecurityAdminRule no longer has parameter configuration_display_name
  - Model EffectiveDefaultSecurityAdminRule no longer has parameter display_name
  - Model EffectiveDefaultSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model EffectiveSecurityAdminRule no longer has parameter configuration_display_name
  - Model EffectiveSecurityAdminRule no longer has parameter display_name
  - Model EffectiveSecurityAdminRule no longer has parameter rule_collection_display_name
  - Model FirewallPolicy no longer has parameter explicit_proxy_settings
  - Model NetworkGroup no longer has parameter conditional_membership
  - Model NetworkGroup no longer has parameter display_name
  - Model NetworkGroup no longer has parameter group_members
  - Model NetworkGroup no longer has parameter member_type
  - Model NetworkManager no longer has parameter display_name
  - Model NetworkSecurityPerimeter no longer has parameter description
  - Model NetworkSecurityPerimeter no longer has parameter display_name
  - Model NetworkSecurityPerimeter no longer has parameter etag
  - Model NspProfile no longer has parameter enabled_log_categories
  - Parameter commit_type of model NetworkManagerCommit is now required
  - Parameter group_connectivity of model ConnectivityGroupItem is now required
  - Parameter network_group_id of model ConnectivityGroupItem is now required
  - Parameter network_group_id of model NetworkManagerSecurityGroupItem is now required
  - Parameter target_locations of model NetworkManagerCommit is now required
  - Removed operation AdminRuleCollectionsOperations.delete
  - Removed operation AdminRulesOperations.delete
  - Removed operation ConnectivityConfigurationsOperations.delete
  - Removed operation NetworkGroupsOperations.delete
  - Removed operation NetworkManagerCommitsOperations.post
  - Removed operation NetworkManagersOperations.delete
  - Removed operation NetworkManagersOperations.patch_tags
  - Removed operation SecurityAdminConfigurationsOperations.delete

## 20.0.0 (2022-05-10)

**Features**

  - Added operation FirewallPoliciesOperations.update_tags
  - Added operation PerimeterAssociableResourceTypesOperations.list
  - Added operation group ConfigurationPolicyGroupsOperations
  - Added operation group ExpressRoutePortAuthorizationsOperations
  - Added operation group NspAccessRulesOperations
  - Added operation group NspAssociationsOperations
  - Added operation group NspProfilesOperations
  - Model ApplicationGateway has a new parameter backend_settings_collection
  - Model ApplicationGateway has a new parameter listeners
  - Model ApplicationGateway has a new parameter routing_rules
  - Model ApplicationGatewayProbe has a new parameter pick_host_name_from_backend_settings
  - Model BackendAddressPool has a new parameter drain_period_in_seconds
  - Model ExpressRouteCircuit has a new parameter authorization_key
  - Model FirewallPolicyIntrusionDetectionConfiguration has a new parameter private_ranges
  - Model LoadBalancerBackendAddress has a new parameter admin_state
  - Model NetworkInterface has a new parameter auxiliary_mode
  - Model P2SConnectionConfiguration has a new parameter configuration_policy_group_associations
  - Model P2SConnectionConfiguration has a new parameter previous_configuration_policy_group_associations
  - Model VirtualHub has a new parameter hub_routing_preference
  - Model VirtualNetworkGatewayConnection has a new parameter gateway_custom_bgp_ip_addresses
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter gateway_custom_bgp_ip_addresses
  - Model VpnServerConfiguration has a new parameter configuration_policy_groups
  - Model VpnSiteLinkConnection has a new parameter vpn_gateway_custom_bgp_addresses

**Breaking changes**

  - Removed operation PerimeterAssociableResourceTypesOperations.get

## 19.3.0 (2021-11-05)

**Features**

  - Model LoadBalancerBackendAddress has a new parameter inbound_nat_rules_port_mapping
  - Model VpnNatRuleMapping has a new parameter port_range
  - Model OwaspCrsExclusionEntry has a new parameter exclusion_managed_rule_sets
  - Model VirtualNetworkPeering has a new parameter remote_virtual_network_encryption
  - Model NetworkInterface has a new parameter vnet_encryption_supported
  - Model VirtualNetworkGateway has a new parameter disable_ip_sec_replay_protection
  - Model VirtualNetwork has a new parameter encryption
  - Model BackendAddressPool has a new parameter inbound_nat_rules
  - Added operation LoadBalancersOperations.begin_list_inbound_nat_rule_port_mappings
  - Added operation group FirewallPolicyIdpsSignaturesOverridesOperations
  - Added operation group RoutingIntentOperations
  - Added operation group FirewallPolicyIdpsSignaturesOperations
  - Added operation group FirewallPolicyIdpsSignaturesFilterValuesOperations

## 19.2.0 (2021-10-21)

**Features**

  - Added operation group AdminRuleCollectionsOperations
  - Added operation group SecurityUserConfigurationsOperations
  - Added operation group ConnectivityConfigurationsOperations
  - Added operation group ActiveSecurityUserRulesOperations
  - Added operation group NetworkManagerCommitsOperations
  - Added operation group NetworkManagersOperations
  - Added operation group NetworkManagerDeploymentStatusOperations
  - Added operation group ActiveConnectivityConfigurationsOperations
  - Added operation group NetworkManagerEffectiveSecurityAdminRulesOperations
  - Added operation group UserRuleCollectionsOperations
  - Added operation group ActiveSecurityAdminRulesOperations
  - Added operation group UserRulesOperations
  - Added operation group NetworkGroupsOperations
  - Added operation group EffectiveVirtualNetworksOperations
  - Added operation group NetworkSecurityPerimetersOperations
  - Added operation group PerimeterAssociableResourceTypesOperations
  - Added operation group AdminRulesOperations
  - Added operation group SecurityAdminConfigurationsOperations
  - Added operation group EffectiveConnectivityConfigurationsOperations
  - Removed old api-version `2017-08-01`

## 19.1.0 (2021-10-09)

**Features**

  - Model ServiceEndpointPolicy has a new parameter service_alias
  - Model ServiceEndpointPolicy has a new parameter contextual_service_endpoint_policies
  - Model ApplicationGatewayRequestRoutingRule has a new parameter load_distribution_policy
  - Model BgpConnection has a new parameter hub_virtual_network_connection
  - Model BastionHost has a new parameter enable_ip_connect
  - Model BastionHost has a new parameter disable_copy_paste
  - Model BastionHost has a new parameter enable_tunneling
  - Model BastionHost has a new parameter scale_units
  - Model BastionHost has a new parameter enable_file_copy
  - Model BastionHost has a new parameter enable_shareable_link
  - Model DscpConfiguration has a new parameter qos_definition_collection
  - Model ServiceTagInformation has a new parameter service_tag_change_number
  - Model VnetRoute has a new parameter bgp_connections
  - Model VpnGateway has a new parameter enable_bgp_route_translation_for_nat
  - Model ServiceEndpointPolicyDefinition has a new parameter type
  - Model ApplicationGateway has a new parameter global_configuration
  - Model ApplicationGateway has a new parameter load_distribution_policies
  - Model InboundNatRule has a new parameter frontend_port_range_end
  - Model InboundNatRule has a new parameter frontend_port_range_start
  - Model InboundNatRule has a new parameter backend_address_pool
  - Model PrivateEndpoint has a new parameter ip_configurations
  - Model PrivateEndpoint has a new parameter application_security_groups
  - Model PrivateEndpoint has a new parameter custom_network_interface_name
  - Model NetworkVirtualAppliance has a new parameter ssh_public_key
  - Model ApplicationGatewayUrlPathMap has a new parameter default_load_distribution_policy
  - Model FirewallPolicy has a new parameter sql
  - Model FirewallPolicy has a new parameter explicit_proxy_settings
  - Model VirtualHub has a new parameter kind
  - Model ApplicationGatewayPathRule has a new parameter load_distribution_policy
  - Added operation BastionHostsOperations.begin_update_tags
  - Added operation group ServiceTagInformationOperations

## 19.0.0 (2021-05-14)

**Features**

  - Model ApplicationGatewayTrustedClientCertificate has a new parameter validated_cert_data
  - Model ApplicationGatewayTrustedClientCertificate has a new parameter client_cert_issuer_dn
  - Model VirtualNetwork has a new parameter flow_timeout_in_minutes
  - Model FrontendIPConfiguration has a new parameter gateway_load_balancer
  - Model IPAddressAvailabilityResult has a new parameter is_platform_reserved
  - Model CustomIpPrefix has a new parameter custom_ip_prefix_parent
  - Model CustomIpPrefix has a new parameter failed_reason
  - Model CustomIpPrefix has a new parameter child_custom_ip_prefixes
  - Model CustomIpPrefix has a new parameter authorization_message
  - Model CustomIpPrefix has a new parameter signed_message
  - Model VirtualNetworkPeering has a new parameter peering_sync_level
  - Model VirtualNetworkPeering has a new parameter resource_guid
  - Model VirtualNetworkPeering has a new parameter do_not_verify_remote_gateways
  - Model VirtualNetworkPeering has a new parameter type
  - Model VirtualNetworkPeering has a new parameter remote_virtual_network_address_space
  - Model Subnet has a new parameter application_gateway_ip_configurations
  - Model Subnet has a new parameter type
  - Model LoadBalancingRule has a new parameter backend_address_pools
  - Model EffectiveNetworkSecurityGroupAssociation has a new parameter network_manager
  - Model BastionHost has a new parameter sku
  - Model VirtualNetworkGateway has a new parameter extended_location
  - Model VirtualNetworkGateway has a new parameter nat_rules
  - Model VirtualNetworkGateway has a new parameter enable_bgp_route_translation_for_nat
  - Model NetworkInterface has a new parameter workload_type
  - Model NetworkInterface has a new parameter private_link_service
  - Model NetworkInterface has a new parameter nic_type
  - Model NetworkInterface has a new parameter migration_phase
  - Model Delegation has a new parameter type
  - Model PublicIPPrefix has a new parameter nat_gateway
  - Model VirtualNetworkGatewayConnection has a new parameter egress_nat_rules
  - Model VirtualNetworkGatewayConnection has a new parameter ingress_nat_rules
  - Model NetworkInterfaceIPConfiguration has a new parameter gateway_load_balancer
  - Model NetworkInterfaceIPConfiguration has a new parameter type
  - Model AvailablePrivateEndpointType has a new parameter display_name
  - Model PublicIPAddress has a new parameter delete_option
  - Model PublicIPAddress has a new parameter nat_gateway
  - Model PublicIPAddress has a new parameter service_public_ip_address
  - Model PublicIPAddress has a new parameter linked_public_ip_address
  - Model PublicIPAddress has a new parameter migration_phase
  - Model VirtualHub has a new parameter preferred_routing_gateway
  - Model BackendAddressPool has a new parameter tunnel_interfaces
  - Model ServiceTagInformationPropertiesFormat has a new parameter state
  - Added operation LoadBalancersOperations.begin_swap_public_ip_addresses
  - Added operation group VirtualNetworkGatewayNatRulesOperations

**Breaking changes**

  - Operation VirtualNetworkPeeringsOperations.begin_create_or_update has a new signature
  - Model VirtualNetworkGateway no longer has parameter virtual_network_extended_location

## 18.0.0 (2021-03-08)

**Features**

  - Model VpnConnection has a new parameter traffic_selector_policies
  - Model VirtualNetworkGateway has a new parameter virtual_network_extended_location
  - Model VirtualNetworkGateway has a new parameter v_net_extended_location_resource_id
  - Model VpnClientConfiguration has a new parameter vpn_authentication_types
  - Model LoadBalancerBackendAddress has a new parameter subnet
  - Model ServiceEndpointPolicy has a new parameter kind
  - Model FirewallPolicy has a new parameter snat
  - Model FirewallPolicy has a new parameter insights
  - Added operation VirtualNetworkGatewayConnectionsOperations.begin_reset_connection
  - Added operation VpnLinkConnectionsOperations.begin_get_ike_sas
  - Added operation VpnLinkConnectionsOperations.begin_reset_connection

**Breaking changes**

  - Model VirtualNetworkGateway no longer has parameter extended_location
  - Model VirtualNetworkGateway no longer has parameter virtual_network_extended_location_resource_id

## 17.1.0 (2021-01-26)

**Features**
  - Model PrivateEndpoint has a new parameter extended_location
  - Model VpnGateway has a new parameter nat_rules
  - Model ExpressRouteConnection has a new parameter express_route_gateway_bypass
  - Model SecurityRule has a new parameter type
  - Model PrivateLinkService has a new parameter extended_location
  - Model Route has a new parameter type
  - Model Route has a new parameter has_bgp_override
  - Model RouteTable has a new parameter resource_guid
  - Model VpnSiteLinkConnection has a new parameter ingress_nat_rules
  - Model VpnSiteLinkConnection has a new parameter vpn_link_connection_mode
  - Model VpnSiteLinkConnection has a new parameter egress_nat_rules
  - Model BackendAddressPool has a new parameter location
  - Model CustomIpPrefix has a new parameter extended_location
  - Added operation ExpressRouteGatewaysOperations.begin_update_tags
  - Added operation VirtualNetworkGatewayConnectionsOperations.begin_get_ike_sas
  - Added operation group NatRulesOperations

## 17.0.0 (2020-11-25)

**Features**

  - Model PublicIPPrefix has a new parameter extended_location
  - Model PublicIPPrefixSku has a new parameter tier
  - Model NatRule has a new parameter translated_fqdn
  - Model NetworkInterface has a new parameter extended_location
  - Model ApplicationRule has a new parameter terminate_tls
  - Model ApplicationRule has a new parameter web_categories
  - Model ApplicationRule has a new parameter target_urls
  - Model VirtualNetworkGatewayConnection has a new parameter connection_mode
  - Model LoadBalancer has a new parameter extended_location
  - Model PublicIPAddress has a new parameter extended_location
  - Model LoadBalancerSku has a new parameter tier
  - Model VirtualNetwork has a new parameter extended_location
  - Model P2SVpnGateway has a new parameter is_routing_preference_internet
  - Model IpGroup has a new parameter firewall_policies
  - Model VpnGateway has a new parameter is_routing_preference_internet
  - Model VirtualNetworkGateway has a new parameter extended_location
  - Model VirtualNetworkGateway has a new parameter virtual_network_extended_location_resource_id
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter connection_mode
  - Model FirewallPolicy has a new parameter sku
  - Model FirewallPolicy has a new parameter transport_security
  - Model FirewallPolicy has a new parameter identity
  - Model FirewallPolicy has a new parameter intrusion_detection
  - Model VirtualHub has a new parameter allow_branch_to_branch_traffic
  - Model PublicIPAddressSku has a new parameter tier
  - Model ServiceTagsListResult has a new parameter next_link
  - Model LoadBalancerBackendAddress has a new parameter load_balancer_frontend_ip_configuration
  - Added operation NetworkInterfacesOperations.list_cloud_service_network_interfaces
  - Added operation NetworkInterfacesOperations.get_cloud_service_network_interface
  - Added operation NetworkInterfacesOperations.list_cloud_service_role_instance_network_interfaces
  - Added operation PublicIPAddressesOperations.list_cloud_service_role_instance_public_ip_addresses
  - Added operation PublicIPAddressesOperations.list_cloud_service_public_ip_addresses
  - Added operation PublicIPAddressesOperations.get_cloud_service_public_ip_address
  - Added operation group WebCategoriesOperations

**Breaking changes**

  - Operation ConnectionMonitorsOperations.begin_create_or_update has a new signature
  - Model VirtualHub no longer has parameter enable_virtual_router_route_propogation

## 16.0.0 (2020-09-15)

**Features**

  - Model VirtualNetworkPeering has a new parameter remote_bgp_communities
  - Model VirtualHub has a new parameter virtual_router_asn
  - Model VirtualHub has a new parameter routing_state
  - Model VirtualHub has a new parameter ip_configurations
  - Model VirtualHub has a new parameter virtual_router_ips
  - Model VirtualHub has a new parameter enable_virtual_router_route_propogation
  - Model VirtualHub has a new parameter bgp_connections
  - Model FirewallPolicyRule has a new parameter description
  - Model ExpressRouteLinkMacSecConfig has a new parameter sci_state
  - Model VpnGateway has a new parameter ip_configurations
  - Model P2SConnectionConfiguration has a new parameter enable_internet_security
  - Model ConnectionMonitorEndpoint has a new parameter type
  - Model ConnectionMonitorEndpoint has a new parameter coverage_level
  - Model ConnectionMonitorEndpoint has a new parameter scope
  - Model FirewallPolicy has a new parameter rule_collection_groups
  - Model FirewallPolicy has a new parameter dns_settings
  - Model NetworkInterface has a new parameter dscp_configuration
  - Model NetworkVirtualAppliance has a new parameter address_prefix
  - Model NetworkVirtualAppliance has a new parameter cloud_init_configuration_blobs
  - Model NetworkVirtualAppliance has a new parameter boot_strap_configuration_blobs
  - Model NetworkVirtualAppliance has a new parameter cloud_init_configuration
  - Model NetworkVirtualAppliance has a new parameter inbound_security_rules
  - Model NetworkVirtualAppliance has a new parameter nva_sku
  - Model NetworkVirtualAppliance has a new parameter virtual_appliance_sites
  - Model ConnectionMonitorTcpConfiguration has a new parameter destination_port_behavior
  - Model ApplicationGatewayHttpListener has a new parameter ssl_profile
  - Model P2SVpnGateway has a new parameter custom_dns_servers
  - Model ApplicationGateway has a new parameter private_link_configurations
  - Model ApplicationGateway has a new parameter trusted_client_certificates
  - Model ApplicationGateway has a new parameter private_endpoint_connections
  - Model ApplicationGateway has a new parameter ssl_profiles
  - Model HubIPAddresses has a new parameter public_i_ps
  - Model PublicIPPrefix has a new parameter custom_ip_prefix
  - Model ApplicationGatewayFrontendIPConfiguration has a new parameter private_link_configuration
  - Model VpnSite has a new parameter o365_policy
  - Model ConnectivityHop has a new parameter previous_links
  - Model ConnectivityHop has a new parameter previous_hop_ids
  - Model ConnectivityHop has a new parameter links
  - Added operation ExpressRoutePortsOperations.generate_loa
  - Added operation FlowLogsOperations.update_tags
  - Added operation HubVirtualNetworkConnectionsOperations.begin_create_or_update
  - Added operation HubVirtualNetworkConnectionsOperations.begin_delete
  - Added operation VpnGatewaysOperations.begin_stop_packet_capture
  - Added operation VpnGatewaysOperations.begin_start_packet_capture
  - Added operation VpnGatewaysOperations.begin_update_tags
  - Added operation VpnConnectionsOperations.begin_stop_packet_capture
  - Added operation VpnConnectionsOperations.begin_start_packet_capture
  - Added operation PrivateLinkServicesOperations.begin_check_private_link_service_visibility_by_resource_group
  - Added operation PrivateLinkServicesOperations.begin_check_private_link_service_visibility
  - Added operation VirtualHubsOperations.begin_get_effective_virtual_hub_routes
  - Added operation P2SVpnGatewaysOperations.begin_reset
  - Added operation P2SVpnGatewaysOperations.begin_update_tags
  - Added operation group CustomIPPrefixesOperations
  - Added operation group VirtualApplianceSitesOperations
  - Added operation group DscpConfigurationOperations
  - Added operation group VirtualHubIpConfigurationOperations
  - Added operation group VirtualHubBgpConnectionOperations
  - Added operation group InboundSecurityRuleOperations
  - Added operation group VirtualApplianceSkusOperations
  - Added operation group ApplicationGatewayPrivateLinkResourcesOperations
  - Added operation group ApplicationGatewayPrivateEndpointConnectionsOperations
  - Added operation group FirewallPolicyRuleCollectionGroupsOperations
  - Added operation group VirtualHubBgpConnectionsOperations

**Breaking changes**

  - Model VirtualHub no longer has parameter virtual_network_connections
  - Model FirewallPolicyRule no longer has parameter priority
  - Model FirewallPolicy no longer has parameter transport_security
  - Model FirewallPolicy no longer has parameter rule_groups
  - Model FirewallPolicy no longer has parameter intrusion_system_mode
  - Model FirewallPolicy no longer has parameter identity
  - Model NetworkVirtualAppliance no longer has parameter boot_strap_configuration_blob
  - Model NetworkVirtualAppliance no longer has parameter sku
  - Model NetworkVirtualAppliance no longer has parameter cloud_init_configuration_blob
  - Model NatRuleCondition no longer has parameter terminate_tls
  - Model HubIPAddresses no longer has parameter public_ip_addresses
  - Model ApplicationRuleCondition no longer has parameter target_urls
  - Removed operation VpnGatewaysOperations.update_tags
  - Removed operation PrivateLinkServicesOperations.check_private_link_service_visibility_by_resource_group
  - Removed operation PrivateLinkServicesOperations.check_private_link_service_visibility
  - Removed operation P2SVpnGatewaysOperations.update_tags

## 16.0.0b1 (2020-06-17)

This is beta preview version.
For detailed changelog please refer to equivalent stable version 10.2.0 (https://pypi.org/project/azure-mgmt-network/10.2.0/)

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.


## 10.2.0 (2020-04-10)

**Features**

  - Model VpnConnection has a new parameter routing_configuration
  - Model NatRuleCondition has a new parameter terminate_tls
  - Model HubVirtualNetworkConnection has a new parameter routing_configuration
  - Model ExpressRouteConnection has a new parameter routing_configuration
  - Model FirewallPolicy has a new parameter transport_security
  - Model FirewallPolicy has a new parameter identity
  - Model FirewallPolicy has a new parameter threat_intel_whitelist
  - Model ApplicationRuleCondition has a new parameter target_urls
  - Model P2SConnectionConfiguration has a new parameter routing_configuration
  - Model BackendAddressPool has a new parameter load_balancer_backend_addresses
  - Added operation LoadBalancerBackendAddressPoolsOperations.create_or_update
  - Added operation LoadBalancerBackendAddressPoolsOperations.delete
  - Added operation group HubRouteTablesOperations

## 10.1.0 (2020-04-10)

**Features**

  - Model VpnConnection has a new parameter dpd_timeout_seconds
  - Model FirewallPolicy has a new parameter intrusion_system_mode
  - Model Subnet has a new parameter ip_allocations
  - Model ApplicationGateway has a new parameter force_firewall_policy_association
  - Model PrivateEndpoint has a new parameter custom_dns_configs
  - Model VirtualNetworkGatewayConnection has a new parameter dpd_timeout_seconds
  - Model VpnClientConfiguration has a new parameter radius_servers
  - Model VirtualNetwork has a new parameter ip_allocations
  - Model VirtualHub has a new parameter security_partner_provider
  - Model VpnServerConfiguration has a new parameter radius_servers
  - Added operation group PrivateDnsZoneGroupsOperations
  - Added operation group SecurityPartnerProvidersOperations
  - Added operation group IpAllocationsOperations

## 10.0.0 (2020-03-31)

**Features**

  - Model VirtualNetworkGatewayConnection has a new parameter use_local_azure_ip_address
  - Model NetworkRuleCondition has a new parameter source_ip_groups
  - Model NetworkRuleCondition has a new parameter destination_ip_groups
  - Model VirtualNetworkGatewayIPConfiguration has a new parameter private_ip_address
  - Model BgpSettings has a new parameter bgp_peering_addresses
  - Model ExpressRouteCircuitConnection has a new parameter ipv6_circuit_connection_config
  - Model ApplicationGatewayHttpListener has a new parameter host_names
  - Model ApplicationRuleCondition has a new parameter source_ip_groups
  - Model VirtualNetworkGateway has a new parameter enable_private_ip_address
  - Model LocalNetworkGateway has a new parameter fqdn
  - Model VpnSiteLink has a new parameter fqdn
  - Model NetworkSecurityGroup has a new parameter flow_logs
  - Added operation NetworkManagementClientOperationsMixin.put_bastion_shareable_link
  - Added operation NetworkManagementClientOperationsMixin.get_bastion_shareable_link
  - Added operation NetworkManagementClientOperationsMixin.delete_bastion_shareable_link
  - Added operation NetworkManagementClientOperationsMixin.disconnect_active_sessions
  - Added operation NetworkManagementClientOperationsMixin.get_active_sessions
  - Added operation group NetworkVirtualAppliancesOperations

**Breaking changes**

  - Model ApplicationGatewayHttpListener no longer has parameter hostnames

## 9.0.0 (2020-01-17)

**Features**

  - Model AzureFirewall has a new parameter ip_groups
  - Model AzureFirewall has a new parameter
    management_ip_configuration
  - Model ConnectionMonitorResult has a new parameter endpoints
  - Model ConnectionMonitorResult has a new parameter
    connection_monitor_type
  - Model ConnectionMonitorResult has a new parameter
    test_configurations
  - Model ConnectionMonitorResult has a new parameter test_groups
  - Model ConnectionMonitorResult has a new parameter outputs
  - Model ConnectionMonitorResult has a new parameter notes
  - Model AzureFirewallIPConfiguration has a new parameter type
  - Model ConnectionMonitor has a new parameter endpoints
  - Model ConnectionMonitor has a new parameter test_configurations
  - Model ConnectionMonitor has a new parameter test_groups
  - Model ConnectionMonitor has a new parameter outputs
  - Model ConnectionMonitor has a new parameter notes
  - Model DdosSettings has a new parameter protected_ip
  - Model ApplicationGatewayRewriteRuleActionSet has a new parameter
    url_configuration
  - Added operation
    P2sVpnGatewaysOperations.disconnect_p2s_vpn_connections
  - Added operation
    VirtualNetworkGatewaysOperations.disconnect_virtual_network_gateway_vpn_connections
  - Added operation group FlowLogsOperations

**Breaking changes**

  - Operation
    ExpressRouteCircuitAuthorizationsOperations.create_or_update has a
    new signature
  - Model ConnectionMonitorParameters has a new signature

## 8.0.0 (2019-11-12)

**Features**

  - Model PrivateLinkServiceConnectionState has a new parameter
    actions_required
  - Model ConnectivityParameters has a new parameter
    preferred_ip_version

**Breaking changes**

  - Model PrivateLinkServiceConnectionState no longer has parameter
    action_required

## 7.0.0 (2019-10-22)

**Features**

  - Model ApplicationGatewayHttpListener has a new parameter hostnames
  - Model ApplicationGatewayHttpListener has a new parameter
    firewall_policy
  - Model ApplicationGatewayPathRule has a new parameter
    firewall_policy
  - Model P2SVpnGateway has a new parameter
    p2_sconnection_configurations
  - Model VpnServerConfiguration has a new parameter
    vpn_client_root_certificates
  - Model VpnServerConfiguration has a new parameter
    radius_server_root_certificates
  - Model VpnServerConfiguration has a new parameter
    radius_client_root_certificates
  - Model VpnServerConfiguration has a new parameter
    vpn_client_revoked_certificates
  - Model ExpressRouteConnection has a new parameter
    enable_internet_security
  - Model AzureFirewallApplicationRule has a new parameter
    source_ip_groups
  - Model WebApplicationFirewallPolicy has a new parameter
    path_based_rules
  - Model WebApplicationFirewallPolicy has a new parameter
    http_listeners
  - Model PrivateLinkService has a new parameter enable_proxy_protocol
  - Model AzureFirewallNetworkRule has a new parameter
    destination_ip_groups
  - Model AzureFirewallNetworkRule has a new parameter
    source_ip_groups
  - Model AzureFirewallNetworkRule has a new parameter
    destination_fqdns
  - Model VirtualWAN has a new parameter virtual_wan_type
  - Model VirtualHub has a new parameter sku
  - Model VirtualHub has a new parameter virtual_hub_route_table_v2s
  - Model AzureFirewallNatRule has a new parameter translated_fqdn
  - Model AzureFirewallNatRule has a new parameter source_ip_groups
  - Model PrivateEndpointConnection has a new parameter link_identifier
  - Model AzureFirewall has a new parameter additional_properties
  - Added operation RouteFiltersOperations.update_tags
  - Added operation ServiceEndpointPoliciesOperations.update_tags
  - Added operation
    PrivateLinkServicesOperations.get_private_endpoint_connection
  - Added operation
    PrivateLinkServicesOperations.list_private_endpoint_connections
  - Added operation group VirtualHubRouteTableV2sOperations
  - Added operation group IpGroupsOperations

**Breaking changes**

  - Operation AzureFirewallsOperations.update_tags has a new signature
  - Operation
    ExpressRouteCircuitAuthorizationsOperations.create_or_update has a
    new signature
  - Model P2SVpnGateway no longer has parameter
    p2s_connection_configurations
  - Model VpnServerConfiguration no longer has parameter
    vpn_server_config_vpn_client_root_certificates
  - Model VpnServerConfiguration no longer has parameter
    vpn_server_config_radius_client_root_certificates
  - Model VpnServerConfiguration no longer has parameter
    vpn_server_config_vpn_client_revoked_certificates
  - Model VpnServerConfiguration no longer has parameter
    vpn_server_config_radius_server_root_certificates
  - Removed operation RouteFiltersOperations.update
  - Removed operation VirtualRoutersOperations.update
  - Removed operation RouteFilterRulesOperations.update
  - Removed operation VirtualRouterPeeringsOperations.update
  - Removed operation FirewallPoliciesOperations.update_tags
  - Removed operation ServiceEndpointPoliciesOperations.update

## 6.0.0 (2019-10-09)

**Features**

  - Model VirtualNetwork has a new parameter bgp_communities
  - Model VirtualHub has a new parameter azure_firewall
  - Model VirtualHub has a new parameter security_provider_name
  - Model P2SVpnGateway has a new parameter
    p2s_connection_configurations
  - Model P2SVpnGateway has a new parameter vpn_server_configuration
  - Model AzureFirewall has a new parameter sku
  - Model VirtualNetworkGateway has a new parameter
    inbound_dns_forwarding_endpoint
  - Model VirtualNetworkGateway has a new parameter
    enable_dns_forwarding
  - Added operation
    P2sVpnGatewaysOperations.get_p2s_vpn_connection_health_detailed
  - Added operation
    NetworkManagementClientOperationsMixin.generatevirtualwanvpnserverconfigurationvpnprofile
  - Added operation group VpnServerConfigurationsOperations
  - Added operation group
    VpnServerConfigurationsAssociatedWithVirtualWanOperations
  - Added operation group AvailableServiceAliasesOperations

**Breaking changes**

  - Model WebApplicationFirewallPolicy has a new required parameter
    managed_rules
  - Model P2SVpnGateway no longer has parameter
    vpn_client_address_pool
  - Model P2SVpnGateway no longer has parameter custom_routes
  - Model P2SVpnGateway no longer has parameter
    p2_svpn_server_configuration
  - Model VirtualWAN no longer has parameter security_provider_name
  - Model VirtualWAN no longer has parameter
    p2_svpn_server_configurations
  - Model PolicySettings has a new signature

## 5.1.0 (2019-10-03)

**Features**

  - Model VirtualNetworkGateway has a new parameter
    vpn_gateway_generation
  - Model ExpressRoutePort has a new parameter identity
  - Model VirtualNetworkGatewayConnection has a new parameter
    traffic_selector_policies
  - Model ExpressRouteLink has a new parameter mac_sec_config
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter
    traffic_selector_policies
  - Model NetworkInterfaceIPConfiguration has a new parameter
    private_link_connection_properties
  - Model ApplicationGatewayRequestRoutingRule has a new parameter
    priority
  - Added operation
    VirtualNetworkGatewayConnectionsOperations.stop_packet_capture
  - Added operation
    VirtualNetworkGatewayConnectionsOperations.start_packet_capture
  - Added operation ConnectionMonitorsOperations.update_tags
  - Added operation
    VirtualNetworkGatewaysOperations.stop_packet_capture
  - Added operation
    VirtualNetworkGatewaysOperations.start_packet_capture
  - Added operation group VirtualRoutersOperations
  - Added operation group VirtualRouterPeeringsOperations

## 5.0.0 (2019-08-27)

**Features**

  - Model PrivateLinkServiceIpConfiguration has a new parameter primary
  - Model PrivateLinkServiceIpConfiguration has a new parameter etag
  - Model PrivateLinkServiceIpConfiguration has a new parameter type
  - Model PrivateLinkServiceIpConfiguration has a new parameter id
  - Model AzureFirewall has a new parameter virtual_hub
  - Model AzureFirewall has a new parameter hub_ip_addresses
  - Model AzureFirewall has a new parameter firewall_policy
  - Model PrivateLinkServiceConnection has a new parameter
    provisioning_state
  - Model PrivateLinkServiceConnection has a new parameter etag
  - Model PrivateLinkServiceConnection has a new parameter type
  - Model PublicIPPrefix has a new parameter
    load_balancer_frontend_ip_configuration
  - Model ApplicationGatewayOnDemandProbe has a new parameter
    backend_address_pool
  - Model ApplicationGatewayOnDemandProbe has a new parameter
    backend_http_settings
  - Model PrivateEndpointConnection has a new parameter
    provisioning_state
  - Model PrivateEndpointConnection has a new parameter etag
  - Model PrivateEndpointConnection has a new parameter type
  - Added operation SubnetsOperations.unprepare_network_policies
  - Added operation group FirewallPolicyRuleGroupsOperations
  - Added operation group FirewallPoliciesOperations

**Breaking changes**

  - Model PrivateLinkServiceIpConfiguration no longer has parameter
    public_ip_address
  - Model ApplicationGatewayOnDemandProbe no longer has parameter
    backend_pool_name
  - Model ApplicationGatewayOnDemandProbe no longer has parameter
    backend_http_setting_name

## 4.0.0 (2019-07-19)

**Features**

  - Model Subnet has a new parameter
    private_link_service_network_policies
  - Model Subnet has a new parameter
    private_endpoint_network_policies
  - Model VpnSite has a new parameter vpn_site_links
  - Model LoadBalancingRule has a new parameter type
  - Model BackendAddressPool has a new parameter outbound_rules
  - Model BackendAddressPool has a new parameter type
  - Model InboundNatPool has a new parameter type
  - Model OutboundRule has a new parameter type
  - Model InboundNatRule has a new parameter type
  - Model Probe has a new parameter type
  - Model FrontendIPConfiguration has a new parameter
    private_ip_address_version
  - Model FrontendIPConfiguration has a new parameter type
  - Model AvailablePrivateEndpointType has a new parameter name
  - Model AvailablePrivateEndpointType has a new parameter
    resource_name
  - Model VpnConnection has a new parameter vpn_link_connections
  - Added operation
    AvailablePrivateEndpointTypesOperations.list_by_resource_group
  - Added operation AzureFirewallsOperations.update_tags
  - Added operation
    PrivateLinkServicesOperations.check_private_link_service_visibility_by_resource_group
  - Added operation
    PrivateLinkServicesOperations.list_auto_approved_private_link_services
  - Added operation
    PrivateLinkServicesOperations.check_private_link_service_visibility
  - Added operation
    PrivateLinkServicesOperations.list_auto_approved_private_link_services_by_resource_group
  - Added operation group VpnLinkConnectionsOperations
  - Added operation group VpnSiteLinkConnectionsOperations
  - Added operation group VpnSiteLinksOperations

**Breaking changes**

  - Operation SubnetsOperations.prepare_network_policies has a new
    signature
  - Model PrepareNetworkPoliciesRequest no longer has parameter
    resource_group_name
  - Model AvailablePrivateEndpointType no longer has parameter
    service_name
  - Removed operation group
    AvailableResourceGroupPrivateEndpointTypesOperations

## 3.0.0 (2019-05-24)

**Features**

  - Model NetworkInterface has a new parameter private_endpoint
  - Model ServiceAssociationLink has a new parameter type
  - Model ServiceAssociationLink has a new parameter allow_delete
  - Model ServiceAssociationLink has a new parameter locations
  - Model Subnet has a new parameter private_endpoints
  - Model PatchRouteFilter has a new parameter ipv6_peerings
  - Model ExpressRouteCircuitPeering has a new parameter type
  - Model ApplicationGatewayProbe has a new parameter port
  - Model RouteFilter has a new parameter ipv6_peerings
  - Model ExpressRouteCircuitAuthorization has a new parameter type
  - Model PeerExpressRouteCircuitConnection has a new parameter type
  - Model AzureFirewall has a new parameter zones
  - Model ResourceNavigationLink has a new parameter type
  - Model ExpressRouteCircuitConnection has a new parameter type
  - Model VpnConnection has a new parameter
    use_policy_based_traffic_selectors
  - Model NatGateway has a new parameter zones
  - Model VpnClientConfiguration has a new parameter aad_audience
  - Model VpnClientConfiguration has a new parameter aad_issuer
  - Model VpnClientConfiguration has a new parameter aad_tenant
  - Added operation
    VirtualNetworkGatewaysOperations.get_vpnclient_connection_health
  - Added operation
    P2sVpnGatewaysOperations.get_p2s_vpn_connection_health
  - Added operation VpnGatewaysOperations.reset
  - Added operation group BastionHostsOperations
  - Added operation group NetworkManagementClientOperationsMixin
  - Added operation group PrivateLinkServicesOperations
  - Added operation group
    AvailableResourceGroupPrivateEndpointTypesOperations
  - Added operation group ServiceAssociationLinksOperations
  - Added operation group ResourceNavigationLinksOperations
  - Added operation group ServiceTagsOperations
  - Added operation group PrivateEndpointsOperations
  - Added operation group AvailablePrivateEndpointTypesOperations

**Breaking changes**

  - Model NetworkInterface no longer has parameter interface_endpoint
  - Model Subnet no longer has parameter interface_endpoints
  - Removed operation group InterfaceEndpointsOperations

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes if you were importing from the v20xx_yy_zz
API folders. In summary, some modules were incorrectly
visible/importable and have been renamed. This fixed several issues
caused by usage of classes that were not supposed to be used in the
first place.

  - NetworkManagementClient cannot be imported from
    `azure.mgmt.network.v20xx_yy_zz.network_management_client`
    anymore (import from `azure.mgmt.network.v20xx_yy_zz` works like
    before)
  - NetworkManagementClientConfiguration import has been moved from
    `azure.mgmt.network.v20xx_yy_zz.network_management_client` to
    `azure.mgmt.network.v20xx_yy_zz`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using `azure.mgmt.network.v20xx_yy_zz.models.my_class`
    (import from `azure.mgmt.network.v20xx_yy_zz.models` works like
    before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.network.v20xx_yy_zz.operations.my_class_operations`
    (import from `azure.mgmt.network.v20xx_yy_zz.operations` works
    like before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 2.7.0 (2019-04-25)

**Features**

  - Model P2SVpnGateway has a new parameter custom_routes
  - Model Subnet has a new parameter nat_gateway
  - Model VpnConnection has a new parameter
    use_local_azure_ip_address
  - Model EffectiveRoute has a new parameter
    disable_bgp_route_propagation
  - Model VirtualNetworkGateway has a new parameter custom_routes
  - Added operation
    ApplicationGatewaysOperations.backend_health_on_demand
  - Added operation DdosProtectionPlansOperations.update_tags
  - Added operation group NatGatewaysOperations

**Bug fixes and preview API updates**

  - Parameter output_blob_sas_url of model
    GetVpnSitesConfigurationRequest is now required
  - Operation VpnSitesConfigurationOperations.download has a new
    signature
  - Model ExpressRouteCircuit no longer has parameter
    allow_global_reach

## 2.6.0 (2019-03-21)

**Features**

  - Model ApplicationGateway has a new parameter firewall_policy
  - Model ApplicationGatewayBackendHealthServer has a new parameter
    health_probe_log
  - Model ExpressRouteCircuitPeering has a new parameter
    peered_connections
  - Model ExpressRouteCircuit has a new parameter global_reach_enabled
  - Added operation group PeerExpressRouteCircuitConnectionsOperations
  - Added operation group WebApplicationFirewallPoliciesOperations

**Bugfixes**

  - Fix incorrect operation
    ApplicationGatewaysOperations.list_available_request_headers
  - Fix incorrect operation
    ApplicationGatewaysOperations.list_available_server_variables
  - Fix incorrect operation
    ApplicationGatewaysOperations.list_available_response_headers

## 2.6.0rc1 (2019-02-15)

**Features**

  - Model AzureFirewall has a new parameter threat_intel_mode
  - Model ApplicationGatewayRewriteRule has a new parameter conditions
  - Model ApplicationGatewayRewriteRule has a new parameter
    rule_sequence
  - Model ApplicationGatewayAutoscaleConfiguration has a new parameter
    max_capacity
  - Added operation SubnetsOperations.prepare_network_policies

## 2.5.1 (2019-01-15)

**Features**

  - Add missing ddos_custom_policies operations

## 2.5.0 (2019-01-04)

**Features**

  - Model PublicIPAddress has a new parameter ddos_settings
  - Added operation
    ApplicationGatewaysOperations.list_available_request_headers
  - Added operation
    ApplicationGatewaysOperations.list_available_server_variables
  - Added operation
    ApplicationGatewaysOperations.list_available_response_headers
  - Added operation ApplicationSecurityGroupsOperations.update_tags

## 2.4.0 (2018-11-27)

**Features**

  - Model ApplicationGatewaySslCertificate has a new parameter
    key_vault_secret_id
  - Model ApplicationGatewayRequestRoutingRule has a new parameter
    rewrite_rule_set
  - Model FlowLogInformation has a new parameter format
  - Model ApplicationGateway has a new parameter identity
  - Model ApplicationGateway has a new parameter rewrite_rule_sets
  - Model TrafficAnalyticsConfigurationProperties has a new parameter
    traffic_analytics_interval
  - Model ApplicationGatewayPathRule has a new parameter
    rewrite_rule_set
  - Model ApplicationGatewayUrlPathMap has a new parameter
    default_rewrite_rule_set

**Breaking changes**

  - Model ApplicationGatewayTrustedRootCertificate no longer has
    parameter keyvault_secret_id (replaced by key_vault_secret_id)

## 2.3.0 (2018-11-07)

**Features**

  - Model ApplicationGatewayWebApplicationFirewallConfiguration has a
    new parameter exclusions
  - Model ApplicationGatewayWebApplicationFirewallConfiguration has a
    new parameter file_upload_limit_in_mb
  - Model ApplicationGatewayWebApplicationFirewallConfiguration has a
    new parameter max_request_body_size_in_kb
  - Model ApplicationGatewayHttpListener has a new parameter
    custom_error_configurations
  - Model ExpressRouteCircuit has a new parameter bandwidth_in_gbps
  - Model ExpressRouteCircuit has a new parameter stag
  - Model ExpressRouteCircuit has a new parameter express_route_port
  - Model EvaluatedNetworkSecurityGroup has a new parameter applied_to
  - Model NetworkConfigurationDiagnosticResult has a new parameter
    profile
  - Model ApplicationGateway has a new parameter
    custom_error_configurations
  - Added operation group LoadBalancerOutboundRulesOperations
  - Added operation group ExpressRouteLinksOperations
  - Added operation group ExpressRoutePortsOperations
  - Added operation group ExpressRoutePortsLocationsOperations

**Breaking changes**

  - Model NetworkConfigurationDiagnosticResult no longer has parameter
    traffic_query
  - Operation
    NetworkWatchersOperations.get_network_configuration_diagnostic
    has a new signature (no longer takes target_resource_id, queries,
    but a NetworkConfigurationDiagnosticParameters instance)

## 2.2.1 (2018-09-14)

**Bugfixes**

  - Fix unexpected exception with network_profiles.delete

## 2.2.0 (2018-09-11)

Default API version is now 2018-08-01

**Features**

  - Model AzureFirewall has a new parameter nat_rule_collections
  - Model VirtualHub has a new parameter route_table
  - Model VirtualHub has a new parameter virtual_network_connections
  - Model VirtualHub has a new parameter p2_svpn_gateway
  - Model VirtualHub has a new parameter express_route_gateway
  - Model VirtualHub has a new parameter vpn_gateway
  - Model VirtualWAN has a new parameter allow_vnet_to_vnet_traffic
  - Model VirtualWAN has a new parameter
    p2_svpn_server_configurations
  - Model VirtualWAN has a new parameter
    office365_local_breakout_category
  - Model VirtualWAN has a new parameter
    allow_branch_to_branch_traffic
  - Model VirtualWAN has a new parameter security_provider_name
  - Model VpnSite has a new parameter is_security_site
  - Model VpnConnection has a new parameter connection_bandwidth
  - Model VpnConnection has a new parameter enable_internet_security
  - Model VpnConnection has a new parameter
    vpn_connection_protocol_type
  - Model VpnConnection has a new parameter enable_rate_limiting
  - Model ServiceEndpointPolicy has a new parameter subnets
  - Model AzureFirewallApplicationRule has a new parameter fqdn_tags
  - Model AzureFirewallApplicationRule has a new parameter target_fqdns
  - Model VpnGateway has a new parameter vpn_gateway_scale_unit
  - Model ApplicationGatewayBackendHttpSettings has a new parameter
    trusted_root_certificates
  - Model VirtualNetworkGatewayConnection has a new parameter
    connection_protocol
  - Model ExpressRouteCircuitPeering has a new parameter
    express_route_connection
  - Model Subnet has a new parameter delegations
  - Model Subnet has a new parameter address_prefixes
  - Model Subnet has a new parameter ip_configuration_profiles
  - Model Subnet has a new parameter service_association_links
  - Model Subnet has a new parameter interface_endpoints
  - Model Subnet has a new parameter purpose
  - Model ApplicationGateway has a new parameter
    trusted_root_certificates
  - Model NetworkInterface has a new parameter tap_configurations
  - Model NetworkInterface has a new parameter hosted_workloads
  - Model NetworkInterface has a new parameter interface_endpoint
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter
    connection_protocol
  - Model HubVirtualNetworkConnection has a new parameter
    enable_internet_security
  - Model NetworkInterfaceIPConfiguration has a new parameter
    virtual_network_taps
  - Added operation
    VirtualNetworkGatewaysOperations.reset_vpn_client_shared_key
  - Added operation group ExpressRouteConnectionsOperations
  - Added operation group AzureFirewallFqdnTagsOperations
  - Added operation group VirtualNetworkTapsOperations
  - Added operation group NetworkProfilesOperations
  - Added operation group P2sVpnServerConfigurationsOperations
  - Added operation group AvailableDelegationsOperations
  - Added operation group InterfaceEndpointsOperations
  - Added operation group P2sVpnGatewaysOperations
  - Added operation group AvailableResourceGroupDelegationsOperations
  - Added operation group ExpressRouteGatewaysOperations
  - Added operation group NetworkInterfaceTapConfigurationsOperations

**Breaking changes**

  - Model VirtualHub no longer has parameter
    hub_virtual_network_connections
  - Model VpnConnection no longer has parameter
    connection_bandwidth_in_mbps
  - Model AzureFirewallApplicationRule no longer has parameter
    target_urls
  - Model VpnGateway no longer has parameter policies
  - Model AzureFirewallIPConfiguration no longer has parameter
    internal_public_ip_address
  - Model ApplicationGatewayAutoscaleConfiguration has a new signature
  - Renamed virtual_wa_ns to virtual_wans

## 2.1.0 (2018-08-28)

Default API version is now 2018-07-01

**Features**

  - Model ExpressRouteCircuit has a new parameter allow_global_reach
  - Model PublicIPAddress has a new parameter public_ip_prefix
  - Model BackendAddressPool has a new parameter outbound_rule
    (replaces outbound_nat_rule)
  - Model FrontendIPConfiguration has a new parameter outbound_rules
    (replaces outbound_nat_rule)
  - Model FrontendIPConfiguration has a new parameter public_ip_prefix
  - Model LoadBalancingRule has a new parameter enable_tcp_reset
  - Model VirtualNetworkGatewayConnectionListEntity has a new parameter
    express_route_gateway_bypass
  - Model VirtualNetworkGatewayConnection has a new parameter
    express_route_gateway_bypass
  - Model Subnet has a new parameter service_endpoint_policies
  - Model InboundNatPool has a new parameter enable_tcp_reset
  - Model LoadBalancer has a new parameter outbound_rules (replaces
    outbound_nat_rule)
  - Model InboundNatRule has a new parameter enable_tcp_reset
  - Added operation group ServiceEndpointPolicyDefinitionsOperations
  - Added operation group ServiceEndpointPoliciesOperations
  - Added operation group PublicIPPrefixesOperations

**Breaking changes**

  - Model BackendAddressPool no longer has parameter outbound_nat_rule
    (now outbound_rules)
  - Model FrontendIPConfiguration no longer has parameter
    outbound_nat_rules (now outbound_rules)
  - Model LoadBalancer no longer has parameter outbound_nat_rules (now
    outbound_rules)

## 2.0.1 (2018-08-07)

**Bugfixes**

  - Fix packet_captures.get_status empty output

## 2.0.0 (2018-07-27)

**Features**

  - Supports now 2018-06-01 and 2018-04-01. 2018-06-01 is the new
    default.
  - Client class can be used as a context manager to keep the underlying
    HTTP session open for performance

**Features starting 2018-04-01**

  - Model FlowLogInformation has a new parameter
    flow_analytics_configuration
  - Model ApplicationGateway has a new parameter enable_fips
  - Model ApplicationGateway has a new parameter
    autoscale_configuration
  - Model ApplicationGateway has a new parameter zones
  - Model ConnectionSharedKey has a new parameter id
  - Added operation group HubVirtualNetworkConnectionsOperations
  - Added operation group AzureFirewallsOperations
  - Added operation group VirtualHubsOperations
  - Added operation group VpnGatewaysOperations
  - Added operation group VpnSitesOperations
  - Added operation group VirtualWANsOperations
  - Added operation group VpnSitesConfigurationOperations
  - Added operation group VpnConnectionsOperations

**Breaking changes starting 2018-04-01**

  - Operation
    VirtualNetworkGatewayConnectionsOperations.set_shared_key has a
    new parameter "id"
  - Operation DdosProtectionPlansOperations.create_or_update parameter
    "parameters" has been flatten to "tags/location"

**Breaking changes starting 2018-06-01**

  - The new class VpnConnection introduced in 2018-04-01 renamed
    "connection_bandwidth" to "connection_bandwidth_in_mbps"

## 2.0.0rc3 (2018-06-14)

**Bugfixes**

  - API version 2018-02-01 enum Probe now supports HTTPS (standard SKU
    load balancer)
  - API version 2015-06-15 adding missing "primary" in
    NetworkInterfaceIPConfiguration

## 2.0.0rc2 (2018-04-03)

**Features**

  - All clients now support Azure profiles.
  - API version 2018-02-01 is now the default
  - Express Route Circuit Connection (considered preview)
  - Express Route Provider APIs
  - GetTopologyOperation supports query parameter
  - Feature work for setting Custom IPsec/IKE policy for Virtual Network
    Gateway point-to-site clients
  - DDoS Protection Plans

## 2.0.0rc1 (2018-03-07)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**Network Breaking changes**

  - Operation network_watcher.get_topology changed method signature

**Features**

  - Add API Version 2018-01-01. Not default yet in this version.
  - Add ConnectionMonitor operation group (2017-10/11-01)
  - Add target_virtual_network / target_subnet to topology_parameter
    (2017-10/11-01)
  - Add idle_timeout_in_minutes / enable_floating_ip to
    inbound_nat_pool (2017-11-01)

**Bugfixes**

  - Fix peer_asn validation rules (2017-10/11-01)

## 1.7.1 (2017-12-20)

**Bugfixes**

Fix `SecurityRule` constructor parameters order to respect the one
used until 1.5.0. This indeed introduces a breaking change for users of
1.6.0 and 1.7.0, but this constructor signature change was not expected,
and following semantic versionning all 1.x versions should follow the
same signature.

This fixes third party library, like Ansible, that expects (for
excellent reasons) this SDK to follow strictly semantic versionning with
regards to breaking changes and have their dependency system asking for
`>=1.0;<2.0`

## 1.7.0 (2017-12-14)

**Features**

  - Add iptag. IpTag is way to restrict the range of IPaddresses to be
    allocated.
  - Default API version is now 2017-11-01

**Bug fixes**

  - Added valid ASN range in ExpressRouteCircuitPeering (#1672)

## 1.6.0 (2017-11-28)

**Bug fixes**

  - Accept space in location for "usage" (i.e. "west us").
  - sourceAddressPrefix, sourceAddressPrefixes and
    sourceApplicationSecurityGroups are mutually exclusive and one only
    is needed, meaning none of them is required by itself. Thus,
    sourceAddressPrefix is not required anymore.
  - destinationAddressPrefix, destinationAddressPrefixes and
    destinationApplicationSecurityGroups are mutually exclusive and one
    only is needed, meaning none of them is required by itself. Thus,
    destinationAddressPrefix is not required anymore.
  - Client now accept unicode string as a valid subscription_id
    parameter
  - Restore missing azure.mgmt.network.__version__

**Features**

  - Client now accept a "profile" parameter to define API version per
    operation group.
  - Add update_tags to most of the resources
  - Add operations group to list all available rest API operations
  - NetworkInterfaces_ListVirtualMachineScaleSetIpConfigurations
  - NetworkInterfaces_GetVirtualMachineScaleSetIpConfiguration

## 1.5.0 (2017-09-26)

**Features**

  - Availability Zones
  - Add network_watchers.get_azure_reachability_report
  - Add network_watchers.list_available_providers
  - Add virtual_network_gateways.supported_vpn_devices
  - Add virtual_network_gateways.vpn_device_configuration_script

## 1.5.0rc1 (2017-09-18)

**Features**

  - Add ApiVersion 2017-09-01 (new default)
  - Add application_security_groups (ASG) operations group
  - Add ASG to network_interface operations
  - Add ASG to IP operations
  - Add source/destination ASGs to network security rules
  - Add DDOS protection and VM protection to vnet operations

**Bug fix**

  - check_dns_name_availability now correctly defines
    "domain_name_label" as required and not optional

## 1.4.0 (2017-08-23)

**Features**

  - Add ApiVersion 2017-08-01 (new default)
  - Added in both 2017-08-01 and 2017-06-01:
      - virtual_network_gateways.list_connections method
      - default_security_rules operations group
      - inbound_nat_rules operations group
      - load_balancer_backend_address_pools operations group
      - load_balancer_frontend_ip_configurations operations group
      - load_balancer_load_balancing_rules operations group
      - load_balancer_network_interfaces operations group
      - load_balancer_probes operations group
      - network_interface_ip_configurations operations group
      - network_interface_load_balancers operations group
      - EffectiveNetworkSecurityGroup.tag_map attribute
      - EffectiveNetworkSecurityRule.source_port_ranges attribute
      - EffectiveNetworkSecurityRule.destination_port_ranges attribute
      - EffectiveNetworkSecurityRule.source_address_prefixes attribute
      - EffectiveNetworkSecurityRule.destination_address_prefixes
        attribute
      - SecurityRule.source_port_ranges attribute
      - SecurityRule.destination_port_ranges attribute
      - SecurityRule.source_address_prefixes attribute
      - SecurityRule.destination_address_prefixes attribute
  - Added in 2017-08-01 only
      - PublicIPAddress.sku
      - LoadBalancer.sku

**Changes on preview**

>   - "available_private_access_services" is renamed
>     "available_endpoint_services"
>   - "radius_secret" parsing fix (was unable to work in 1.3.0)

## 1.3.0 (2017-07-10)

**Preview features**

  - Adding "available_private_access_services" operation group
    (preview)
  - Adding "radius_secret" in Virtual Network Gateway (preview)

**Bug Fixes**

  - VMSS Network ApiVersion fix in 2017-06-01 (point to 2017-03-30)

## 1.2.0 (2017-07-03)

**Features**

Adding the following features to both 2017-03-01 and 2017-06-01:

  - express route ipv6
  - VMSS Network (get, list, etc.)
  - VMSS Public IP (get, list, etc.)

## 1.1.0 (2017-06-27)

**Features**

  - Add list_usage in virtual networks (2017-03-01)
  - Add ApiVersion 2017-06-01 (new default)

This new ApiVersion is for new Application Gateway features:

>   - ApplicationGateway Ssl Policy custom cipher suites support [new
>     properties added to Sslpolicy Property of
>     ApplciationGatewayPropertiesFormat]
>   - Get AvailableSslOptions api [new resource
>     ApplicationGatewayAvailableSslOptions and child resource
>     ApplicationGatewayPredefinedPolicy]
>   - Redirection support [new child resource
>     ApplicationGatewayRedirectConfiguration for Application Gateway,
>     new properties in UrlPathMap, PathRules and RequestRoutingRule]
>   - Azure Websites feature support [new properties in
>     ApplicationGatewayBackendHttpSettingsPropertiesFormat,
>     ApplicationGatewayProbePropertiesFormat, schema for property
>     ApplicationGatewayProbeHealthResponseMatch]

## 1.0.0 (2017-05-15)

  - Tag 1.0.0rc3 as stable (same content)

## 1.0.0rc3 (2017-05-03)

**Features**

  - Added check connectivity api to network watcher

## 1.0.0rc2 (2017-04-18)

**Features**

  - Add ApiVersion 2016-12-01 and 2017-03-01
  - 2017-03-01 is now default ApiVersion

**Bugfixes**

  - Restore access to NetworkWatcher and PacketCapture from 2016-09-01

## 1.0.0rc1 (2017-04-11)

**Features**

To help customers with sovereign clouds (not general Azure), this
version has official multi ApiVersion support for 2015-06-15 and
2016-09-01

## 0.30.1 (2017-03-27)

  - Add NetworkWatcher
  - Add PacketCapture
  - Add new methods to Virtualk Network Gateway
      - get_bgp_peer_status
      - get_learned_routes
      - get_advertised_routes

## 0.30.0 (2016-11-01)

  - Initial preview release. Based on API version 2016-09-01.

## 0.20.0 (2015-08-31)

  - Initial preview release. Based on API version 2015-05-01-preview.
