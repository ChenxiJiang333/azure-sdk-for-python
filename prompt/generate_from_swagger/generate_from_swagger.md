**Context**

- PACKAGE: "Xxx"
- ENABLECHANGELOG: false,
- FULL PACKAGE: "azure-mgmt-{PACKAGE}"
- REST repo: "C:/dev/azure-rest-api-specs"
- SDK repo: "C:/dev/azure-sdk-for-python"
- VENV path: "C:/dev/azure-sdk-for-python/.venv"
- HeadSha: latest commit id of REST repo

**DO**

- Follow this guidance exactly

# Generate from swagger step by step

- step into REST repo then run
```bash
git checkout . && git clean -fd && git checkout origin/main && git pull origin main
```
- step into SDK repo
- if current branch name is not "{PACKAGE}-migration", run `git checkout origin/main && git pull origin main` then checkout a new branch named "{PACKAGE}-migration"
- Search "{FULL PACKAGE}" in all "readme.python.md" files of REST REPO. If there is one contains the target string "{FULL PACKAGE}", remember the PATH of the file. Parse PATH to get README with reference of format "{REST REPO}/{README}/readme.python.md"
- create "generate_input_swagger.json" at VENV path. Fill in key and value with following sample
```json
{
  "specFolder": "{REST REPO}",
  "headSha": "{HeadSha}",
  "runMode": "auto-release",
  "repoHttpsUrl": "https://github.com/Azure/azure-rest-api-specs",
  "enableChangelog": {ENABLECHANGELOG},
  "relatedReadmeMdFiles": [
    "{README}/readme.md"
  ]
}
```
- activate virtual environment of VENV path then run `sdk_generator .venv/generate_input_swagger.json .venv/generate_output.json` at root folder of SDK repo
- get "path" and "packageName" from generate_output.json
- step into folder {{path}}/{{packageName}} of SDK repo
- if .tox exist under this folder, clean .tox
- activate virtual environment of VENV path then run run command `tox run -c ../../../eng/tox/tox.ini --root . -e breaking -- --code-report`
- renamed "code_report.json" to "code_report_swagger.json"
- run `git status` for users to see status
- run
```bash
git add . && git commit -m "generate from swagger"
```


