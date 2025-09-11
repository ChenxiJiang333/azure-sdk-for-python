# Azure Monitor OTEL SDK not working

## question 
Hi there, I am trying to try to use the (Azure Monitor OTEL Exporter)[https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter#microsoft-opentelemetry-exporter-for-azure-monitor] for a python application, and I am having trouble getting data flow when I follow the examples of setting up the exporter. I tried to copy the (hello world sample code)[https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter#export-hello-world-trace] and put my connection string, and I'm still not seeing any tracing data land in my traces table in my App Insights instance. Could I get some help here to figure out what is going on, or where the sample code might not be functional?

I tried to look through the debug logs:
```
2025-05-20 22:57:57,387 DEBUG urllib3.connectionpool Starting new HTTP connection (1): 169.254.169.254:80
2025-05-20 22:57:57,396 DEBUG urllib3.connectionpool http://169.254.169.254:80 "GET /metadata/instance/compute?api-version=2017-12-01&format=json HTTP/1.1" 200 636
2025-05-20 22:57:57,400 INFO azure.core.pipeline.policies.http_logging_policy Request URL: 'https://westus-0.in.applicationinsights.azure.com//v2.1/track'
Request method: 'POST'
Request headers:
    'Content-Type': 'application/json'
    'Content-Length': '1545'
    'Accept': 'application/json'
    'x-ms-client-request-id': 'defa6d6e-35cd-11f0-a616-3bc028b7fd3a'
    'User-Agent': 'azsdk-python-azuremonitorclient/unknown Python/3.10.12 (Linux-6.5.0-1025-azure-x86_64-with-glibc2.35)'
A body is sent with the request
2025-05-20 22:57:57,401 DEBUG urllib3.connectionpool Starting new HTTPS connection (1): westus-0.in.applicationinsights.azure.com:443
2025-05-20 22:57:57,663 DEBUG urllib3.connectionpool https://westus-0.in.applicationinsights.azure.com:443 "POST /v2.1/track HTTP/1.1" 200 None
2025-05-20 22:57:57,663 INFO azure.core.pipeline.policies.http_logging_policy Response status: 200
Response headers:
    'Transfer-Encoding': 'chunked'
    'Content-Type': 'application/json; charset=utf-8'
    'Server': 'Microsoft-HTTPAPI/2.0'
    'Strict-Transport-Security': 'REDACTED'
    'X-Content-Type-Options': 'REDACTED'
    'Date': 'Tue, 20 May 2025 22:57:56 GMT'
Hello, World!
2025-05-20 22:57:57,666 INFO azure.core.pipeline.policies.http_logging_policy Request URL: 'https://eastus-8.in.applicationinsights.azure.com//v2.1/track'
Request method: 'POST'
Request headers:
    'Content-Type': 'application/json'
    'Content-Length': '1610'
    'Accept': 'application/json'
    'x-ms-client-request-id': 'df22f14e-35cd-11f0-a616-3bc028b7fd3a'
    'User-Agent': 'azsdk-python-azuremonitorclient/unknown Python/3.10.12 (Linux-6.5.0-1025-azure-x86_64-with-glibc2.35)'
A body is sent with the request
2025-05-20 22:57:57,667 DEBUG urllib3.connectionpool Starting new HTTPS connection (1): eastus-8.in.applicationinsights.azure.com:443
2025-05-20 22:57:57,742 DEBUG urllib3.connectionpool https://eastus-8.in.applicationinsights.azure.com:443 "POST /v2.1/track HTTP/1.1" 200 None
2025-05-20 22:57:57,742 INFO azure.core.pipeline.policies.http_logging_policy Response status: 200
Response headers:
    'Transfer-Encoding': 'chunked'
    'Content-Type': 'application/json; charset=utf-8'
    'Server': 'Microsoft-HTTPAPI/2.0'
    'Strict-Transport-Security': 'REDACTED'
    'X-Content-Type-Options': 'REDACTED'
    'Date': 'Tue, 20 May 2025 22:57:56 GMT'
2025-05-20 22:57:57,743 INFO azure.monitor.opentelemetry.exporter.export._base Transmission succeeded: Item received: 2. Items accepted: 2
2025-05-20 22:57:57,745 INFO azure.core.pipeline.policies.http_logging_policy Request URL: 'https://westus-0.in.applicationinsights.azure.com//v2.1/track'
Request method: 'POST'
Request headers:
    'Content-Type': 'application/json'
    'Content-Length': '1573'
    'Accept': 'application/json'
    'x-ms-client-request-id': 'df2ef098-35cd-11f0-a616-3bc028b7fd3a'
    'User-Agent': 'azsdk-python-azuremonitorclient/unknown Python/3.10.12 (Linux-6.5.0-1025-azure-x86_64-with-glibc2.35)'
A body is sent with the request
2025-05-20 22:57:57,745 DEBUG urllib3.connectionpool Starting new HTTPS connection (2): westus-0.in.applicationinsights.azure.com:443
2025-05-20 22:57:58,001 DEBUG urllib3.connectionpool https://westus-0.in.applicationinsights.azure.com:443 "POST /v2.1/track HTTP/1.1" 200 None
2025-05-20 22:57:58,001 INFO azure.core.pipeline.policies.http_logging_policy Response status: 200
Response headers:
    'Transfer-Encoding': 'chunked'
    'Content-Type': 'application/json; charset=utf-8'
    'Server': 'Microsoft-HTTPAPI/2.0'
    'Strict-Transport-Security': 'REDACTED'
    'X-Content-Type-Options': 'REDACTED'
    'Date': 'Tue, 20 May 2025 22:57:57 GMT'
```

Sample code:
```
"""
An example to show an application using Opentelemetry tracing api and sdk. Custom dependencies are
tracked via spans and telemetry is exported to application insights with the AzureMonitorTraceExporter.
"""

import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
import logging

# Enable detailed debug logging for Azure Monitor and OpenTelemetry
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
# Increase verbosity for key components
for logger_name in [
    "azure.monitor.opentelemetry",
    "azure.core.pipeline.policies.http_logging_policy",
    "azure.monitor.opentelemetry.exporter",
    "opentelemetry",
    "opentelemetry.sdk.trace",
    "opentelemetry.sdk.trace.export",
]:
    logging.getLogger(logger_name).setLevel(logging.DEBUG)

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)
# This is the exporter that sends data to Application Insights
exporter = AzureMonitorTraceExporter(
    connection_string="InstrumentationKey=c0b360fa-422d-40e5-b8a9-d642578f9fce;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=087d527c-b60e-4346-a679-f6abf367d0f0"
)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

with tracer.start_as_current_span("hello"):
    print("Hello, World!")

# Telemetry records are flushed automatically upon application exit
# If you would like to flush records manually yourself, you can call force_flush()
tracer_provider.force_flush()
```

## answer
The traces table in appinsights is populated by the logging exporter. See examples here-> (azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry-exporter/samples/logs at main · Azure/azure-sdk-for-python)[https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter/samples/logs]

If you want your data from your spans in app insights, they would appear in the requests/dependncies table in appinsights depending on if you are making outbound or inbound requests. You can view your span attributes being mappedin custom dimensions field in appinsights. Please refer to the official documentation -> (Microsoft OpenTelemetry exporter for Azure Monitor | Microsoft Learn)[https://learn.microsoft.com/en-us/python/api/overview/azure/monitor-opentelemetry-exporter-readme?view=azure-python-preview]

Please keep in mind that using the exporter directly is experimental but it seems like your use case is specific in nature that you need to work with the components itself instead of via the distro?

# Failed to start record

## question 
Hi team, I was getting internal server error from test-proxy when I tried to run tests on a commit of main branch. The following shows the local variables in the scope of `tools\azure-sdk-tools\devtools_testutils\proxy_testcase.py#L91`.
```
result.auto_close = True
result.chunk_left = None
result.chunked = False
result.closed = True
result.connection = None
result.data = b''
result.decode_content = True
result.enforce_content_length = True
result.headers = HTTPHeaderDict({'Content-Length': '0', 'Date': 'Tue, 13 Mar 2025 10:59:00 GMT'})
result.length_remaining = 0
result.msg = None
result.reason = 'Internal Server Error'
result.retries = Retry(total=3, connect=None, read=None, redirect=None, status=None)
result.status = 500
result.url = '/record/start'
result.version = 11
result.version_string = 'HTTP/1.1'
result._body = b''
```
The following text is the error message.
```
:\Source\Repos\azure-sdk-for-python\sdk\webpubsub\azure-messaging-webpubsubservice\tests\test_reverse_proxy.py::TestWebpubsubReverseProxy::test_reverse_proxy_call failed: args = (<test_reverse_proxy.TestWebpubsubReverseProxy object at 0x000001BE9CF45310>,)
kwargs = {'__aggregate_cache_key': ('EnvironmentVariableLoader',), 'webpubsub_connection_string': 'Endpoint=https://wps-prod-se...ps-prod-seasia.webpubsub.azure.com', 'webpubsub_reverse_proxy_endpoint': 'https://wps-prod-seasia.webpubsub.azure.com'}
trimmed_kwargs = {'webpubsub_connection_string': 'Endpoint=https://wps-prod-seasia.webpubsub.azure.com;AccessKey=<redated>;Version=1.0;', 'webpubsub_reverse_proxy_endpoint': 'https://wps-prod-seasia.webpubsub.azure.com'}
test_id = 'sdk/webpubsub/azure-messaging-webpubsubservice/tests/recordings/test_reverse_proxy.pyTestWebpubsubReverseProxytest_reverse_proxy_call'

    def record_wrap(*args, **kwargs):
        def transform_args(*args, **kwargs):
            copied_positional_args = list(args)
            request = copied_positional_args[1]
    
            transform_request(request, recording_id)
    
            return tuple(copied_positional_args), kwargs
    
        trimmed_kwargs = {k: v for k, v in kwargs.items()}
        trim_kwargs_from_test_function(test_func, trimmed_kwargs)
    
        if is_live_and_not_recording():
            return test_func(*args, **trimmed_kwargs)
    
        test_id = get_test_id()
>       recording_id, variables = start_record_or_playback(test_id)

tools\azure-sdk-tools\devtools_testutils\proxy_testcase.py:194: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

test_id = 'sdk/webpubsub/azure-messaging-webpubsubservice/tests/recordings/test_reverse_proxy.pyTestWebpubsubReverseProxytest_reverse_proxy_call'

    def start_record_or_playback(test_id: str) -> "Tuple[str, Dict[str, str]]":
        """Sends a request to begin recording or playing back the provided test.
    
        This returns a tuple, (a, b), where a is the recording ID of the test and b is the `variables` dictionary that maps
        test variables to values. If no variable dictionary was stored when the test was recorded, b is an empty dictionary.
        """
        variables = {}  # this stores a dictionary of test variable values that could have been stored with a recording
    
        json_payload = {"x-recording-file": test_id}
        assets_json = get_recording_assets(test_id)
        if assets_json:
            json_payload["x-recording-assets-file"] = assets_json
    
        encoded_payload = json.dumps(json_payload).encode("utf-8")
        http_client = get_http_client()
    
        if is_live():
            result = http_client.request(
                method="POST",
                url=RECORDING_START_URL,
                body=encoded_payload,
            )
            if result.status != 200:
                message = six.ensure_str(result.data)
>               raise HttpResponseError(message=message)
E               azure.core.exceptions.HttpResponseError: Operation returned an invalid status 'None'

tools\azure-sdk-tools\devtools_testutils\proxy_testcase.py:93: HttpResponseError
```

The commit is 7f659e62a6689e45276f75255b3fb9fcf8fbba1f 
To reproduce the issue, try run the test in `sdk\webpubsub\azure-messaging-webpubsubservice\tests` in live test mode. Any troubleshooting guide for the test-proxy? 

## answer
It's absolutely a conflict with the repo assuming you will always have an assets.json tag present. So when it attempts to restore a tag that doesn't exist, it crashes.

I definitely think that we can improve the error handling to make this a bit more visible to you. On proxy output side it's readily visible.

So. For you. I would recommend the following to unblock yourself.
1. in your env or active shell session, set PROXY_URL=http://localhost:5000. I have reason to believe that we have an issue with newer versions of the async libraries over default https certificate
2. delete your .assets folder, then update your assets.json to the following content before rerunning your tests
```
{
  "AssetsRepo": "Azure/azure-sdk-assets",
  "AssetsRepoPrefixPath": "python",
  "TagPrefix": "python/webpubsub/azure-messaging-webpubsubservice",
  "Tag": ""
}
```

Once you successfully record new recordings, test-proxy push and your Tag will be properly populated.

# Question Regarding Regression in Python SDK v11.0.0 for Container Registry

## question
Hi Language - Python, I'm from the Azure Container Registry team, and we have a question regarding one of the recent SDK releases.

The release in question is v11.0.0 ([AutoRelease] t2-containerregistry-2024-12-10-60943(can only be merged by SDK owner) by azure-sdk · Pull Request #38810 · Azure/azure-sdk-for-python), which was generated based on this Swagger PR Savaradh containerregistry microsoft.container registry 2024 11 01 preview new by savaradh · Pull Request #31612 · Azure/azure-rest-api-specs

We recently noticed a regression in version 11.0.0: Previously, the _create_initial method returned a deserialized Task object, but in v11.0.0, it now returns a streamed response. This change was not mentioned in the changelog. 

Additionally, our Swagger PR did not modify the 2019-06-01-preview/containerregistry_build.json file, so we're unsure why the SDK PR includes changes to these operation files.

In the "removed" lines (lines 503-507 in red), there was code that did:
```
if response.status_code == 200:
    deserialized = self._deserialize("Task", pipeline_response)
if response.status_code == 201:  
    deserialized = self._deserialize("Task", pipeline_response)
```
But in the current version (line 496 in green), it's doing:
```
deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)
```

Could someone help us understand the root cause of this issue? Any insights would be greatly appreciated. Thanks

## answer
This was a change made in the code generator a while ago, and it's basically an implementation detail change in the public generated code. `_create_initial` is a private method that is used to set up the initial call to start the polling in `begin_create`. We just switched over our initial calls to not do premature deserialization, and there is 0 customer impact. Hope this clears stuff up!

# OOB Stable Python SDK

## question
Hi Language - Python team, I'm trying to release Python SDK here: https://github.com/Azure/sdk-release-request/issues/6124 which is required to test and release Azure CLI module. Given that CLI has a deadline of next week for code complete, I have a couple of questions around this:

1. Can this SDK be released out of band ASAP?
2. For future iterations, what's the process we should take to align with CLI releases, so that we have enough time to release SDKs and then release CLI as well?
Thanks

## answer
1. SDK team will release this package in advance to unblock CLI. Add Chenxi Jiang (WICRESOFT NORTH AMERICA LTD) for awareness.
2. If CLI module depends on SDK, it is better to make release request issue earlier so that SDK team could prepare the release in advance.

# GA review

## question
Hi all, we're looking to release our first stable Python SDK in (Deid GA release by jovinson-ms · Pull Request #40850 · Azure/azure-sdk-for-python)[https://github.com/Azure/azure-sdk-for-python/pull/40850]. Would appreciate a look at the APIView, as we pulled in some suggested client customization from Java and .NET reviews but would like feedback on whether they are idiomatic to Python.

## answer
Hi, I would recommend making a post in the (Language - Python - Reviews)[https://teams.microsoft.com/l/channel/19%3A4175567f1e154a80ab5b88cbd22ea92f%40thread.skype/Language%20-%20Python%20-%20Reviews?groupId=3e17dcb0-4257-4a30-b843-77f47f1d4121&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47] channel

# Changelog release requirements

## question
Hi all, I'm trying to release our data plane SDK's first stable version in (Deid GA release by jovinson-ms · Pull Request #40850 · Azure/azure-sdk-for-python)[https://github.com/Azure/azure-sdk-for-python/pull/40850]. I'm getting (build failures on changelog validation)[https://dev.azure.com/azure-sdk/public/_build/results?buildId=4824427&view=logs&j=b70e5e73-bbb6-5567-0939-8415943fadb9&t=ac8f4042-9b76-5db4-27b1-2a4abaa9bb3c&l=101]. Looking through the docs, I don't see any changelog update process for data plane in contrast to the control plane automation. Can someone help me understand what the process is here?

## answer
You didn't update the base version of the package! Appears to still be `1.0.0b1`
I believe it should be `1.0.0` to match the changelog you added

# CSpell config

## question
Hi all, I know there are common CSpell config settings as .vscode/cspell.json. I also see a few package-level cspell config files checked in: (Code search results)[https://github.com/search?q=repo%3AAzure%2Fazure-sdk-for-python+path%3Acspell.json&type=code]. Is there some config that needs to be set for pipelines to use local cspell config?

## answer
We haven't done this in the SDK repos yet but we intend to allow folks to inherit from the root file.  Similar to https://github.com/Azure/azure-rest-api-specs/blob/main/specification/communication/cspell.yaml where it imports the root cspell config. So as long as you inherit it should work.

# Disable Pylint checks on .pyi files

## question
Hi all,
 
Storage is adding .pyi files for each of our clients to move `kwargs` to named keywords without having to make massive changes to our runtime code. We have noticed that pylint still runs on these .pyi files and a lot of the checks just don't make sense there, for example `super-init-not-called`. Obviously super init would not be called in a stub.

Example PR: ([Storage] [Named Keywords] [Blob] `_container_client.pyi` and aio by weirongw23-msft · Pull Request #41030 · Azure/azure-sdk-for-python)[https://github.com/Azure/azure-sdk-for-python/pull/41030/files]

This is causing us to have to put in a bunch of pylint disables. Curious on everyone's thoughts on simply disabling pylint on stub files entirely?

## answer
You could consider using `Unpack` with `TypedDict` to handle the typing of kwargs? In the long term it would probably be a lower maintenance solution (it also allows the addition of documentation in intellisense prompts - which the current pyi file doesn't seem to have). 
Here's an example if you want to have a read through:
(azure-sdk-for-python/sdk/projects/azure-projects/azure/projects/resources/storage/_resource.py at main · Azure/azure-sdk-for-python)[https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/projects/azure-projects/azure/projects/resources/storage/_resource.py#L237-L243]

# Python Storage SDK - `walk_blobs` API

## question
Hi Anna and Kashif Khan,
 
(A customer mentioned)[https://github.com/Azure/azure-sdk-for-python/issues/40873] that `walk_blobs` API could return `BlobPrefix` where the current rtype is just `BlobProperties`. Based on this feedback, it appears that `walk_blob` needs to have rtype `BlobProperties | BlobPrefix` ((PR)[https://github.com/Azure/azure-sdk-for-python/pull/40931]). However, this would be a breaking change to our customers, and it would be harder to work with as the customer needs to type check themselves, so not great.
 
In .NET, `GetBlobsByHierarchy` (returns a custom type)[https://github.com/Azure/azure-sdk-for-net/blob/6ee19685b3c1ecc7f9d7b6318954b12708dcc179/sdk/storage/Azure.Storage.Blobs/src/BlobContainerClient.cs#L2713-L2773] of `Pageable<BlobHierarchyItem>` which has a Boolean value to check whether the item is `BlobPrefix` or `BlobProperties`.
 
We'd like some feedback on how to best proceed here. Thanks!

## answer
To clarify, changing the type hint is not a breaking change, just annoying to work with a Union return type. The other options of introducing a wrapper class however, would be breaking obviously.
If this is already acting that way at runtime, it means people already use `isintance` or `try/except AttributeError` anyway, so the `Union` still make things better.
