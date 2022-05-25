# Virtual environment setup

Upgrade pip.

```bash
python3 -m pip install --upgrade pip
```

Create a base folder to store the virtual environments in.

```bash
mkdir ~/.venv
```

Create a new virtual environment.

```bash
python3 -m venv ~/.venv/venv
```

Activate the virtual environment.

```bash
source ~/.venv/venv/bin/activate
```

Install `ipykernel`.

```bash
python3 -m pip install ipykernel
```

Add the new kernel.

```bash
ipython kernel install --name=venv --user
```

## TL;DR

```bash
python3 -m pip install --upgrade pip
mkdir ~/.venv
python3 -m venv ~/.venv/venv
source ~/.venv/venv/bin/activate
python3 -m pip install ipykernel
ipython kernel install --name=venv --user
```
