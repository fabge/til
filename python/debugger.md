# Python debugger

It's possible to automatically drop into the Python debugger when an exception is raised.

```python
# test.py
def f(x): return 1/x
print(f(0))
```

```bash
python -m pdb -c c test.py

# Traceback (most recent call last) :
# ...
# ZeroDivisionError: division by zero Uncaught exception. Entering post mortem debugging
# Running 'cont' or 'step' will restart the program
# > /home/jhoward/test.py (1)f() → def f(x): return 1/x
# (Pdb) args
# x = 0
# (Pdb) q
```

The `-c c` option continues the program immediately, so you don't have to type `c` to continue.

(from: https://twitter.com/jeremyphoward/status/1756541454288396402)
