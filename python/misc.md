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

#TODO globals()

## function parameters

```python
sums(a=1234, b=5678)
```

is the same as

```python
sums(**{'a': 1234, 'b': 5678})
```
