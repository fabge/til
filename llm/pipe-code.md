# Pipe code and let explain

```bash
rg -I -A 5 get_automation_account_credentials | llm -s 'explain what get_automation_account_credentials does'
```

[ripgrep](https://github.com/BurntSushi/ripgrep) finds the first 5 occurences including surrounding code of `calculate_findings`.  
Piping it to `llm` explains what `calculate_findings` does.
