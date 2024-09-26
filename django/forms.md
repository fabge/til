# Django forms

## form validation

## reuse a form template for create and update

If you want to reuse a form template for e.g. creating and updating a model instance, there is a trick to specify the action:

Instead of

{% raw %}

```html
<form method="post" action="{% url 'cheeses:add' %}">
<!-- and -->
<form method="post" action="{% url 'cheeses:edit' %}">
```

{% endraw %}

you can use

```html
<form method="post" action=".">
```

Using `action="."` as is a commonly-used trick to reuse a form template for both create and update views.
