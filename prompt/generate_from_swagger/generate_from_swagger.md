**Context**

REST repo: "C:/dev/azure-rest-api-specs"
SDK repo: "C:/dev/azure-sdk-for-python"
VENV path: "C:/dev/azure-sdk-for-python/.venv"
HeadSha: latest commit id of REST repo
SERVICE: "devtestlabs"
README: "specification/devtestlabs/resource-manager/readme.md"

**DO**
- Follow this guidance exactly

# Generate from swagger step by step
- step into REST repo then clean repo with `git reset --hard HEAD`
- checkout origin/main and pull latest main branch
- step into sdk repo then clean repo with `git reset --hard HEAD`
- if current branch name doesn't end with "-migration", checkout origin/main and pull latest main branch then checkout a new branch named "{{SERVICE}}-migration"
- create "generate_input_swagger.json" at VENV path. Fill in key and value with following sample
```json
{
  "specFolder": "{{REST REPO}}",
  "headSha": "{{HeadSha}}",
  "repoHttpsUrl": "https://github.com/Azure/azure-rest-api-specs",
  "relatedReadmeMdFiles": [
    "{{README}}"
  ]
}
```
- activate virtual environment of VENV path then run "python -m packaging_tools.sdk_generator .venv/generate_input_swagger.json .venv/generate_output.json" at root folder of SDK repo
- get "path" and "packageName" from generate_output.json
- step into folder {{path}}/{{packageName}} of SDK repo
- if .tox exist under this folder, clean .tox
- activate virtual environment of VENV path then run run command "tox run -c ../../../eng/tox/tox.ini --root . -e breaking -- --code-report"
- renamed "code_report.json" to "code_report_swagger.json"
- commit all changes with "generate from swagger"


