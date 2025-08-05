# SecurityInsights missing credential_scope update when targeting azure gov cloud

## question 
Hey Team, Not sure if its a bug or rather a missing feature. But when utilizing (azure.mgmt.securityinsight.SecurityInsights class | Microsoft Learn)[https://learn.microsoft.com/en-us/python/api/azure-mgmt-securityinsight/azure.mgmt.securityinsight.securityinsights?view=azure-python] and specifying the base_url to point to azure gov - Along with the ClientSecretCredential pointing to us gov. The credential_Scope doesn't get updated. Instead it will fail with: 
```
(InvalidAuthenticationTokenAudience) The 'EvolvedSecurityTokenService' access token has been obtained for wrong audience or resource 'https://management.azure.com'. It should exactly match with one of the allowed audiences 'https://management.core.usgovcloudapi.net/','https://management.core.usgovcloudapi.net','https://management.usgovcloudapi.net/','https://management.usgovcloudapi.net'.
Code: InvalidAuthenticationTokenAudience
```
Had to dig into the sdk to understand how to override this... basically, we are just passing in the credential_scopes which will get passed thru 
-> https://github.com/Azure/azure-sdk-for-python/blob/6e86b7a2820bf1db476f9505cdad4b51f2dd00ab/sdk/securityinsight/azure-mgmt-securityinsight/azure/mgmt/securityinsight/_security_insights.py#L174 
```
self._config = SecurityInsightsConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
```
-- TO---> https://github.com/Azure/azure-sdk-for-python/blob/6e86b7a2820bf1db476f9505cdad4b51f2dd00ab/sdk/securityinsight/azure-mgmt-securityinsight/azure/mgmt/securityinsight/_configuration.py#L55
```
self.credential_scopes = kwargs.pop("credential_scopes", ["https://management.azure.com/.default"])
```

Working Example found here: (Sentinel_Rules_Gov_Example/test_sentinel.py at main · VinnyBonner/Sentinel_Rules_Gov_Example)[https://github.com/VinnyBonner/Sentinel_Rules_Gov_Example/blob/main/test_sentinel.py]
```
SUBSCRIPTION_ID = '<SUBSCRIPTION_ID>'
RESOURCE_GRP = '<RESOURCE_GROUP_NAME>'
WORKSPACES = ['<WORKSPACE_NAME>']
CLIENT_ID = '<CLIENT_ID>'
TENANT_ID = '<TENANT_ID>'


AZURE_GOVERNMENT_AUTHORITY = "https://login.microsoftonline.us/"
AZURE_GOVERNMENT_MANAGEMENT = "https://management.usgovcloudapi.net"
SCOPE = "https://management.usgovcloudapi.net/.default"

class Sentinel:
    """Use RestAPI to communicate with Sentinel directly"""

    def __init__(self, secret: str) -> None:
        """Info needed to connect, authenticate to Sentinel"""

        self.creds = ClientSecretCredential(tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=secret, authority=AZURE_GOVERNMENT_AUTHORITY, base_url=AZURE_GOVERNMENT_MANAGEMENT)

    def __enter__(self) -> Sentinel:
        if 'Windows' in platform.system():  # avoid certificate validation on Windows???
            os.environ['REQUESTS_CA_BUNDLE'] = ''
            os.environ['CURL_CA_BUNDLE'] = ''
        try:
            self.client = SecurityInsights(credential=self.creds, subscription_id=SUBSCRIPTION_ID, base_url=AZURE_GOVERNMENT_MANAGEMENT, credential_scopes=[SCOPE])
        except (ValueError, ClientAuthenticationError) as err:
            print(f'unable to authenticate to sentinel: {err}')
        return self
```
 
Easy way to break it and reproduce the error is update line 36 by removing the credential_scopes kwargs - update line 36 to the below
```
self.client = SecurityInsights(credential=self.creds, subscription_id=SUBSCRIPTION_ID, base_url=AZURE_GOVERNMENT_MANAGEMENT)
```
 
This will reproduce the issue. 
 
So the question / reason for the post... 
Can you consider one of the following: 
Update documentation so developers know they also need to pass in the credential_scope
OR
Update the code so that it will use the base_url passed in plus the /.default for the credential_scope when creating the config
 
Just some way so that customers working in the gov space know how to properly configure the code to connect to the sovereign clouds like US GOV FairFax.
 
Happy to demo/walk thru if you need it since it does require gov sub. 
 
Thanks!

## answer
Thanks for the feedback. Here is the doc to show how to use non-public cloud: (Connect to all regions using Azure libraries for Python multicloud - Python on Azure | Microsoft Learn)[https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-sovereign-domain].
```
resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=resource_manager,
    credential_scopes=[resource_manager + "/.default"])
```

Yet as requiring users to provide duplicated information is not ideal, we have developed a new experience where users only need to supply the cloud information, and the library automatically handles the rest. This new behavior will be available once a new version of the library is released. Reference implementation: [azure-sdk-for-python AppConfiguration client](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/appconfiguration/azure-mgmt-appconfiguration/azure/mgmt/appconfiguration/_app_configuration_management_client.py#L73).
```
resource_client = ResourceManagementClient(
    credential, subscription_id,
    cloud_setting=resource_manager,
```

# Entitlement Required for SDK Generation Pipeline Access

## question 
Hi team,
 
I'm currently working on generating the Python SDK using the pipeline: (Using the SDK generation pipelines)[https://eng.ms/docs/products/azure-developer-experience/develop/sdk-generation-pipelines]. Although I have write access to the related GitHub repositories, I’m unable to access the pipeline itself.
Could you please let me know which entitlement is required for this access? Thank you!

## answer
https://aka.ms/azsdk/access
```
You'll need a GitHub account to contribute to Azure REST API and SDK repositories. Before you get started, be sure that you also:

Join the Microsoft organization on GitHub.
Join the Azure organization.
Check the visibility of your Microsoft and Azure org memberships.

If you're working on branches in the main repo for your spec, or working in the Azure SDK repositories to submit pull requests or serving as the support contact for issues, you'll need write access so that you can apply or dismiss labels, create or modify issues, and assign issues to others. It also allows you to add/update test recordings in the test assets repo.

To get access to Azure SDK repos, request to join the (Azure SDK Partners)[https://aka.ms/azsdk/join/azuresdkpartners] and have the request approved by your manager. After your manager approves, it may take up to one day for you to automatically be added to the (azure-sdk-partners)[https://github.com/orgs/Azure/teams/azure-sdk-partners] GitHub team. This will get you write access to all Azure SDK related repos. These membership requests will need to be renewed every 180 days.
```
