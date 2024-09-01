# Django tests

Common practice is to delete `tests.py` and create individual test modules for each file of the app.  
E.g. an app named `myapp` will may have a `test_views.py`, `test_admin.py`, etc.

- Delete `tests.py`
- Create a directory in its place called `tests/`
- Inside of tests, create `__init__.py` and `test_models.py`.
