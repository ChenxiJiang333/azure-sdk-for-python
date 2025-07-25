**GOAL**

Generate issue title and issue body for users

**Context**

- PACKAGE-NAME: "azure-mgmt-authorization"
- REST-REPO-URL: "https://github.com/Azure/azure-rest-api-specs"
- ISSUE-TITLE-TEMPLATE: `[resource manager] Python: Release request for Release for {SERVICE-NAME} (convert to singleapi)`
- CURRENT-DATE: {current Month/DAY+4/Year} (e.g. 07/24/2025)
- ISSUE-BODY-TEMPLATE:

```
{TARGET-URL}
->Readme Tag: Xxx
## Release request for <i>Release for {SERVICE-NAME}</i>
**Requested by @msyyc**
**Link**: [{TARGET-URL}]({TARGET-URL})  
**Namespace Approval Issue**:
**Readme Tag**: Xxx
**Target release date**: No later than {CURRENT-DATE} 
```

**Step**

1. Search PACKAGE-NAME with REST-REPO-URL. If there is file named "readme.python.md" that contains PACKAGE-NAME, remember the README URL of the file
2. Get SERVICE-NAME which is next part of "specification" in README URL
3. TARGET-URL is parent url of README URL
4. Output issue title with ISSUE-TITLE-TEMPLATE
5. Output issue title with ISSUE-BODY-TEMPLATE
