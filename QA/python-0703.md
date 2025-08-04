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
Then, wrap the operation call like this:
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
This policy can be injected once into the client constructor using per_call_policies, making it a scalable and maintainable solution. No new feature is needed for this—it’s supported today.

# pipeline got stuck

## question 
Hello,
   I have a feature branch that won't be merged to main.   I just want to release it.   Before I do that, I want to make sure the pipeline is green.   But it is stuck currently.   Could someone help?
[Feature/azure ai agents/1.0.2 by howieleung · Pull Request #41623 · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/pull/41623)

## answer
If your pipeline is stuck and you're working from a feature branch that won't be merged to main, but you still want to release it, here's what you can do:

First, although your PR has conflicts, you mentioned that rebasing isn't appropriate because the main branch contains the latest beta code, while your feature branch is for a stable release. In this case, you can simply run your internal release build against the release branch. If it reaches the "approve release" phase, you're good to go.

You don’t have to approve a manually queued internal build, and this is consistent with how you've handled prior stable releases. Running the pipeline as a final check is understandable, even if not strictly required.

If you're trying to maintain the PR build pattern, here's a recommended approach:

Get your release branch to the desired state, excluding changelog and version updates.
Submit a PR targeting your release branch that includes the changelog and version updates.
The PR build will use the merge commit from both branches in the python - pullrequest pipeline, avoiding conflicts with main.
Once merged, your release branch will be in its final state, and you can queue the release build.
To clarify, the release build runs all the same tests plus a few more. If your goal is to validate the final public PR, this method works well with release branches.
