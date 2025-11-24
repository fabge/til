# api for aws, azure, gcp

the following describes various methods to authenticate and interact with aws, azure, and gcp clouds - specifically using python.
i am describing my most used paths here - no claim of being complete.

## aws

aws is straightfoward to interact with, as `boto3` is the official aws sdk for python and is well maintained.

the authentication happens through the aws cli. when authenticated against an account, `boto3` will automatically pick up the credentials from the aws cli configuration.

```bash
# login usen aws cli (in this case sso with profile default)
aws sso login
```

```python
import boto3
client = boto3.client('s3')
client.list_buckets()
```

## azure

azure interaction can be done through the `azure` sdk for python, but i have had bad experiences with it being outdated, not well maintained or not full featured. this is why i tend to use the vanilla azure rest api with python's `requests` library.

authentication can be done in multiple ways, but the most straightforward is using the `DefaultAzureCredential` class from the `azure-identity` package, which supports various authentication methods including environment variables, managed identities, and azure cli login.

```bash
# login using azure cli - and select the right subscription
az login
```

```python
from azure.identity import DefaultAzureCredential
import requests
credential = DefaultAzureCredential()
token = credential.get_token("https://management.azure.com/.default").token
headers = {"Authorization": f"Bearer {token}"}
url = "https://management.azure.com/subscriptions/[SUBSCRIPTION_ID]/providers/Microsoft.Storage/storageAccounts?api-version=2025-06-01"
response = requests.get(url, headers=headers)
print(response.json())
```

## gcp

gcp interaction can be done through the `google-cloud` sdk for python.

authentication can be done using the `google-auth` library, which supports various methods including application default credentials and service account keys.

```bash
# login using gcloud cli
gcloud auth application-default login
gcloud auth application-default set-quota-project [PROJECT_ID]
```

```python
from google.cloud import storage
client = storage.Client()
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)
```
