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
