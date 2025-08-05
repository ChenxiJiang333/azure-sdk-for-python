# Release pipeline failing

## question 
Hi Language - Python,
Wondering why this pipeline is failing: https://dev.azure.com/azure-sdk/internal/_build/results?buildId=4959365&view=logs&j=447d33cb-e696-5bdf-6dab-daffaacae469
The pr checks were successfull…
```
_ ERROR collecting sdk/healthinsights/azure-healthinsights-cancerprofiling/tests/test_cancer_profiling.py _
ImportError while importing test module '/mnt/vss/_work/1/s/sdk/healthinsights/azure-healthinsights-cancerprofiling/tests/test_cancer_profiling.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
.tox/mindependency/lib/python3.13/site-packages/azure/core/rest/__init__.py:27: in <module>
    from ._rest_py3 import (
.tox/mindependency/lib/python3.13/site-packages/azure/core/rest/_rest_py3.py:40: in <module>
    from ._helpers import (
.tox/mindependency/lib/python3.13/site-packages/azure/core/rest/_helpers.py:28: in <module>
    import cgi
E   ModuleNotFoundError: No module named 'cgi'
```

## answer
Your PR checks passed because you only changed `azure-healthinsights-radiologyinsights`, and the `pull request` build is scoped to only that package. However, `internal` builds are service-wide, so they include all packages in the `healthinsights` folder, even those do not have a release stage. That's why the failure is only on the `internal` build.

To unblock you, please run a build that artificially limits the build scope to only `azure-healthinsights-radiologyinsights` by adding variable `BuildTargetingString` with value `azure-healthinsights-radiologyinsights`.

# Testing SDK PRs

## question 
General Hi team , I am working on prs for ODBA and I want to know what are the testing scopes required for the PRs. 
https://github.com/Azure/azure-sdk-for-python/pull/41428

## answer
Hi, we already commit some basic tests for the PR and we pass those test locally. For mgmt SDK, it shall be enough. Of course, it would be nice if you are willing to commit more tests by yourselves. You can refer the guidance [azure-sdk-for-python/doc/dev/tests.md at main · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/tests.md) and our last commit for test [[AutoRelease\] t2-oracledatabase-2025-06-05-34855(can only be merged by SDK owner) by azure-sdk · Pull Request #41428 · Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python/pull/41428/commits/fbcfd9783d2933d5c3258cdb3a30d032b20170cd).
