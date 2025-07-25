**Context**

- PACKAGE: "Xxx"
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
git reset --hard HEAD && git checkout origin/main && git pull origin main
```
- step into SDK repo
- if current branch name is not "{PACKAGE}-migration", run `git checkout origin/main && git pull origin main` then checkout a new branch named "{{PACKAGE}}-migration"
- Search "{FULL PACKAGE}" by fetch remote url `https://github.com/Azure/azure-rest-api-specs`. If there is file named "readme.python.md" that contains "{FULL PACKAGE}", remember the URL of the file. Parse URL to get README with reference of format "https://github.com/Azure/azure-rest-api-specs/{README}/readme.python.md"
- create "generate_input_swagger.json" at VENV path. Fill in key and value with following sample
```json
{
  "specFolder": "{REST REPO}",
  "headSha": "{HeadSha}",
  "repoHttpsUrl": "https://github.com/Azure/azure-rest-api-specs",
  "relatedReadmeMdFiles": [
    "{README}"
  ]
}
```
- activate virtual environment of VENV path then run `python -m packaging_tools.sdk_generator .venv/generate_input_swagger.json .venv/generate_output.json` at root folder of SDK repo
- get "path" and "packageName" from generate_output.json
- step into folder {{path}}/{{packageName}} of SDK repo
- if .tox exist under this folder, clean .tox
- activate virtual environment of VENV path then run run command `tox run -c ../../../eng/tox/tox.ini --root . -e breaking -- --code-report`
- renamed "code_report.json" to "code_report_swagger.json"
- run `git status` for users to see status
- run
```bash
git add -u && git commit -m "generate from swagger"
```


