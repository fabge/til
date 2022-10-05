# Bash snippets

zgrep -l  'assumed-role/EnBWAdminRole' cloudtrail_687503256810/* -R

zgrep  'EnBWAdminRole' cloudtrail_265043837094 -Rl | xargs -I{} bash -c "zless {}"

xargs für parallelisierung

zgrep  'EnBWAdminRole' cloudtrail_265043837094 -Rl | xargs -P2 -n2  -I{} bash -c  "zless {} | jq | grep EnBWAdminRole | grep arn:aws:sts" | sed -e 's/^[ \t]*//'  | grep -v , | sort | uniq -c
