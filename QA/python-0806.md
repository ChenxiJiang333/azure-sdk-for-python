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
