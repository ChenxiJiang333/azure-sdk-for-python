# Release History

## 1.0.0b2 (2025-11-11)

### Breaking Changes

  - Deleted or renamed client `WebSiteManagementClient`
  - Model `AppServiceCertificateOrder` instance variables `certificates`, `distinguished_name`, `domain_verification_token`, `validity_in_years`, `key_size`, `product_type`, `auto_renew`, `provisioning_state`, `status`, `signed_certificate`, `csr`, `intermediate`, `root`, `serial_number`, `last_certificate_issuance_time`, `expiration_time`, `is_private_key_external`, `app_service_certificate_not_renewable_reasons`, `next_auto_renewal_time_stamp`, and `contact` have been moved under property `properties`
  - Model `AppServiceCertificateOrderPatchResource` instance variables `certificates`, `distinguished_name`, `domain_verification_token`, `validity_in_years`, `key_size`, `product_type`, `auto_renew`, `provisioning_state`, `status`, `signed_certificate`, `csr`, `intermediate`, `root`, `serial_number`, `last_certificate_issuance_time`, `expiration_time`, `is_private_key_external`, `app_service_certificate_not_renewable_reasons`, `next_auto_renewal_time_stamp`, and `contact` have been moved under property `properties`
  - Model `AppServiceCertificatePatchResource` instance variables `key_vault_id`, `key_vault_secret_name`, and `provisioning_state` have been moved under property `properties`
  - Model `AppServiceCertificateResource` instance variables `key_vault_id`, `key_vault_secret_name`, and `provisioning_state` have been moved under property `properties`
  - Model `DetectorResponse` instance variables `metadata`, `dataset`, `status`, `data_providers_metadata`, and `suggested_utterances` have been moved under property `properties`
  - Model `ReissueCertificateOrderRequest` instance variables `key_size`, `delay_existing_revoke_in_hours`, `csr`, and `is_private_key_external` have been moved under property `properties`
  - Model `RenewCertificateOrderRequest` instance variables `key_size`, `csr`, and `is_private_key_external` have been moved under property `properties`
  - Method `CertificateOrdersDiagnosticsOperations.get_app_service_certificate_order_detector_response` changed its parameter `start_time` from `positional_or_keyword` to `keyword_only`
  - Method `CertificateOrdersDiagnosticsOperations.get_app_service_certificate_order_detector_response` changed its parameter `end_time` from `positional_or_keyword` to `keyword_only`
  - Method `CertificateOrdersDiagnosticsOperations.get_app_service_certificate_order_detector_response` changed its parameter `time_grain` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed model `AppServiceCertificateCollection`
  - Deleted or renamed model `AppServiceCertificateOrderCollection`
  - Deleted or renamed model `CsmOperationCollection`
  - Deleted or renamed model `DetectorResponseCollection`

## 1.0.0b1 (2025-11-11)

### Other Changes

  - Initial version
