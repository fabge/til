# Revert commit

If you want to revert a commit, meaning only the changes of this commit - not until this commit - you can use the following:

```bash
# git checkout -b revert-this
git revert <commit hash>
# git push
```

If you want to revert multiple commits, you can use the following:

```bash
# git checkout -b revert-this
git revert --no-commit <first commit hash>
git revert --no-commit <second commit hash>
git revert --no-commit <third commit hash>
git commit -m "revert"
# git push
```
