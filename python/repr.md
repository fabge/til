# Using `repr`

Objects have two string representations:

- str(obj) - printable output
- repr(obj) - for programmers
- The convention for `__repr__` is to return a string that, when fed to `eval()`, will recreate the underlying object.
- print(obj) uses `__str__`

(from https://github.com/SumanthRH/python-mastery/blob/main/learnings.md).

Example for `__repr__`:

```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Car name: {self.name}, color: {self.color}"

    def __repr__(self):
        return f"Car(name='{self.name}', color='{self.color}')"

car = Car("Tesla", "red")
print(car)
# Car name: Tesla, color: red
print(repr(car))
# Car(name='Tesla', color='red')

same_car = eval(repr(car))
print(same_car.name)
# Tesla
print(same_car.color)
# red
```
