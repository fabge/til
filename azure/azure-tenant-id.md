# Find Azure Tenant Id by Subscription Id

You can find the tenant id by subscription id by using the following code:

```python
import re
import requests

subscription_id = 'ed20c67e-57c6-4b04-8a7f-9f25f4d8ea56'
url = f'https://management.azure.com/subscriptions/{subscription_id}/?api-version=2020-08-01'
response = requests.get(url)
if header:= response.headers.get('WWW-Authenticate'):
    tenant_id = re.search(r'(?<=https:\/\/login.windows.net\/).*?(?=")', header).group()
```

Somewhat hacky, but it works.
