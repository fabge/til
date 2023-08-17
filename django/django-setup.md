# Django setup tl;dr

Most basic setup, without database.

{% raw %}

```bash
django-admin startproject main
cd main
touch views.py
```

```python
# main/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def data(request, data_id):
    return render(request, 'detail.html', {'data_id': data_id})
```

```python
# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/<int:data_id>/', views.detail, name='data'),
]
```

```python
# main/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        ...

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

```text
/project/
    |-- main/
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        |-- views.py
        |-- wsgi.py
    |-- static/
        |-- input.css
        |-- output.css
    |-- templates/
        |-- base.html
        |-- index.html
        |-- detail.html
    |-- manage.py
```

```html
{% load static %}

<link rel="stylesheet" href="{% static 'style.css' %}">

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

```bash
python manage.py runserver
```

{% endraw %}
