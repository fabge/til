# Invoke the Azure API via HTTP endpoints

Authenticating against the Azure REST API can be very tricky. Usually you are advised to create an App Registration/Service Principal, get the Cliend Id and create a Client Secret, use those to get a token and authenticate with said token against the request.

## az cli

There is a much simpler way - using [`az rest`](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-rest).  
To authenticate and invoke a custom HTTP endpoint, you have to have `az cli` installed and be logged in. Using `az rest` automatically authenticates using the logged-in credential: If Authorization header is not set, it attaches header `Authorization: Bearer <token>`:

```bash
az rest method get --url "https://management.azure.com/providers/Microsoft.Billing/billingAccounts?api-version=2019-10-01-preview"
```

Or with `PUT` method:

```bash
az rest --method put --url "https://management.azure.com/providers/Microsoft.Billing/billingAccounts/4858737/billingRoleAssignments/326c745a-d97d-46d0-9d81-8b49545d09c3?api-version=2019-10-01-preview" --body @body.json
```

## python

Using python, we get the `token` from the `DefaultAzureCredential` and use that to authenticate against the REST API by setting the `Authorization` header.

```python
import requests
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://management.azure.com/.default")

response = requests.get(
    "https://management.azure.com/providers/Microsoft.Billing/billingAccounts?api-version=2019-10-01-preview",
    headers={"Authorization": f"Bearer {token.token}"},
)

print(response.json())
```
