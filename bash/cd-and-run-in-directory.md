# Run bash script in specific directory

From [Simon Willison](https://twitter.com/simonw/status/1380596108502528002). There is always the possibility of `cd`ing into a directory and returning afterwards:

```bash
cd some-dir && ./my-script && cd -
```

However you can run commands like the this in a subshell, using parenthesis:

```bash
(cd some-dir && ./my-script)
```
