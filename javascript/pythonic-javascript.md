# Pythonic Javascript

Content from:
* [Javascript for Python programmers](https://mike.depalatis.net/blog/javascript-for-python-programmers.html)
* [Javascript Object Literal](https://www.dyn-web.com/tutorials/object-literal/)
* [JavaScript Module Pattern: In-Depth](http://www.adequatelygood.com/JavaScript-Module-Pattern-In-Depth.html)
* [Python vs Javascript](https://realpython.com/python-vs-javascript/)

## Exception handling

```python
# python
try:
    thing()
except Exception:
    print("oh no!")

raise ValueError("not a good value")
```

```javascript
// javascript
try {
  thing();
} catch (error) {
  console.error("oh no!");
}

throw "not a good value";
```

## Iterators

```python
# python
arr = [1, 2, 3]
obj = {
    "a": 1,
    "b": 2,
    "c": 3
}

for val in arr:
    print(val)

for key in obj:
    print(key)
```

```javascript
// javascript
var arr = [1, 2, 3];
var obj = {
  a: 1,
  b: 2,
  c: 3
};

for (let val of arr) {
  console.log(val);
}

// or...
arr.forEach((value, index) => {
  console.log(value);
});

for (let key in obj) {
  console.log(key);
}
```

## Generators

```python
# python
def gen(x):
    while True:
        yield x
        x = x + 1
```

```javascript
// javascript
function* gen(x) {
  while (true) {
    yield x;
    x++;
  }
}
```

## Classes

```python
# python
class Thing:
    def __init__(self, a):
        self.a = a

    def add_one(self):
        return self.a + 1

class OtherThing(Thing):
    def __init__(self, a, b):
        super(OtherThing, self).__init__(a)
        self.b = b

    def add_things(self):
        return self.a + self.b
```

```javascript
// javascript
class Thing {
  constructor(a) {
    this.a = a;
  }

  addOne() {
    return this.a + 1;
  }
}

class OtherThing extends Thing {
  constructor(a, b) {
    super(a);
    this.b = b;
  }

  addThings() {
    return this.a + this.b;
  }
}
```

## Functional programming

```python
# python
expression = lambda a, b: a + b
```

```javascript
// javascript
// Arrow functions are more powerful than Python lambdas, but not in this example!
let expression = (a, b) => a + b;

// or...
let sameThing = function (a, b) {
  return a + b;
}
```

# General Javascript

A JavaScript object literal is a comma-separated list of name-value pairs wrapped in curly braces. Object literals encapsulate data, enclosing it in a tidy package. This minimizes the use of global variables which can cause problems when combining code.

Object literals are defined using the following syntax rules:

* A colon separates property name from value.
* A comma separates each name-value pair from the next.
* There should be no comma after the last name-value pair.

```javascript
var myObject = {
    sProp: 'some string value',
    numProp: 2,
    bProp: false
};
```

## Functions

Unlike constants, variables in JavaScript don’t need an initial value. You can provide one later:

```javascript
let name;
name = 'John Doe';
```

When you leave off the initial value, you create what’s called a variable declaration rather than a variable definition. Such variables automatically receive a special value of undefined, which is one of the primitive types in JavaScript. This is different in Python, where you always define variables except for variable annotations. But even then, these variables aren’t technically declared.    

## Arrow functions

Notice that there’s no function keyword anymore, and the return statement is implicit. The arrow symbol (=>) separates the function’s arguments from its body.  
When you want to return an object literal from an arrow function, you need to wrap it in parentheses to avoid ambiguity with a block of code:

```javascript
let add = (a, b) => ({
  result: a + b
});
```

Otherwise, the function body would be confused for a block of code without any return statements, and the colon would create a labeled statement rather than a key-value pair.

```javascript
// javascript function
 function funcName(param) {
  return param + 10;
}

// javascript arrow function
const funcName = (param) => param + 2
```

## Anonymous Closures

This is the fundamental construct that makes it all possible, and really is the single best feature of JavaScript. We’ll simply create an anonymous function, and execute it immediately. All of the code that runs inside the function lives in a closure, which provides privacy and state throughout the lifetime of our application.

```javascript
(function () {
  // ... all vars and functions are in this scope only
  // still maintains access to all globals
}());
```

Notice the () around the anonymous function. This is required by the language, since statements that begin with the token function are always considered to be function declarations. Including () creates a function expression instead.
