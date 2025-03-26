# Python miscellanea

## `__call__`

Defining `__call__` let's us use an object like a function (i.e. it's *callable*).

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

add5 = Adder(5)
print(add5(10)) # 15
```

## globals()

The `globals()` function returns a dictionary representing the current global symbol table. This includes all global variables and functions in the current module.

```python
x = 1
def foo():
    print("hello")

# Get dictionary of global symbols
global_dict = globals()
print(global_dict['x'])  # prints: 1
print(global_dict['foo'])  # prints: <function foo at ...>
```

You can also modify global variables using this dictionary, though this is generally not recommended:

```python
globals()['x'] = 100
print(x)  # prints: 100
```

## function parameters

```python
sums(a=1234, b=5678)
```

is the same as

```python
sums(**{'a': 1234, 'b': 5678})
```

## expression vs statement

Using `if` as an expression rather than a statement allows us to use it inside functions.
It is called a ternary operator.

```python
def f():
    return matches if matches else 0
```

## truthy and falsy values

In Python, `0`, `None`, `[]`, `{}`, `""`, `()` are all considered falsy.

A list with more than 0 elements, a string with more than 0 characters, a dictionary with more than 0 keys, a set with more than 0 elements, etc. are all considered truthy.  
Also an integer that is not 0 is considered truthy.
