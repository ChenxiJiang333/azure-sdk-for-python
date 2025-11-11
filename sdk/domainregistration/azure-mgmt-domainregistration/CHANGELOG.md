# Release History

## 1.0.0b2 (2025-11-11)

### Breaking Changes

  - Deleted or renamed client `WebSiteManagementClient`
  - Model `Domain` instance variables `contact_admin`, `contact_billing`, `contact_registrant`, `contact_tech`, `registration_status`, `provisioning_state`, `name_servers`, `privacy`, `created_time`, `expiration_time`, `last_renewed_time`, `auto_renew`, `ready_for_dns_record_management`, `managed_host_names`, `consent`, `domain_not_renewable_reasons`, `dns_type`, `dns_zone_id`, `target_dns_type`, and `auth_code` have been moved under property `properties`
  - Model `DomainOwnershipIdentifier` instance variable `ownership_id` has been moved under property `properties`
  - Model `DomainPatchResource` instance variables `contact_admin`, `contact_billing`, `contact_registrant`, `contact_tech`, `registration_status`, `provisioning_state`, `name_servers`, `privacy`, `created_time`, `expiration_time`, `last_renewed_time`, `auto_renew`, `ready_for_dns_record_management`, `managed_host_names`, `consent`, `domain_not_renewable_reasons`, `dns_type`, `dns_zone_id`, `target_dns_type`, and `auth_code` have been moved under property `properties`
  - Model `TopLevelDomain` instance variable `privacy` has been moved under property `properties`
  - Method `DomainsOperations.delete` changed its parameter `force_hard_delete_domain` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed model `CsmOperationCollection`
  - Deleted or renamed model `DomainCollection`
  - Deleted or renamed model `DomainOwnershipIdentifierCollection`
  - Deleted or renamed model `NameIdentifierCollection`
  - Deleted or renamed model `TldLegalAgreementCollection`
  - Deleted or renamed model `TopLevelDomainCollection`

## 1.0.0b1 (2025-11-11)

### Other Changes

  - Initial version
