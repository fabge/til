# Django models

## `null=True` and `blank=True`

`null=True` and `blank=True` are two different concepts in Django models.

- `null=True` specifies that the database column will accept NULL values.
- `blank=True` specifies that the field is allowed to be blank in forms.

For example, if you have a `CharField` in your model and you want to allow empty strings in the database, you should set `null=True`:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True)
```

If you want to allow empty strings in forms, you should set `blank=True`:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=True)
```

## `created` and `modified` fields

Create a model which as a `created` and `modified` field. This is useful for tracking when a record was created and last updated.

```python
from django.db import models

class SimpleTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

Then, inherit from this model in your models.

```python
from django.db import models

class MyModel(SimpleTimeStampedModel):
    name = models.CharField(max_length=100)
```

Now, whenever you create or update a `MyModel` instance, the `created` and `modified` fields will be automatically updated.

### Using `update_fields` with `save()`

When you call `save()` on a model instance, you can pass an `update_fields` argument to specify which fields should be updated. This can be useful when you only want to update specific fields.  
However, if you pass `update_fields` to `save()`, the `modified` field will not be updated.
The `CustomTimeStampedModel` below fixes this issue.

```python
from django.db import models

class CustomTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields:
            kwargs['update_fields'] = set(update_fields).union({'modified'})
        super().save(*args, **kwargs)
```

Now, when you call `save()` with `update_fields`, the `modified` field will be updated as well.

```python
my_model = MyModel.objects.get(pk=1)
my_model.name = 'New Name'
my_model.save(update_fields=['name'])
```

## `slug` field

Create a model which has a `slug` field. This is useful for creating SEO-friendly URLs.
Using `AutoSlugField` from `django-autoslug` makes this easy.

```python
from django.db import models
from autoslug import AutoSlugField

class Example(models.Model):
    name = models.CharField(max_length=100)
    slug = models.AutoSlugField(unique=True, always_update=False, populate_from="name")
```

TODO:

Since CountryField is an extension of CharField, we treat it similarly. We want country_of_origin to be optional, since it might be unknown for some cheeses, and so we set blank=True. But we don’t set null=True because Django’s convention is to store empty values as the empty string, and to retrieve NULL/empty values as the empty string. (See Two Scoops of Django for a more detailed explanation.)
