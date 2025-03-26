# Bash snippets

```bash
zgrep -l  'assumed-role/AdminRole' cloudtrail_123412341234/* -R
```

This command searches for files containing the text 'assumed-role/AdminRole' in the cloudtrail_123412341234 directory and its subdirectories:

- `zgrep`: Like grep but for compressed files (e.g., .gz files)
- `-l`: Only lists the filenames (not the matching lines)
- `-R`: Searches recursively through directories

```bash
zgrep  'AdminRole' cloudtrail_123412341234 -Rl | xargs -I{} bash -c "zless {}"
```

This command finds files containing 'AdminRole' and displays their contents:

- First part finds matching files (similar to previous command)
- `xargs`: Takes the output from zgrep and passes it as arguments to the next command
- `-I{}`: Defines a placeholder (`{}`) for the input
- `bash -c "zless {}"`: For each file found, runs zless to view its contents
- `zless`: Like 'less' command but for compressed files

xargs für parallelisierung

```bash
zgrep  'AdminRole' cloudtrail_123412341234 -Rl | xargs -P2 -n2  -I{} bash -c  "zless {} | jq | grep AdminRole | grep arn:aws:sts" | sed -e 's/^[ \t]*//'  | grep -v , | sort | uniq -c
```

This is a more complex command that processes CloudTrail logs to find unique AWS STS role assumptions:

- `-P2`: Runs 2 parallel processes
- `-n2`: Processes 2 arguments at a time
- `jq`: Formats JSON output
- Multiple `grep` commands filter for specific patterns
- `sed -e 's/^[ \t]*//'`: Removes leading whitespace
- `grep -v ,`: Excludes lines containing commas
- `sort | uniq -c`: Sorts the output and counts unique occurrences
