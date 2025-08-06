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