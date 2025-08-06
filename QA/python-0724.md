# The date for the changelog being released must be the latest in the file.

## question 
We have this PR to Main branch that updates CHANGELOG.md: https://github.com/Azure/azure-sdk-for-python/pull/42064 . The change looks correct to me... adding `## 1.0.0b13 (Unreleased)`. Yet the PR build pipeline has an error in the Analyze job titled "Verify ChangeLogEntries":
```
[debug]Verifying as a release build because the changelog entry has a valid date.
##[error]Invalid date [ 2025-06-23 ]. The date for the changelog being released must be the latest in the file.
##[debug]Processed: ##vso[task.LogIssue type=error;]Invalid date [ 2025-06-23 ]. The date for the changelog being released must be the latest in the file.
##[debug]$LASTEXITCODE: 1

##[debug]Exit code 1 received from tool '/usr/bin/pwsh'
##[debug]STDIO streams have closed for tool '/usr/bin/pwsh'
##[debug]task result: Failed
##[error]PowerShell exited with code '1'.
##[debug]Processed: ##vso[task.issue type=error;source=TaskInternal;correlationId=98b16427-6102-4a6a-a6a6-3227b7c530df;]PowerShell exited with code '1'.
##[debug]Processed: ##vso[task.complete result=Failed;]PowerShell exited with code '1'.
Finishing: Verify ChangeLogEntries
```
 
Any idea why? Seems like a tool bug to me.

## answer
The error occurred because the changelog entry for version `1.0.0b13 (Unreleased)` was added without updating the `_version.py` file. the tool gets the version from there and tries to validate the change log entry for that version. In this case it sees that version isn't the latest version in the changelog and complains (granted the error message could be better). However, the version update is what is missing. Also, looks like a lot of version increment PRs have been getting ignored. It might be worth taking these PR and then pulling them into your feature branches. However if you don't plan to use them then just close them.
