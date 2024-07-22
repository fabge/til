# Monkey Patching

In Python you can modify the behavior of a class or module at runtime by adding new methods or attributes. This is called monkey patching.

Here is an example: Sometimes I found it useful to have additional error logging when calling `raise_for_status` on a requests response. This can be achieved by monkey patching the `Response` class:

```python
import requests

def new_raise_for_status(self):
    try:
        self.old_raise_for_status()
    except requests.exceptions.HTTPError as e:
        if err.response.text:
            print(err.response.text)
        raise

requests.models.Response.old_raise_for_status = requests.models.Response.raise_for_status
requests.models.Response.raise_for_status = new_raise_for_status

response = requests.get('https://example.com/12341234')
response.raise_for_status()
```

slightly different:

```python
from requests import HTTPError, Response
import requests

original_raise_for_status = Response.raise_for_status

def custom_raise_for_status(self) -> None:
    try:
        original_raise_for_status(self)
    except HTTPError as err:
        if err.response.text:
            print(err.response.text)
        raise

Response.raise_for_status = custom_raise_for_status

r = requests.post('https://example.com/12341234')

r.raise_for_status()
```

or you can use a decorator:

```python
import requests

def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            if err.response.text:
                print(err.response.text)
            raise
    return wrapper

requests.models.Response.raise_for_status = log_errors(requests.models.Response.raise_for_status)

response = requests.get('https://example.com/12341234')
response.raise_for_status()
```
