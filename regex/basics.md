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
