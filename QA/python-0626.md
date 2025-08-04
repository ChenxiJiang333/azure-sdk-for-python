# Generate code cause too-many-locals and Unused import urllib.parse

## question 
Hello Language - Python Got issue with code gen...   When I run lint using next-pylint
```
tox run -e next-pylint -c ../../../eng/tox/tox.ini --root .
```
I am getting
azure/ai/agents/aio/operations/_operations.py:1357: [R0914(too-many-locals), RunsOperations.create] Too many local variables (34/25)
azure/ai/agents/aio/operations/_operations.py:4090: [R0914(too-many-locals), AgentsClientOperationsMixin.create_agent] Too many local variables (26/25)
azure/ai/agents/aio/operations/_operations.py:4475: [R0914(too-many-locals), AgentsClientOperationsMixin.update_agent] Too many local variables (27/25)
azure/ai/agents/aio/operations/_operations.py:4815: [R0914(too-many-locals), AgentsClientOperationsMixin.create_thread_and_run] Too many local variables (32/25)
azure/ai/agents/aio/operations/_operations.py:26: [W0611(unused-import), ] Unused import urllib.parse
 
The _operations.py is straightly created by code gen.  Need advise how to fix them..

## answer
The issues you're seeing when running `next-pylint` are due to `_operations.py` being a generated file, and `next-pylint` referencing a different `pylintrc` file.

We already have some exclusion of emitted files in the root `pylintrc`, like:

```
(?:.*[/\\]|^)agents/(models/_models.py|_model_base.py|operations/_operations.py|aio/operations/_operations.py)$
```

So I would not expect the errors you show to be in the CI pipeline, only when you run locally.

The problem is that `next-pylint` uses `eng/pylintrc`, and this file doesn’t include the same ignore-paths for agents. That’s an oversight on my part.

We have a separate `pylintrc` file for `next-*` as we have to ignore the next- pylint checks added every 3 months to not break everyday CI while still allowing users to fix the next-* warnings.

We will update the `eng/pylintrc` to align with the ignore-paths added to the root `pylintrc`. You can refer to this PR for the fix:

https://github.com/Azure/azure-sdk-for-python/pull/41607/files

This should address the `too-many-locals` and `unused import urllib.parse` warnings you’re seeing.

# Release pipeline failing

## question 
Hi Language - Python,
Wondering why this pipeline is failing: https://dev.azure.com/azure-sdk/internal/_build/results?buildId=4959365&view=logs&j=447d33cb-e696-5bdf-6dab-daffaacae469
The pr checks were successfull…

## answer
Your nightly/internal pipeline is failing due to a Python 3.13 error that’s been happening for the past couple months. The root cause is that `azure-healthinsights-cancerprofiling` specifies too old of a minimum version of `azure-core` for Python 3.13, where `cgi` was removed.

Your PR checks passed because you only changed `azure-healthinsights-radiologyinsights`, and the pull request build is scoped to only that package. However, internal builds are service-wide, so they include all packages in the `healthinsights` folder, even those not being released. That's why the failure surfaced internally.

To unblock you, I ran a build that artificially limits the build scope to only `azure-healthinsights-radiologyinsights`, which should allow you to release successfully.

If `azure-healthinsights-cancerprofiling` is deprecated and not going to be released again, we should follow the deprecation process as outlined here:
https://github.com/Azure/azure-sdk-for-python/blob/main/doc/deprecation_process.md

If we might need to release it again someday, we should fix the dependencies to keep it from falling into bitrot.

# Testing SDK PRs

## question 
General Hi team , I am working on prs for ODBA and I want to know what are the testing scopes required for the PRs. 
https://github.com/Azure/azure-sdk-for-python/pull/41428

## answer
Hi, we already commit some basic tests for the PR and we pass those test locally. For mgmt SDK, it shall be enough. Of course, it would be nice if you are willing to commit more tests by yourselves. You can refer the guidance [azure-sdk-for-python/doc/dev/tests.md at main · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/tests.md) and our last commit for test [[AutoRelease\] t2-oracledatabase-2025-06-05-34855(can only be merged by SDK owner) by azure-sdk · Pull Request #41428 · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/pull/41428/commits/fbcfd9783d2933d5c3258cdb3a30d032b20170cd).

# Code generator on python validates versions by comparing literals.

## question 
Hello, Language - Python!
We have an SDK code with three different versions:
2025-05-01
v1
v2025_05_15_preview ([link](https://github.com/Azure/azure-rest-api-specs/blob/87bd051c295d94fffa28a4fa6b18f8b4b71c50ec/specification/ai/Azure.AI.Agents/main.tsp#L47))
We have added the method in version v1 and the swagger has generated correctly: this method was present in both v1 and 2025_05_15_preview ([Add thread message delete operation by nick863 · Pull Request #35320 · Azure/azure-rest-api-specs](https://github.com/Azure/azure-rest-api-specs/pull/35320/files)). When I have generated the Python code, the validation code directly [compares literals](https://github.com/Azure/azure-sdk-for-python/blob/68f3822229eba94c3fb49a29b57b8f37c85845cf/sdk/ai/azure-ai-agents/azure/ai/agents/_validation.py#L24), which leads to the fact that 2025_05_15_preview seems to be not supported anymore as "v1" is technically greater then "2025_05_15_preview". Is there a possibility to compare enum values as opposed to literals?

## answer
The issue you're encountering is because the validation code directly compares literals, so 2025_05_15_preview seems to be not supported anymore as v1 is technically greater than 2025_05_15_preview.

But this validation code was not designed to work when API version scheme is not consistent from a version to another, and TypeSpec semantic for version ordering is not lexical, it's the order in the file. So codegen needs to follow TypeSpec semantic since this is our source of truth.

We confirmed this is wrong and decided to fix it. As a solution:

I have PRs out both for disabling the versioning validation, and for validating API versioning by checking the spec ordering.

The emitter has been released, I'm just currently in the process of updating the emitter-package.json in the azure-sdk-for-python repo.

Once this PR passes:
https://github.com/Azure/azure-sdk-for-python/pull/41724

You can pull from main and try regenerating. Let me know if you see any diffs in regeneration and if these diffs work out for you.
 