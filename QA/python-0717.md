# API View Displays Incorrect Python Package Name

## question 
Hi team,
 
I am generating the Python SDK api view for sdk review meeting. After I followed the instruction here to generate Python package: [What to do after generating the SDK code with codegen · Azure/azure-sdk-for-python Wiki](https://github.com/Azure/azure-sdk-for-python/wiki/What-to-do-after-generating-the-SDK-code-with-codegen#how-to-create-package). It generate a package name like this: **azure_ai_language_text-1.0.0b1-py3-none-any.whl**, with long suffix. And after uploading it to Api view, it still keep the same long name:
`azure_ai_language_text-1.0.0b1-py3-none-any.whl`
But I noticed that in the previous version api view, the Python namespace only show simplified verison like this :
`azure-ai-language-conversations`
Should I manually modify the package name before uploading it to api view, or is there anything that I was missing? Thank you!

## answer
Hi, this is a bug in the parser and an issue is filed for it here. [[Python APIView\] manual uploads have the whl as the title name · Issue #10459 · Azure/azure-sdk-tools](https://github.com/Azure/azure-sdk-tools/issues/10459)
 
I'm currently working on fixing this. Is there a particular reason for the manual upload? Otherwise, you can auto-generate the APIView with the correct name by opening up a PR in the azure-sdk-for-python repo with the changes.

# Python Live Test for async api

## question 
Hello Language - Python,
 
We at Callautomation are working on adding live tests for the async APIs. When I tried to run a live test, I encountered an SSL certificate issue, as shown below. Could you help me understand what I might be missing?
 
```
        except aiohttp.client_exceptions.ClientError as err:
>           raise ServiceRequestError(err, error=err) from err
E           azure.core.exceptions.ServiceRequestError: Cannot connect to host localhost:5001 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1028)')]
```
 
C:\Users\v-dharmarajv\AppData\Local\Programs\Python\Python313\Lib\site-packages\azure\core\pipeline\transport\_aiohttp.py:364: ServiceRequestError

## answer
You're encountering an SSL certificate error when running live tests for async APIs, specifically when connecting to https://localhost:5001. This is the test proxy endpoint, and the error is likely due to certificate verification failing. Although the same code works for another team member, the issue may be caused by environment variables — either missing or incorrectly set.

To run live tests, make sure AZURE_TEST_RUN_LIVE is set to "true". If you also want to record, avoid setting AZURE_SKIP_LIVE_RECORDING. As a workaround for the SSL issue, set the environment variable PROXY_URL to http://localhost:5000 instead of using HTTPS. This bypasses certificate validation and resolves the issue.
 