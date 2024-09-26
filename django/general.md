# Django general

## imports

Use absolute imports when importing from outside the current app.

Use explicit relative imports when importing from another module within the current app.

## urls

Always try to use underscores (the “_” character) over dashes. This isn’t just more Pythonic, it’s friendlier to more IDEs and text editors.

Note that we are referring to the name argument of `url()` here, not the actual URL typed into the browser.

```python
patterns = [
    path(route='add/', view=views.add_topping, name='toppings:add_topping'), # instead of 'toppings:add-topping'
]
```

The same rule applies for template block names.

{% raw %}

```html
{% block content_body %} # instead of 'content-body'
```

{% endraw %}

## template tags

Introspecting template tags or discovering their source can be difficult and time consuming for developers not using a very, very limited pool of IDEs. Therefore, we follow the commonly-used naming pattern of `<app_name>_tags.py`.

## model methods, manager methods, or general utility

Try to keep business logic out of views. When business logic is placed into easily reusable components, and called from within views, it makes extending components of the project to do more things much easier.

Since it’s not always possible to do this at the beginning of a project, our rule of thumb has become whenever we find ourselves duplicating business logic instead of Django boilerplate between views, it’s time to move code out of the view.

## utility functions

```python
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse

def check_sprinkles(request: HttpRequest) -> HttpRequest:
    if request.user.can_sprinkle or request.user.is_staff:
        # By adding this value here it means our display templates
        # can be more generic. We don't need to have
        # {% if request.user.can_sprinkle orrequest.user.is_staff %}
        # instead just using
        # {% if request.can_sprinkle %}
        request.can_sprinkle = True
        return request
    # Return a HTTP 403 back to the user
    raise PermissionDenied
```

You’ll note that we return back a HttpRequest object rather than an arbitrary value or even a None object. We do this because as Python is a dynamically typed language, we can attach additional attributes to the HttpRequest.
