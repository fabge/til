# Remove Azure DevOps Retention Leases

There maybe hundreds of builds in an Azure DevOps build pipeline with Retention Leases, which prevent the deletion of the build pipeline.

Following Python script loops through all builds and removes the retention leases.

```python
import requests
AZURE_DEVOPS_PAT = "pswd"
BASE_URL = "https://dev.azure.com/org/project"
HEADERS = {"Content-Type": "application/json-patch+json"}
BUILD_DEFINITION_ID = '750'

url = f"{BASE_URL}/_apis/build/builds?definitions={BUILD_DEFINITION_ID}"
response = requests.get(
    url,
    headers=HEADERS,
    auth=("", AZURE_DEVOPS_PAT),
)
builds = response.json()['value']
for build in builds:
    if not build['retainedByRelease']:
        continue
    response = requests.get(
        f"{BASE_URL}/_apis/build/builds/{build['id']}/leases?api-version=7.1-preview.1",
        headers=HEADERS,
        auth=("", AZURE_DEVOPS_PAT),
    )
    for lease in response.json()['value']:
        response = requests.delete(
            f"{BASE_URL}/_apis/build/retention/leases?ids={lease['leaseId']}&api-version=6.0-preview.1",
            headers=HEADERS,
            auth=("", AZURE_DEVOPS_PAT),
        )
```
