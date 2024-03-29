# Django setup tl;dr

## Basic

```bash
django-admin startproject core
mv core app
cd app
python manage.py startapp main
touch main/urls.py
mkdir static templates
touch requirements.txt
touch templates/base.html
touch templates/index.html
touch templates/data.html
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
    path("__reload__/", include("django_browser_reload.urls")),
]
```

```python
# core/settings.py

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    'main.apps.MainConfig',
    ...
    'tailwind',
    'django_browser_reload',
    'django_extensions',
]

MIDDLEWARE = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    ...
]

TEMPLATES = [{
    ...
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    ...
}]

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
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
Django==5.0
django_browser_reload==1.12.1
django-tailwind==3.6.0
whitenoise==6.6.0
django-extensions==3.2.3
```

**tailwind**

https://django-tailwind.readthedocs.io/en/latest/installation.html#installation

```bash
python manage.py tailwind init
```

```python
# core/settings.py

INSTALLED_APPS = [
  ...
  'theme',
]

TAILWIND_APP_NAME = 'theme'
```

```bash
python manage.py migrate
```

**README.md**

python manage.py runserver

python manage.py tailwind start

python manage.py shell_plus --notebook

## Jupyter notebook

https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
