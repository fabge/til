# Squash/rebase commits

To squash the last 4 commits into one:

```bash
git rebase -i HEAD~4
```

Change the bottom 3 commits from `pick` to `f` or `fixup` and save the file.  
Keep or change the top commit message to whatever you want.  
Then force push to the remote branch:  

```bash
git push -f
```
