# Subsetting/slicing lists

Getting the last two elements of a list in javascript can be done using the list's length property:

```javascript
var list = [1, 2, 3, 4, 5];
var lastTwo = list[list.length - 2];
```

This can be made simpler by using the slice method:

```javascript
var list = [1, 2, 3, 4, 5];
var lastTwo = list.slice(-2);
```

You can also specify the start and end index of the slice:

```javascript
var list = [1, 2, 3, 4, 5];
var lastTwo = list.slice(3, 5);
```
