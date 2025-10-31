# CHANGELOG Optimization Guide

This document provides rules and guidelines for optimizing and standardizing CHANGELOG entries. Apply these rules to ensure consistency and clarity in documentation.

## Overview

When optimizing a CHANGELOG, **ONLY** make necessary updates that ensure the log completely meets the conditions of the rules while respecting the original format.

## CHANGELOG

```
CHANGELOG_CONTENT
```

## Optimization Rules

### 1. Operation Group Naming

Standardize the naming of operation groups for consistency.

**Before:**
```
Added model ...Operations
```

**After:**
```
Added operation group ...Operations
```

### 2. Parameter Default Value Changes

Transform default value change descriptions into more user-friendly language.

#### 2.1 Required Parameters
**Before:**
```
`A` removed default value None from its parameter `B`
```

**After:**
```
Parameter `B` of `A` is now required
```

#### 2.2 Optional Parameters
**Before:**
```
`A` parameter `B` changed default value from ... to none
```

**After:**
```
Parameter `B` of `A` is now optional
```

### 3. Entries to Remove

The following types of entries should be removed as they are not relevant for end users:

1. **Method overloads:**
   ```
   Method `...` has a new overload `...`
   ```

2. **Internal property changes:**
   ```
   Model `...` deleted or renamed its instance variable `additional_properties`
   ```

### 4. Parameter Renaming

When both insertion and deletion of parameters occur together, merge them into a single rename entry.

**Before:**
```
`A` inserted a `positional_or_keyword` parameter `C`
`A` deleted or renamed its parameter `B` of kind `positional_or_keyword`
```

**After:**
```
`A` renamed its instance variable `B` to `C`
```

### 5. Grouping Moved Instance Variables Under a New Container Property

When a model introduces a new container property (commonly named `properties`) and multiple instance variables of that model are subsequently reported as "deleted or renamed", treat these as a structural move rather than separate deletions. Consolidate the repeated deletion/rename lines into a single, clearer entry indicating that the variables were moved under the new property.

**Before:**
```
   - Model `A` added property `properties`
   - Model `A` deleted or renamed its instance variable `a`
   - Model `A` deleted or renamed its instance variable `b`
   - Model `A` deleted or renamed its instance variable `c`
```

**After:**
```
   - Model `A` added property `properties`
   - Model `A` moved instance variable `a`, `b` and `c` under property `properties`
```

### 6. Hybrid Model Migration Note

When a CHANGELOG contains one or more entries in the `### Breaking Changes` section of the form:
```
Model `X` deleted or renamed its instance variable `y`
```
this often indicates a transition to new "hybrid models" (models that behave both like dictionaries and typed models). In such cases, insert the following standardized migration note as the FIRST bullet (or line) directly under the `### Breaking Changes` heading:

```
This version introduces new hybrid models which have dual dictionary and model nature. Please follow https://aka.ms/azsdk/python/migrate/hybrid-models for migration.
```

Rules / Constraints:
1. Add the note only if at least one matching instance-variable deletion/rename line exists.
2. Do not add the note if it already exists (avoid duplicates).
3. Preserve the original ordering of the existing breaking change entries after inserting the note.

**Before:**
```
### Breaking Changes
- Model `A` deleted or renamed its instance variable `a`
- Model `B` deleted or renamed its instance variable `b`
```

**After:**
```
### Breaking Changes
- This version introduces new hybrid models which have dual dictionary and model nature. Please follow https://aka.ms/azsdk/python/migrate/hybrid-models for migration.
- Model `A` deleted or renamed its instance variable `a`
- Model `B` deleted or renamed its instance variable `b`
```

If multiple such lines are present, the note is still inserted only once.
