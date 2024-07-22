# Monkey Patching

In Python you can modify the behavior of a class or module at runtime by adding new methods or attributes. This is called monkey patching.

Here is an example: Sometimes I found it useful to have additional error logging when calling `raise_for_status` on a requests response. This can be achieved by monkey patching the `Response` class:

```python
import requests

def custom_raise_for_status(self):
    try:
        self.old_raise_for_status()
    except requests.exceptions.HTTPError as e:
        if err.response.text:
            print(err.response.text)
        raise

requests.models.Response.old_raise_for_status = requests.models.Response.raise_for_status
requests.models.Response.raise_for_status = custom_raise_for_status

response = requests.get('https://example.com/12341234')
response.raise_for_status()
```

or you can use a decorator:

```python
import requests

def patched_raise_for_status(func):
    def wrapper(self):
        try:
            return func(self)
        except requests.exceptions.HTTPError as e:
            if err.response.text:
                print(err.response.text)
            raise
    return wrapper

requests.models.Response.raise_for_status = patched_raise_for_status(requests.models.Response.raise_for_status)

response = requests.get('https://example.com/12341234')
response.raise_for_status()
```

... with @wraps, keeping the original function signature, such as the original function's metadata, like docstring, module information, etc.:

```python
from functools import wraps
import requests

def patched_raise_for_status(func):
    @wraps(func)
    def wrapper(self):
        try:
            return func(self)
        except requests.exceptions.HTTPError as e:
            if err.response.text:
                print(err.response.text)
            raise
    return wrapper
```
