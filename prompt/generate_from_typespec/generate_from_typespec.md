**Context**

- REST repo: "C:/dev/azure-rest-api-specs"
- SDK repo: "C:/dev/azure-sdk-for-python"
- VENV path: "C:/dev/azure-sdk-for-python/.venv"
- ENABLECHANGELOG: true,
- PULL REQUEST: "https://github.com/Azure/azure-rest-api-specs/pull/35579"
- HeadSha: latest complete commit id of PULL REQUEST
- TSP PATH: path where tsp file. You can get it from PULL REQUEST (e.g. "specification/servicelinker/ServiceLinker.Management")

# Generate from swagger step by step
- step into REST repo then run
```bash
git reset --hard HEAD
git clean -fd
```
- checkout the source branch of PULL REQUEST
- step into sdk repo then run
```bash
git reset --hard HEAD
git clean -fd
```
- if current branch name is not "{{SERVICE}}-migration", run `git checkout origin/main && git pull origin main` then checkout a new branch named "{{SERVICE}}-migration"
- create `generate_input_typespec.json` at VENV path. Fill in key and value with following sample
```json
{
  "specFolder": "{REST REPO}",
  "headSha": "{HeadSha}",
  "runMode": "auto-release",
  "repoHttpsUrl": "https://github.com/Azure/azure-rest-api-specs",
  "enableChangelog": {ENABLECHANGELOG},
  "relatedTypeSpecProjectFolder": [
    "{TSP PATH}"
  ]
}
```
- activate virtual environment of VENV path then run "python -m packaging_tools.sdk_generator .venv/generate_input_typespec.json .venv/generate_output.json" at root folder of SDK repo
- get "path" and "packageName" from generate_output.json
- step into folder {{path}}/{{packageName}} of SDK repo
- IF folder .tox exist under this folder, delete .tox
- activate virtual environment of VENV path then run run command "tox run -c ../../../eng/tox/tox.ini --root . -e breaking -- --code-report"
- rename "code_report.json" to "code_report_typespec.json"
- run `git status` for users to see status
- run
```bash
git add . && git commit -m "generate from typespec"
```
- activate virtual environment of VENV path then run run command "tox run -c ../../../eng/tox/tox.ini --root . -e breaking -- --source-report code_report_swagger.json --target-report code_report_typespec.json" then extract changelog from output which has format `(Xxx): ...`. Abondon `(Xxx): ` for each item of changelog then fill `CHANGELOG.md` with proper format.
- run
```bash
git add . && git commit -m "changelog" && git push msyyc HEAD
```
