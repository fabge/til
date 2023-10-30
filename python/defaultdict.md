# defaultdict

If you want to add a key to a dictionary, but you are not sure if the key exists, you can use defaultdict.

```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
```

Compare this to how you would have to write it with a normal dictionary:

```python
d = {}

if 'a' not in d:
    d['a'] = []

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
```
