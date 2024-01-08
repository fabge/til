# Do some action when changing directory (cd)

The following script activates a virtualenv when changing directory to a directory containing a folder named `.venv`:

```bash
function cd {
    builtin cd "$@"
    if [ -d .venv ]; then
        source .venv/bin/activate
    fi
}
```

This might be useful if you want to activate virtual envs automatically when changing directory to the project directory.
