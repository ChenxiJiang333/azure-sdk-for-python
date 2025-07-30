**GOAL**

bump typespec-python for emitter-package.json

**Context**
- SDK repo: C:/dev/azure-sdk-for-python
- Typespec Python Version: latest version of `@azure-tools/typespec-python`
- PR Title: "bump typespec-python {Typespec Python Version}"

**STEPS**:
- step into SDK repo then run:
```bash
git reset --hard HEAD
git checkout origin/main
git pull origin main
```
- checkout New Branch named `bump-typespec-python-{Typespec Python Version}`
- run `npx npm-check-updates --packageFile eng/emitter-package.json`
- run `tsp-client generate-lock-file`
- commit changes about `emitter-package.json` and `emitter-package-lock.json`
- create PR with New Branch, PR Title
