# What's the cleanest way to have a bash script run something in a specific working directory?

There is always the possibility of `cd`ing into a directory and returning afterwards:

```bash
cd some-dir && ./my-script && cd -
```

However you can run commands like the this in a subshell, using parenthesis:

```bash
(cd some-dir && ./my-script)
```