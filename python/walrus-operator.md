# Walrus Operator

The := operator is officially known as the **assignment expression operator**.  
It allows me to assign a value to a variable in another statement.  
This makes if statements more succinct and prevent repetition:

```python
d = {}
x = d.get('a')
if x:
    x += 1
```

The above code can be written in a more concise way using the := operator:

```python
d = {}
if (x := d.get('a')):
    x += 1
```

This looks like small change, but the code becomes more readable, especially if the `get` operation is more verbose.
