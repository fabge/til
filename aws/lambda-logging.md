# Lambda logging

From https://twitter.com/elrowan/status/1714213101862588576:

Don’t use Python’s logging.basicConfig() to set up logging in AWS Lambda (even though that’s the example in the official docs). Instead, use following configuration:

```python
import logging
import os

level = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))
log = logging.getLogger(__name__)
log.setLevel(level)
```
