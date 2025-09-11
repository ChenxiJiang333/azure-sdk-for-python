# Python test run failed using pytest

## question 
Hi team,
I was following the instructions to add a test for the Python SDK: [Dataplane Codegen Quick Start for Test · Azure/azure-sdk-for-python Wiki](https://github.com/Azure/azure-sdk-for-python/wiki/Dataplane-Codegen-Quick-Start-for-Test)
I created a .env file containing the CONVERSATIONS_ENDPOINT and CONVERSATIONS_KEY, and tried placing it either alongside the azure-sdk-for-python repo folder, or inside the repo root at azure-sdk-for-python/.env. When I run pytest, I get the following error:
```
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='localhost', port=5001): 
Max retries exceeded with url: /playback/start 
(Caused by NewConnectionError: Failed to establish a new connection: 
[WinError 10061] No connection could be made because the target machine actively refused it)
```
And this is my test: [test_create_project.py](https://github.com/Azure/azure-sdk-for-python/blob/02348a1d6eb5abe69e0ac0d67c2f5164d8dca638/sdk/cognitivelanguage/azure-ai-language-conversations-authoring/tests/test_create_project.py):
```
import functools
import pytest

from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer, recorded_by_proxy
from azure.ai.language.conversations.authoring import AuthoringClient
from azure.ai.language.conversations.authoring.models import ConversationAuthoringCreateProjectDetails 

from azure.core.credentials import AzureKeyCredential

ConversationsPreparer = functools.partial(
    PowerShellPreparer, 'conversations',
    conversations_endpoint="fake_resource.servicebus.windows.net/",
    conversations_key="fake_key"
)

class TestConversations(AzureRecordedTestCase):

# Start with any helper functions you might need, for example a client creation method:
    def create_client(self, endpoint, key):
        credential = AzureKeyCredential(key)
        client = AuthoringClient(endpoint, credential)
        return client

    ...

class TestConversationsCase(TestConversations):
    @ConversationsPreparer()
    @recorded_by_proxy
    def test_conversation_prediction(self, conversations_endpoint, conversations_key):
        client = self.create_client(conversations_endpoint, conversations_key)

        # Access the project operation group separately 
        project_client = client.conversation_authoring_project 

        # Define project name and creation details 
        project_name = "MyPythonProject0723" 
        project_data = ConversationAuthoringCreateProjectDetails( 
            project_kind="Conversation", 
            project_name=project_name,
            language="en-us", 
            multilingual=True, 
            description="Project description" 
        ) 

        # Create the project 
        response = project_client.create_project( 
            project_name=project_name, 
            body=project_data 
        ) 

        # Print confirmation 
        print(f"Project created: {response.project_name}, Kind: {response.project_kind}, Language: {response.language}")
```
Could you please take a look and let me know what I might be missing? Thank you!

## answer
Hi, it looks like the test proxy hasn't actually started up before your tests run, so requests to the endpoint aren't connecting. You'll need to add a conftest.py file to your tests directory that invokes the test_proxy fixture, per these instructions: https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/tests.md#start-the-test-proxy-server:
```
Start the test proxy server

The test proxy has to be available in order for tests to work; this is done automatically with a pytest fixture.

Create a conftest.py file within your package's test directory (sdk/{service}/{package}/tests), and inside it add a session-level fixture that accepts the test_proxy fixture as a parameter (and has autouse set to True):

import pytest

# autouse=True will trigger this fixture on each pytest run, even if it's not explicitly used by a test method
# test_proxy auto-starts the test proxy
# patch_sleep and patch_async_sleep streamline tests by disabling wait times during LRO polling
@pytest.fixture(scope="session", autouse=True)
def start_proxy(test_proxy, patch_sleep, patch_async_sleep):
    return

As shown in the example, it's recommended to also request the patch_sleep and patch_async_sleep fixtures unless your tests have a unique need to use time.sleep or asyncio.sleep during playback tests (this is unusual). All of these fixtures are imported by the central /sdk/conftest.py, so pytest will automatically resolve the references.

For more details about how this fixture starts up the test proxy, or the test proxy itself, refer to the test proxy migration guide.
```
 
Looking at the [test documentation](https://github.com/Azure/azure-sdk-for-python/wiki/Dataplane-Codegen-Quick-Start-for-Test) that you linked, we forgot to include this guidance -- I just updated the page to fix that. Thank you for letting us know!
