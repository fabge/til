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

```html
{% block content_body %} # instead of 'content-body'
```

## template tags

Introspecting template tags or discovering their source can be difficult and time consuming for developers not using a very, very limited pool of IDEs. Therefore, we follow the commonly-used naming pattern of `<app_name>_tags.py`.
