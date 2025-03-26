# Useful regex patterns

## Lookahead and lookbehind

`(?!)` - negative lookahead  
`(?=)` - positive lookahead  
`(?<=)` - positive lookbehind  
`(?<!)` - negative lookbehind

## Capture groups

Using capture groups can make the process of finding substrings easier. Instead of using positive lookbehind, using a capture group makes following regular expression more readable:

Using positive lookbehind and positive lookahead:

```python
re.findall(r'(?<=<link rel="alternate" type="application\/json" href=")\S+(?=")', text)
```

Using capture groups:

```python
re.findall(r'<link rel="alternate" type="application/json" href="(\S+)"', text)
```

## `regex` library

The `regex` library is a superset of the `re` library. It has additional features and more thorough Unicode support.

What is specifically handy is the `.captures` method. It returns a list of all the captures in the order they appear in the regex pattern.

```python
from regex import search

rx = r'Item +(\d+): +(\d+ *)+'

data = "Item 1: 4 3 2 1"

m = search(rx, data)

m.captures(1) # ['1']

[int(i) for i in m.captures(2)] # [4, 3, 2, 1]

idx, ints = m.captures(1, 2)
idx # ['1']
[int(i) for i in ints] # [4, 3, 2, 1]
```
