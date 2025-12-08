# Release History

## tsp migration

### Breaking Changes

  - Deleted or renamed client `CertificateRegistrationMgmtClient`
  - Model `AppServiceCertificateOrder` moved instance variable `certificates`, `distinguished_name`, `domain_verification_token`, `validity_in_years`, `key_size`, `product_type`, `auto_renew`, `provisioning_state`, `status`, `signed_certificate`, `csr`, `intermediate`, `root`, `serial_number`, `last_certificate_issuance_time`, `expiration_time`, `is_private_key_external`, `app_service_certificate_not_renewable_reasons`, `next_auto_renewal_time_stamp` and `contact` under property `properties`
  - Model `AppServiceCertificateOrderPatchResource` moved instance variable `certificates`, `distinguished_name`, `domain_verification_token`, `validity_in_years`, `key_size`, `product_type`, `auto_renew`, `provisioning_state`, `status`, `signed_certificate`, `csr`, `intermediate`, `root`, `serial_number`, `last_certificate_issuance_time`, `expiration_time`, `is_private_key_external`, `app_service_certificate_not_renewable_reasons`, `next_auto_renewal_time_stamp` and `contact` under property `properties`
  - Model `AppServiceCertificatePatchResource` moved instance variable `key_vault_id`, `key_vault_secret_name` and `provisioning_state` under property `properties`
  - Model `AppServiceCertificateResource` moved instance variable `key_vault_id`, `key_vault_secret_name` and `provisioning_state` under property `properties`
  - Model `DetectorResponse` moved instance variable `metadata`, `dataset`, `status`, `data_providers_metadata` and `suggested_utterances` under property `properties`
  - Model `ReissueCertificateOrderRequest` moved instance variable `key_size`, `delay_existing_revoke_in_hours`, `csr` and `is_private_key_external` under property `properties`
  - Model `RenewCertificateOrderRequest` moved instance variable `key_size`, `csr` and `is_private_key_external` under property `properties`
  - Deleted model `AppServiceCertificateCollection`/`AppServiceCertificateOrderCollection`/`CsmOperationCollection`/`DetectorResponseCollection` which actually were not used by SDK users
  - Method `CertificateOrdersDiagnosticsOperations.get_app_service_certificate_order_detector_response` changed its parameter `start_time`/`end_time`/`time_grain` from `positional_or_keyword` to `keyword_only`

## 1.0.0b1 (2025-12-08)

### Other Changes

  - Initial version