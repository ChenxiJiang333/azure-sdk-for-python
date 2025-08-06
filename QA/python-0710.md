# How to make code gen to generate `AgentsOperations` instead of `AgentsClientOperationsMixin`

## question 
Hello Language - Python

I have code gen generated
```
class AgentsClientOperationsMixin(
    ClientMixinABC[AsyncPipelineClient[HttpRequest, AsyncHttpResponse], AgentsClientConfiguration]
):
```
Is it possible to generate `AgentsOperations`
This class is public.  So I want a better name.

## answer
The AgentsClientOperationsMixin class should not be documented or publicly exposed. Although it is currently accessible via from azure.ai.agents.operations import AgentsClientOperationsMixin, this visibility causes it to appear in public documentation like Microsoft Learn, which is not intended.

After discussion, the Python SDK team concluded that the correct solution is to make the mixin operation group a private class. This change ensures the class is hidden from public documentation while maintaining compatibility with the generated code.

The issue has been tracked in https://github.com/microsoft/typespec/issues/7803, and the fix has been implemented in https://github.com/microsoft/typespec/pull/7817.

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
