# Code generator for error handling

## question 
Hi Language - Python!

Azure Batch has an error handling model that is similar to the ODataV4Format class but is slightly different. Right now, we will have to do our own exception building for our Track 2 Python SDK and would have to manually retrieve our service error messages to surface to the customer. This would also mean that we'd have to manually maintain the error handling on our end and add it in as a patch for every operation. Is there a way that we could utilize the code generator to assist with maintaining the exception handling in this case? 
```
// BatchError model
{
    "code": "ExampleCode",
    "message": {
        "lang": "en-us",
        "value": "This is an example error message"
    },
    "values": {
        "key": "ExampleInnerErrorCode",
        "value": "This is a more detailed message on the inner error"
    }
}

// ODataV4Format
{
    "code": "ExampleCode",
    "message": "This is an example error message",
    "details": [
        {
            "code": "ExampleInnerErrorCode",
            "message": "This is a more detailed message on the inner error"
        }
    ]
}
```

## answer
The recommended approach is to create a custom error format class like:
```
class BatchErrorFormat(ODataV4Format):
    # Custom parsing logic here
```
Then, wrap the operation calls like this:
```
try:
   generated_client.op()
except HttpResponseError as err:
   # Build what you need
   raise HttpResponseError(ressponse=err.response, model=err.modell, error_format=BatchErrorFormat)
```
This pattern is similar to what's used in https://github.com/Azure/azure-sdk-for-python/blob/5b574616e2a237ef3eeccf86390da7f52279746c/sdk/core/azure-mgmt-core/azure/mgmt/core/exceptions.py#L58C1-L58C37 and https://github.com/Azure/azure-sdk-for-python/blob/5b574616e2a237ef3eeccf86390da7f52279746c/sdk/oep/azure-mgmt-oep/azure/mgmt/oep/aio/operations/_operations.py#L101.

To avoid patching every operation, a cleaner solution is to implement a custom pipeline policy:
```
class BatchExceptionPolicy:
    def send(request):
        try:
            return self.next.send(request)
        except HttpResponseError as err:
            raise HttpResponseError(response=err.response, model=err.model, error_format=BatchErrorFormat) from err
```
Then inject the policy into the client constructor using `per_call_policies`: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#pipeline

# pipeline got stuck

## question 
Hello,
I have a feature branch that won't be merged to main.  I just want to release it.  Before I do that, I want to make sure the pipeline is green. But it is stuck currently. Could someone help?
[Feature/azure ai agents/1.0.2 by howieleung · Pull Request #41623 · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/pull/41623)

## answer
You can simply run your internal release build against the release branch. If it reaches the "approve release" phase, you're good to go, it's actually more certain than if you got a PR build to run.

Yet if you want to maintain the PR build pattern. I do have a recommendation how you can make that work with release branches.
 
1. Get your release branch where you want it to be minus `changelog` and `version` updates.
2. Submit a PR targeting your release branch with the `changelog` and `version` updates. the PR build will use the merge commit from both your branches in the `python - pullrequest` pipeline, instead of hitting conflicts with `main`.
3. Merge that. Your release branch will be in final state, which you can queue the release build for.
 
To be clear, your release build will run all the same tests + a couple more, but if it's really about the last public PR then that's how you would do it with a release branch
