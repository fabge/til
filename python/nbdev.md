# nbdev

[nbdev](https://nbdev.fast.ai/) is a tool for exploratory programming and makes it possible to develop complex libraries using only Jupyter notebooks.

I tend to write smaller scripts in my day to day work, so instead of setting up a comlete nbdev project I found following snippet more useful in this regard:

```python
from nbdev.export import nb_export
nb_export('test.ipynb', '.')
```

Pasting and running those lines at the end of a notebook exports it as a pure .py file - removing the need to copy and paste between those files.
