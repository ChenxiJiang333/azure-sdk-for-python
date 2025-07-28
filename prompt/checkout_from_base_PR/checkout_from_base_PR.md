# GOAL
checkout a new PR on an existing PR then close existing PR

# CONTEXT
- Existing PR: YOUR_PR_URL_LINK

# STEP
1. Fetch Existing PR to get REPO name, BRANCH name, PR TITLE and PR description.
2. Step into local repo `C:/dev/{REPO}`
3. run `git reset --hard HEAD`
4. Create a NEW NAME with PR TITLE and PR description then checkout a NEW BRANCH with NEW NAME based on BERACH
5. Generate NEW PR description with "moved from {Existing PR}\n{PR description}.
6. Create NEW PR in same REPO with NEW BRANCH, PR TITLE and NEW PR description. 
7. Update Existing PR description by adding `moved to {NEW PR URL LINK}\n` at head of PR description then close it.
