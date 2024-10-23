# Bash snippets

```bash
zgrep -l  'assumed-role/EnBWAdminRole' cloudtrail_123412341234/* -R
```

```bash
zgrep  'EnBWAdminRole' cloudtrail_123412341234 -Rl | xargs -I{} bash -c "zless {}"
```

xargs für parallelisierung

```bash
zgrep  'EnBWAdminRole' cloudtrail_123412341234 -Rl | xargs -P2 -n2  -I{} bash -c  "zless {} | jq | grep EnBWAdminRole | grep arn:aws:sts" | sed -e 's/^[ \t]*//'  | grep -v , | sort | uniq -c
```
