# Django queries

## lazy evaluation

Django ORM doesn’t make the SQL calls until the data is actually needed. We can chain ORM methods and functions as much as we want, and until we try to loop through the result, Django doesn’t touch the database.

Instead of being forced to chain many methods and advanced database features on a single line, we can break them up over as many lines as needed. This increases readability, which improves the ease of maintenance, which increases time for getting ice cream.

```python

from django.db.models import Q
from promos.models import Promo

def fun_function(name=None):
    """Find working ice cream promo"""
    results = Promo.objects.active()
    results = results.filter(
        Q(name__startswith=name) |
        Q(description__icontains=name)
    )
    results = results.exclude(status='melted')
    results = results.select_related('flavors')
    return results
```

## advanced queries

Django’s ORM is easy to learn, intuitive, and covers many use cases. Yet there are a number of things it does not do well. What happens then is that, after the queryset is returned, we begin processing more and more data in Python. This is a shame, because every database manages and transforms data faster than Python (or Ruby, JavaScript, Go, Java, et al).

Instead of managing data with Python, we always try to use Django’s advanced query tools to do the lifting. In doing so we not only benefit from increased performance, we also enjoy using code that is more proven (Django and most databases are constantly tested) than any Python-based workarounds we create.

```python
from django.db.models import F

from models.customers import Customer

customers = Customer.objects.filter(scoops_ordered__gt=F('store_visits'))
```

`F` expressions allow us to reference model fields in a query. This is useful when we want to compare two fields or perform an operation on a field.
