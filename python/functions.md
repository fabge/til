# Functions

- Functions are also objects in python. You can pass them around, assign them to variables, and also inspect attributes. 
- Docstring: The first line of a function can be a string. Inspect via `func.__doc__`-
- Type hints/ annotations: Inspect via `func.__annotations__`. Of course, as we are all painfully aware, type annotations do absolutely nothing in Python.
- You can also just add random attributes to a function! Stored in `func.__dict__`.
- More helpful attributes: `func.__defaults__`, `func.__code__.co_argcount`, `func.__code__.co_varnames`
- `inspect` module in python: enables more structured inspection.
