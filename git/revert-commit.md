# Revert commit

If you want to revert a commit, meaning only the changes of this commit - not until this commit - you can use the following:

```bash
# git checkout -b revert-this
git revert <commit hash>
# git push
```

This also works for Pull Requests.
