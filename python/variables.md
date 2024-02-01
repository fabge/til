# Scope of variables

- All statements have 2 scopes/ access to two scopes: The global scope of the module in which it is in, and the local scope, the scope private to the function it is in.
- Global variables can be accessed within a function, but it cannot be modified without an explicit global keyword. This is important: **Globals are already readable**! Only before you modify them, you need to specify this keyword.
- `globals()`/`locals()`: Gives you a dictionary with the contents of the global/local scope respectively.
