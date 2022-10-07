# Safely Pass Data to JavaScript in a Django Template

from: [How to Safely Pass Data to JavaScript in a Django Template](https://adamj.eu/tech/2022/10/06/how-to-safely-pass-data-to-javascript-in-a-django-template/)

I have done this wrong in the past.

```python
{# DON’T DO THIS #}
<script>
    const username = "{{ username }}";
</script>
```

Most of the time, I pass complex data structures to Javascript. So this is the most relevant part to me:

```html
{{ follower_chart|json_script:"follower-chart-data" }}
```

Django renders this as:

```html
<script id="follower-chart-data" type="application/json">[{"date": "2022-10-05", "count": 11}, {"date": "2022-10-06", "count": 12}]</script>
```

You can then use `document.getElementById()` to find the data `<script>` elements, and JSON.parse() again to parse the contained data:

```html
const followerData = JSON.parse(
  document.getElementById('follower-chart-data').textContent
);
```
