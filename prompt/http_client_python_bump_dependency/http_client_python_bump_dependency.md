**Goal**
Create a new PR to bump dependencies or release new version

**Context**

- REPO: `C:/dev/typespec`
- CURRENT-DATE: {current Month-Day} (e.g. 07-24)

**Steps**

- step into folder `{REPO}/packages/http-client-python`
- run `git checkout . && git checkout origin/main && git pull origin main`
- run `git checkout -b publish/python-release-{CURRENT-DATE}`
- run `npx npm-check-updates -u --filter @typespec/*,@azure-tools/* --packageFile package.json `
- update `peerDependencies` of package.json. If its format is ">=0.a.b <1.0.0", only update 0.a.b but keep format ">=xxx <xxx" unchanged; If its format is "^1.a.b", just update to latest version.
- run `npm run change:version`
- run `npm install && npm run build && git add -u && git commit -m "bump version"`
- step into REPO
- run `git push origin HEAD`
- create new PR with title `[python] release new version`.
   **NOTE**: DO NOT add PR description.
