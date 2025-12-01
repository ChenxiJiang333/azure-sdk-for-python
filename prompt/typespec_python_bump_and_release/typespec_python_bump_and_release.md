**Goal**

Help user bump dependency "@typespec/http-client-python" for `Azure/autorest.python` repo

**Context**

- BASE_BRANCH: "main"
- CURRENT_DATE: current date (e.g. "2025-01-01")

# Step
1. Step into root folder of "Azure/autorest.python" repo
2. If BASE_BRANCH is "main", run `git checkout . && git checkout origin/main && git pull origin main && git checkout -b publish/release-{{CURRENT_DATE}}`; if BASE_BRANCH is not "main", run `git checkout . && git fetch origin {{BASE_BRANCH}} && git checkout {{BASE_BRANCH}}`
3. Get latest VERSION of "@typespec/http-client-python" then update version of "@typespec/http-client-python" to "~{{VERSION}}" for file 
"packages/autorest.python/package.json" and "packages/typespec-python/package.json"
4. run `pnpm change version`, then there shall at least be 4 files changed:
- "packages/autorest.python/package.json"
- "packages/autorest.python/CHANGELOG.md"
- "packages/typespec-python/package.json"
- "packages/typespec-python/CHANGELOG.md"
5. version tool already calcuated next version in last step but it may update version with wrong: use `git diff` to get udpated content of "CHANGELOG.md", if there is "### Features", we shall upgrade to minor version instead of patch version, so update version of up 4 files to minor version
6. run `pnpm install && pnpm build && git add -u`
7. commit with message "bump version" and push
8. If there is no existing PR for current branch, create one.
