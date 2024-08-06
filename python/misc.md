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

globals()