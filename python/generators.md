# Generators

- Calling a generator function creates a generator object.
- Function only executes on `next()`.
- Generators are one time use.
- A generator function cannot execute by itself (need a loop)
- The `yield` statement represents the point of preemption. This is where executed last stopped

```python
def my_generator():
    print("Starting up")
    yield 1
    print("Resuming")
    yield 2
    print("Ending")

gen = my_generator()
next(gen)
# Starting up
# 1
next(gen)
# Resuming
# 2
next(gen)
# Ending
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```
