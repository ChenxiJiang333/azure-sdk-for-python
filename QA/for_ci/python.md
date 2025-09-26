# Python Live Test for async api

## question 
Hello Language - Python,

We at Callautomation are working on adding live tests for the async APIs. When I tried to run a live test, I encountered an SSL certificate issue, as shown below. Could you help me understand what I might be missing?

```
        except aiohttp.client_exceptions.ClientError as err:
>           raise ServiceRequestError(err, error=err) from err
E           azure.core.exceptions.ServiceRequestError: Cannot connect to host localhost:5001 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1028)')]

C:\Users\v-dharmarajv\AppData\Local\Programs\Python\Python313\Lib\site-packages\azure\core\pipeline\transport\_aiohttp.py:364: ServiceRequestError
```

## answer
You're encountering an SSL certificate error when running live tests for async APIs, specifically when connecting to https://localhost:5001. This is the test proxy endpoint, and the error is likely due to certificate verification failing. Although the same code works for another team member, the issue may be caused by environment variables — either missing or incorrectly set.

To run live tests, make sure AZURE_TEST_RUN_LIVE is set to "true". If you also want to record, avoid setting AZURE_SKIP_LIVE_RECORDING. As a workaround for the SSL issue, set the environment variable PROXY_URL to http://localhost:5000 instead of using HTTPS. This bypasses certificate validation and resolves the issue.

# release pipeline link for Python SDK `azure-mgmt-resource-bicep`

## question

How to find the specific release pipeline link of Python SDK `azure-mgmt-resource-bicep` and it would be nicer if someone can provide me the link directly.

## answer

To find the specific release pipeline link for the Python SDK `azure-mgmt-resource-bicep`, you typically need to locate the corresponding pipeline in Azure DevOps under the internal Azure SDK project. The naming convention for the pipeline is usually `python - <servicedir>`, where `<servicedir>` matches the service directory (in this case, likely resource or resource-bicep).

Here is the general process:
1. Go to [Azure DevOps - Azure SDK Internal Project](https://dev.azure.com/azure-sdk/internal/_build)
2. Search for the pipeline named `python - resource` or similar, as the pipeline is named according to the service directory for management SDKs.
3. The direct link format for a service pipeline is: `https://dev.azure.com/azure-sdk/internal/_build?definitionId=<ID>&_a=summary`
- You can search for `resource` in the pipelines list to locate the exact one.

# Is test recordings working in azure-sdk-for-python-pr repo?

## question

I wrote test code in a topic branch in `azure-sdk-for-python-pr` repo (https://github.com/Azure/azure-sdk-for-python-pr/tree/dargilco/agents-v2-tests-part-1/sdk/ai/azure-ai-agents-v2).
 
I define 
set AZURE_TEST_RUN_LIVE=true
set AZURE_SKIP_LIVE_RECORDING=false
 
and run the tests, but no ".assets" folder is created. The test complete successfully without any errors.
 
I am following the same test writing guidelines that I used successfully to record test in the `azure-sdk-for-python` repo, therefore I want to check on the status of recording support in `azure-sdk-for-python-pr`. Thanks!

## answer

Based on the available information, if you are running tests in the azure-sdk-for-python-pr repo with AZURE_TEST_RUN_LIVE=true and AZURE_SKIP_LIVE_RECORDING=false, and no .assets folder is being created (but tests pass), it likely indicates that the recording migration (to out-of-repo assets) has not yet been completed or set up for your package/branch in the azure-sdk-for-python-pr repository.

The current Azure SDK test infrastructure expects the following when running live tests:

If the package has been migrated to use the test proxy and out-of-repo recordings, running live tests with the correct environment variables should create/update the .assets directory at the root of the repo. This directory contains the local sparse clone of the required recordings.
If your package has not been migrated, the recordings may still be expected in the old /tests/recordings folder structure, or the test proxy integration may not be fully configured in the PR branch.

Key points from the documentation:

"If tests were recorded for a new library, there should now be a folder called recordings inside your package's tests directory. Each recording in this folder will be a .json file... The final step in setting up recordings is to move these files out of the azure-sdk-for-python and into the azure-sdk-assets repository."
After migration: "These recording updates will be reflected in a git-excluded .assets folder at the root of the repo."
If you do not see a .assets folder, it likely means the test proxy migration is not yet in place or fully set up for your topic branch.

Recommended next steps:

Confirm if your package in azure-sdk-for-python-pr has been migrated to use the test proxy and out-of-repo recordings. Look for an assets.json file at the package root and .assets at the repo root.
If not migrated, refer to the recording migration guide for the migration process.
If migrated and still no .assets folder is created, verify that your test environment and variables are set up as required (including git version and credentials), and consult the test proxy troubleshooting guide.

Summary:Your observation suggests that the recording support via the .assets folder is not yet active for your branch or package in the azure-sdk-for-python-pr repo. This could be due to the migration not being completed, or the package not being configured for out-of-repo recordings yet. Please check the migration status or reach out to the repo maintainers for confirmation.

# Confirming Actual Release Date Based on Changelog?

## question

Hi team,
Quick question — in the PR for our package (`azure-mgmt-hdinsight`), the CHANGELOG.md lists the release date as `2025-10-19` for version `9.1.0b2`.
Just wanted to confirm: Is the actual release date determined by the date shown in the changelog?
If not, how can I find out the actual release date?
Thanks!

## answer

The release date shown in the CHANGELOG.md (e.g., 2025-10-19 for version 9.1.0b2) is not what actually determines the official release date of the package. The date in the changelog is meant to document when the release was prepared and what changes are included, but the actual release date is determined by when the package is published to PyPI (or the official distribution channel) after the release process is completed.
As part of the Azure SDK release process, maintainers are instructed to ensure the changelog is accurate and matches the release, but the true release date is when the package is published, not the date listed in the changelog.
So, you should not rely solely on the date in the changelog as the authoritative release date. Always refer to the package's publication timestamp on PyPI or the Azure SDK release tracking tools for the actual release date.
