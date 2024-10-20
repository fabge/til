# uv - single file scripts

uv includes first-class support for single-file Python scripts with inline dependency metadata.

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests<3",
#     "rich",
# ]
# ///
import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

From there, uv run main.py will execute the script in an isolated, ephemeral virtual environment with all of its dependencies installed.
(from https://astral.sh/blog/uv-unified-python-packaging)
