# Databricks authentication with Azure

The official Databricks/Azure documentation to access a Azure Blob Storage suggests following ways to authenticate:

- OAuth 2.0 with a Microsoft Entra ID service principal
- Shared access signatures (SAS)
- Account keys

All of those methods require hard-coded credentials somewhere in the code or the environment, which is something i would like to avoid - especially if all of the code is stored in a git repository.

Fortunately, there is a better way - using managed identities. It is not documented properly, but can be used just as well:

1. Databricks creates a managed identity in its managed resource group, aptly named `dbmanagedidentity`. Get the client id of this managed identity.
2. Assign the `Storage Blob Data Contributor` role to this managed identity, scoped to the storage account you want to access.

## 1. Using the Azure SDK

Use the following code to access the storage account:

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from io import StringIO
import pandas as pd

account_url = "https://databricksfabian.blob.core.windows.net/"
container_name = "test"
blob_name = "example.csv"

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

data = blob_client.download_blob(encoding='utf8').readall()
df = pd.read_csv(StringIO(data))
```

## 2. Using Databricks' spark configuration

Use the following code to access the storage account:

```python
spark.conf.set("fs.azure.account.auth.type", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.MsiTokenProvider")
spark.conf.set("fs.azure.account.oauth2.msi.tenant", "<tenant-id>")
spark.conf.set("fs.azure.account.oauth2.client.id", "<managed-identity-client-id>")

df = spark.read.format("csv").load("abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<file-name>")
```
