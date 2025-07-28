# GOAL
Create a new PR based on an existing PR then close existing PR

# CONTEXT
- Existing PR: YOUR_PR_URL_LINK

# STEP
1. Fetch Existing PR to get REPO name, BRANCH name, PR TITLE and PR description.
2. Step into local repo `C:/dev/{REPO}`
3. run
```bash
git reset --hard HEAD
git clean -fd
```
5. Create a NEW NAME with PR TITLE and PR description then checkout a NEW BRANCH with NEW NAME based on BERACH
6. Parse PR description and anaylze which ISSUE the Existing PR try to fix
7. Generate NEW PR description with `Moved from {Existing PR}\nFix {ISSUE}`.

   **NOTE**: DO NOT ADD detailed PR decription into NEW PR description
9. Create NEW PR in same REPO with NEW BRANCH, PR TITLE and NEW PR description. 
10. Add comment "Moved to {NEW PR URL LINK}" in Existing PR then close it.
