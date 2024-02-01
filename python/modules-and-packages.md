# Modules and Packages

- The very basic: Every source file is a module. The import module will **load AND execute** a module.
- Modules are a namespace for the definitions inside, and as expected, a layer over a Python dictionary (the globals of that module).
Special variables: `__file__` (name of source file), `__name__` (name of the module) and `__doc__`. -> The main module: `__name__ == __main__`.
- `import foo` in `bar.py`:  Executes `foo` and adds a reference to `foo` in `bar.__dict__`
    - `from foo import func` : `foo` still executes, but only `func` is added to `bar`'s dictionary
    - `from foo import *`: All names that don't start with underscore get added to `bar`
- Each module is loaded only once. Use `sys.modules` to get a list of loaded modules.
- Module reloading (with `importlib`): This is not advised, since existing instances of classes will still use old code, specific names imported `from foo import name` don't get updated, and can break typechecks/ code with `super()`
- Module import basics: Relative imports of submodules don't work - imports are always absolute
    - Use "." prefix
- Packages: `__package__` (name of the enclosing package), `__path__` (search path for subcomponents)
- Main use of `__init__.py`: stitching together multiple source files into a "unified" top-level import
- Controlling exports: Submodules should define `__all__` to control `from module import *`. This is useful in `__init__`!
- `__main__.py` designates an entrypoint for a package! Makes the module executable `python -m module`
- Inject dynamic import magic with `__import__` or `importlib`. Can do things like `__import__(f"{__package__}.formats.{format}")` (this imports a file from `.formats` if present)
