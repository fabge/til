# Django setup tl;dr

## Basic

```bash
django-admin startproject core
mv core app
cd app
python manage.py startapp main
touch main/urls.py
mkdir static templates
touch templates/base.html
touch templates/index.html
```

```python
# main/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def data(request, data_id):
    return render(request, 'data.html', {'data_id': data_id})
```

```python
# main/urls.py
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/<int:data_id>/', views.data, name='data'),
]
```

```python
# core/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

```python
# core/settings.py

INSTALLED_APPS = [
    'main.apps.MainConfig',
    ...
]

TEMPLATES = [{
    ...
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    ...
}]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

```text
/project/
    |-- core/
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        |-- wsgi.py
    |-- main/
        |-- __init__.py
        |-- admin.py
        |-- apps.py
        |-- models.py
        |-- tests.py
        |-- urls.py
        |-- views.py
    |-- static/
        |-- input.css
        |-- output.css
    |-- templates/
        |-- base.html
        |-- index.html
        |-- detail.html
    |-- manage.py
```

{% raw %}

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}YOUR TITLE{% endblock %}</title>
    {% load static tailwind_tags %}
    {% tailwind_css %}
    <script src="https://unpkg.com/htmx.org@1.9.6"></script>
    {% block head %}{% endblock %}
</head>
<body>
    <div>
        <a href="{% url 'index' %}">YOUR INDEX</a>
    </div>
    {% block content %}{% endblock content %}
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %}
{% block title %}YOUR TITLE{% endblock %}
{% block content %}
    <div>
        <a href="{% url 'data' 1 %}">YOUR DATA</a>
    </div>
{% endblock content %}
```

```html
<!-- templates/data.html -->
{% extends 'base.html' %}

{% block content %}
<h1>hello world</h1>
{% endblock %}
```

{% endraw %}

```txt
# requirements.txt
Django==4.2.7
django-tailwind[reload]==3.6.0
```

## Tailwind

https://django-tailwind.readthedocs.io/en/latest/installation.html#installation

## Jupyter notebook

https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
