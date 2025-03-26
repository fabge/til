# Django User

## custom user model

(from: <https://docs.djangoproject.com/en/5.1/topics/auth/customizing/>)

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

## custom user fields

### option 1: subclass AbstractUser

Choose this option if you like Django’s `User model` fields the way they are, but need extra fields. For what it’s worth, this is the first approach that we look at anytime we start a new project. When using django-authtools’ base models, forms, and admin objects, we find that it’s the quickest and easiest way to implement custom user models.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class KarmaUser(AbstractUser):
    karma = models.PositiveIntegerField(verbose_name='karma', default=0, blank=True)
```

### option 2: subclass AbstractBaseUser

`AbstractBaseUser` is the bare-bones option with only 3 fields: `password`, `last_login`, and `is_active`.

Choose this option if:

- You’re unhappy with the fields that the User model provides by default, such as first_name and last_name.
- You prefer to subclass from an extremely bare-bones clean slate but want to take advantage of the AbstractBaseUser sane default approach to storing passwords.

### option 3: linking back from a related model

To make this technique work, we continue to use `django.contrib.models.User` (called preferably via `django.contrib.auth.get_user_model()`) and keep your related fields in separate models (e.g. `Profiles`). Here’s an example:

```python
from django.conf import settings
from django.db import models
from flavors.models import Flavor

class EaterProfile(models.Model):
    # Default user profile
    # If you do this you need to either have a post_save signal or redirect to a profile_edit view on initial login.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    favorite_ice_cream = models.ForeignKey(Flavor, null=True, blank=True)

class ScooperProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    scoops_scooped = models.IntegerField(default=0)
```

## handling multiple user types

### add a user type field

This approach assumes different roles have the same data and methods available to them. In the user model, add a choices field distingishing between types of users. This allows for role checks across a Django project.

```python
class User(AbstractUser):
    class Types(models.TextChoices):
        EATER = "EATER", "Eater"
        SCOOPER = "SCOOPER", "Scooper"
        INVENTOR = "INVENTOR", "Inventor"

    # What type of user are we?
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.EATER)
```

### add a user type field plus proxy models

It is typical for different types of users to have different methods and properties. For example, a SCOOPER would have a scoop_icecream() method and an EATER would have a consume() method.

```python
class User(AbstractUser):
    class Types(models.TextChoices):
        EATER = "EATER", "Eater"
        SCOOPER = "SCOOPER", "Scooper"
        INVENTOR = "INVENTOR", "Inventor"

    # What type of user are we?
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.EATER)

    def save(self, *args, **kwargs):
        # If a new user, set the user's type based off the
        # base_type property
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)
```

and in `models.py``

```python
class InventorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.INVENTOR)

class Inventor(User):
    # This sets the user type to INVENTOR during record creation
    base_type = User.Types.INVENTOR
    # Ensures queries on the Inventor model return only Inventors
    objects = InventorManager()

    # Setting proxy to "True" means a table WILL NOT be created
    # for this record
    class Meta:
        proxy = True

    # Only inventors get to invent new flavors!
    def invent(self):
        # Magical custom logic goes Here
        return "Delicious!"
```

As mentioned in the comments, proxy models don’t add fields. What they do create is references to a model object on which we can hang custom managers, methods, and properties.  
The example queries below will show the power of this approach

```python
>>> from users.models import User, Inventor
>>> User.objects.count() # Over 300 million users!
323482357
>>> Inventor.objects.count() # But only 3 inventors
3
>>> # Calling someone as both a User and an Inventor
>>> user = User.objects.get(username='umafeldroy')
>>> user
<User: uma>
>>> inventor = Inventor.objects.get(username='umafeldroy')
>>> inventor
<Inventor: uma>
>>> # Calling a method that's only for inventors
>>> user.invent()
AttributeError
>>> inventor.invent()
'Delicious'
```

The proxy approach gives us multiple types of users without creating a new User table or being forced to dramatically extend django.contrib.auth in such a way that we can’t use third-party libraries.

That proxy models can have their own model managers means that we can have more ex-
plicit queries. This helps prevent mistakes in granting permission. Compare these two code
examples for clarity:

```python
User.objects.filter(type=User.Types.INVENTOR)
Inventor.objects.filter()
```

## adding extra data fields

1. Use `OneToOneField` relations to profile model
1. Put all the fields in the base User model. This approach is simple, but with enough users and user-specific data can result in the User table slowing. Even without performance considerations in, there is significant risk of innappropiate data being held by the wrong user type.

Our preference is the first option, to link back from a related model and combine with proxy models.

```python
class Inventor(User):
    # ...
    objects = InventorManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.inventorprofile

class Scooper(User):
    # ...
    objects = ScooperManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.scooperprofile

class Eater(User):
    # ...
    objects = EaterManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.eaterprofile
```

We really like this approach, it is easy to remember that the relation to the profile table is accessible via the extra property. It even works with architectures that allow users to have more than one role.

Proxy models are something typically used sparingly as complex implementations can be confusing. However, under the right circumstances such as multiple user types, they are incredibly useful.

## using `get_user_model()` to get the custom user model

```python
from django.contrib.auth import get_user_model

get_user_model()
# <class django.contrib.auth.models.User>
# or when using a custom user model
# <class profiles.models.UserProfile>
```

## using settings.AUTH_USER_MODEL for Foreign Keys to User

In Django, the official preferred way to attach ForeignKey, OneToOneField, or ManyToManyField to User is as follows:

```python
from django.conf import settings
from django.db import models

class IceCreamStore(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
```
