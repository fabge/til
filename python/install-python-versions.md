# Install different Python versions

[Pyenv](https://github.com/pyenv/pyenv) allows me to have different Python versions on my machine in parallel.

```bash
pyenv install 3.10.0
```

This gives me a Python 3.10 installation on my Mac in `~/.pyenv/versions/3.10.0/bin/python`.

Then, I can create a new virtual environment using the above path.

```bash
~/.pyenv/versions/3.10.0/bin/python -m venv /tmp/py310
```

And activate that virtual environment:

```bash
source /tmp/py310/bin/activate
```