**Goal**
Create a new PR to bump dependencies

**Context**

- REPO: `C:/dev/typespec`
- CURRENT-DATE: {current Month-Day} (e.g. 07-24)

**Steps**

- step into folder `{REPO}/packages/http-client-python`
- run `git reset --hard && git checkout origin/main && git pull origin main`
- run `git checkout -b publish/bump-dep-{CURRENT-DATE}`
- run `npx npm-check-updates -u --filter @typespec/*,@azure-tools/* --packageFile package.json `
- update `peerDependencies` of package.json. If its format is ">=0.a.b <1.0.0", only update 0.a.b but keep format ">=xxx <xxx" unchanged; If its format is "^1.a.b", just update to latest version.
- run `npm install`
- run `npm run build`
- run `npm run change:add` and select `Bump dependencies" then input message "bump typespec"
- run `npm run format && git status`
- step into REPO
- run `git add -u && git commit -m "bump dependencies for python" && git push origin HEAD`
- create new PR with title `[python] bump typespec dependencies`.
   **NOTE**: DO NOT add PR description.