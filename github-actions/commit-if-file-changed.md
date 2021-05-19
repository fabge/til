# Commit a file if it changed

This recipe commits potential changes made back to the parent repo but only if it has changed:

```yaml
on:
  push:
    branches:
    - master
# ...
    - name: Commit and push if changed
      run: |-
        git config user.name "Automated"
        git config user.email "actions@users.noreply.github.com"
        git add -A
        timestamp=$(date -u)
        git commit -m "Latest data: ${timestamp}" || exit 0
        git push
```