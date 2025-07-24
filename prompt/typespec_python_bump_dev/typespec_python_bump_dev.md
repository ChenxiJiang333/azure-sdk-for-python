**Goal**

Help user release dev version for `@typespec/http-client-python` then bump it in `Azure/autorest.python` repo

**Context**

- HTTP-CLIENT-PYTHON-PR: https://github.com/microsoft/typespec/pull/7992
- TYPESPEC-PYTHON-PR: https://github.com/Azure/autorest.python/pull/3135
- SDK-REPO: C:/dev/azure-sdk-for-python
- TYPESPEC-PYTHON-REPO: C:/dev/autorest.python
- HTTP-CLIENT-PYTHON-REPO: C:/dev/typespec
- CHANGELOG of PR is usually in `.md` file under `.chronus` folder

# Step

## Stage 1: release dev version for `@typespec/http-client-python`
1. Get latest stable version and latest dev version for `@typespec/http-client-python`. According to stable version and dev version, calculate NEXT DEV VERSION number.
2. Get SOURCE BRANCH NAME of HTTP-CLIENT-PYTHON-PR
3. Step into HTTP-CLIENT-PYTHON-REPO, run `git reset --hard HEAD && git checkout origin/main && git pull origin main`. Then checkout NEW BRANCH with name "{SOURCE BRANCH NAME}-{NEXT DEV VERSION}" if not created yet.
4. Update "version" of file "packages/http-client-python/package.json" with NEXT DEV VERSION. Then run `git add -u && git commit -m "update version" && git push origin HEAD`
5. Step into SDK-REPO, activate virtual environment `.venv` then run `az login`
6. trigger release pipeline with command `az pipelines run --id 7189 --branch {NEW BRANCH}`. Get the "id" from command result and hint user to check pipeline status with complete PIPELINE URL `https://dev.azure.com/azure-sdk/internal/_build/results?buildId={id}&view=results`. 
7. Run `pwsh C:/users/yuchaoyan/timer.ps1 15 {PIPELINE URL}` which may take 15 minutes.
8. Get latest dev version of `@typespec/http-client-python` to confirm NEXT DEV VERSION is released

## Stage 2: update for TYPESPEC-PYTHON-PR

9. Get CHANGELOG by info fetched from `{HTTP-CLIENT-PYTHON-PR}/files`
10. Step into TYPESPEC-PYTHON-REPO and checkout branch of TYPESPEC-PYTHON-PR
11. Split CHANGELOG and show each part of CHANGELOG with wrap of "``" so that user could copy the content conveniently then 
12. Run "pnpm change add"
13. update version of "@typespec/http-client-python" in "packages/autorest.python/package.json" and "packages/typespec-python/package.json" with `~{NEXT DEV VERSION}`
14. run `pnpm install && pnpm build && git add -u && git add .chronus && git commit -m "bump http-client-python version" && git push origin HEAD`
15. run `pwsh C:/users/yuchaoyan/timer.ps1 60 {TYPESPEC-PYTHON-PR}`

