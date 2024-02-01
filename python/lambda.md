# Using `lambda`

Lambdas can be used to alter function args similar to `functools.partial`.

```python
import functools

def multiply(x, y):
    return x * y

multiply_lambda = lambda x: multiply(x, 5)
multiply_partial = functools.partial(multiply, y=5)

print(multiply_lambda(3))
# 15
print(multiply_partial(3))
# 15
```
