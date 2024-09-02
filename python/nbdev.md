# nbdev

[nbdev](https://nbdev.fast.ai/) is a tool for exploratory programming and makes it possible to develop complex libraries using only Jupyter notebooks.

## nb_export

I tend to write smaller scripts in my day to day work, so instead of setting up a comlete nbdev project I found following snippet more useful in this regard:

```python
#| default_exp core

#|export
def foo(): pass

from nbdev.export import nb_export
nb_export('test.ipynb', '.')
```

Pasting and running those lines at the end of a notebook exports it as pure `core.py` file - removing the need to copy and paste between those files.

## nbdev for subparts of a project

1. Create a `settings.ini` file (just one for the whole project/repo)

2. In your notebook file, add "`#|default_exp module_name`" in the very top cell of the notebook.

3. For every code cell that you want include in `module_name.py`, you should have "`#| export`" at the top.

Then you can run `nbdev_export --path module_name.ipynb` and it works! (i.e. `module_name.py` appears in the `lib_name/` specified in `settings.ini`.)
