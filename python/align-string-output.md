# Align string output with f-strings

It can be useful to align the output of strings. Here is an example how to immitate a table of contents:

```python
contents = {"Introduction": 1, "Python Basics": 5, "Creating Your First Program": 12, "Operators and Variables": 29}
for chapt, page in contents.items():
    print(f"{chapt:.<30}{page:.>5}")
```

The `.` sets the filler character and can be ommitted, `<` or `>` or `^` defines the alignment (left, right, middle) and the number defines the column width.

Output:

```text
Introduction......................1
Python Basics.....................5
Creating Your First Program......12
Operators and Variables..........29
```
