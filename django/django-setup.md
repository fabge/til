# Django setup tl;dr

Most basic setup, without database.

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

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

```bash
python manage.py runserver
```
