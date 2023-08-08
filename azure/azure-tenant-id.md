# Find Azure Tenant Id by Subscription Id

You can find the tenant id by subscription id by using the following code:

```python
host_name = 'management.azure.com'
api_version = '2020-08-01'
url = f'https://{host_name}/subscriptions/{subscription_id}/?api-version={api_version}'
response = get(url)
header = response.headers.get('WWW-Authenticate')
tenant_id = ''
if header:
    tenant_id = search(r'(?<=https:\/\/login.windows.net\/).*?(?=")', header).group()
```
