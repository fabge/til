# Django User

(from: https://docs.djangoproject.com/en/5.1/topics/auth/customizing/)

When starting a new project, it’s highly recommended to set up a custom user model, even if the default `User` model is sufficient. This model behaves identically to the default user model, but makes it easy to customize it in the future if the need arises:

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

Don’t forget to point `AUTH_USER_MODEL` to it. Do this before creating any migrations or running manage.py migrate for the first time.

Also, register the model in the app’s `admin.py`:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
