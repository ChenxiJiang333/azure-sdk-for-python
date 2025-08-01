# Azure SDK Migration Guide: New Hybrid Operation Design Generation Breaking Changes

The direct link to this page can be found at aka.ms/azsdk/python/migrate/hybrid-operations

This guide covers the breaking changes you'll encounter when upgrading to our new operation design and how to fix them in your code.

Our new hybrid operations are named as such because they have a dual dictionary and operation nature.

## Summary of Breaking Changes

When migrating to the hybrid operation design, expect these breaking changes:

| Change                                                                              | Impact                                                    | Quick Fix                                                                         |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [Query/Header Parameters](#queryheader-parameters-requiring-keywords) | Query and header signatures changed from positional to keyword-only | Convert all positional parameters to keyword arguments |
| [ETag Parameters](#etag-parameters-restructured) | header signatures `if_match`/`if_none_match` restructured to `etag/match_condition` | Replace `if_match="etag"` with `etag="etag", match_condition=MatchConditions.IfNotModified` |

## Detailed Breaking Changes

### Query/Header Parameters Requiring Keywords

**What changed**: Query and header parameters in operation methods have been changed from positional to keyword-only to improve clarity and prevent parameter order mistakes.

**What will break**:

- Code that passes positional parameters

**Before**:

```python
from azure.mgmt.confluent import ConfluentManagementClient

client = ConfluentManagementClient(credential, subscription_id)

# Query parameters can be passed positionally
environments = client.organization_operations.list_environments(
    "resource_group",
    "org_name", 
    10,        # Pass page_size as positional
    "token"    # Pass page_token as positional
)
```

**After**:

```python
from azure.mgmt.confluent import ConfluentManagementClient

client = ConfluentManagementClient(credential, subscription_id)

# ❌ Raises TypeError
environments = client.organization_operations.list_environments(
    "resource_group",
    "org_name", 
    10,
    "token"
)

# ✅ Use these approaches instead
environments = client.organization_operations.list_environments(
    "resource_group",
    "org_name",
    page_size=10,         # Must be passed with a keyword
    page_token="token"    # Must be passed with a keyword
)
```

**Migration steps:**

- Convert all positional parameters to keyword arguments

### ETag Parameters Restructured

**What changed**: Conditional request headers `if_match` and `if_none_match` have been replaced with more semantic `etag` and `match_condition` parameters that use enum values for better type safety.

**What will break**:

- Code using `if_match` or `if_none_match` parameters

**Before**:

```python
from azure.mgmt.containerservicefleet import ContainerServiceFleetManagementClient

client = ContainerServiceFleetManagementClient(credential, subscription_id)

fleet = client.fleets.begin_create_or_update(
    resource_group_name="rg",
    fleet_name="fleet1", 
    resource=fleet_operation,
    if_match="etag-value"
)
```

**After**:

```python
from azure.mgmt.containerservicefleet import ContainerServiceFleetManagementClient
from azure.core.matching import MatchConditions

client = ContainerServiceFleetManagementClient(credential, subscription_id)

# New ETag parameters with enum
fleet = client.fleets.begin_create_or_update(
    resource_group_name="rg",
    fleet_name="fleet1",
    resource=fleet_operation,
    etag="etag-value",
    match_condition=MatchConditions.IfModified
)
```

**Migration steps:**

- Import `MatchConditions` from `azure.core.matching`
- Replace `if_match="etag-value"` with `etag="etag-value", match_condition=MatchConditions.IfNotModified`
- Replace `if_none_match="etag-value"` with `etag="etag-value", match_condition=MatchConditions.IfModified`

**MatchConditions enum values:**
- `MatchConditions.IfNotModified` - Equivalent to `if_match` (update only if resource hasn't changed)
- `MatchConditions.IfModified` - Equivalent to `if_none_match` (update only if resource has changed)  
- `MatchConditions.IfPresent` - Update only if resource exists
- `MatchConditions.IfMissing` - Update only if resource doesn't exist

## Why These Changes?

Our hybrid operations prioritize consistency with the underlying REST API:

- **Improved Code Readability**: Method calls become self-documenting when parameters are named.
- **Prevents Parameter Order Mistakes**: Keyword-only parameters eliminate bugs caused by passing arguments in the wrong order.

If you encounter issues not covered here, please file an issue on [GitHub](https://github.com/microsoft/typespec/issues) with tag `emitter:client:python`.
