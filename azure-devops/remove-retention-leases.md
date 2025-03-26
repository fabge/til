# Remove Azure DevOps Retention Leases

There maybe hundreds of builds in an Azure DevOps build pipeline with Retention Leases, which prevent the deletion of the build pipeline.

Following Python script loops through all builds and removes the retention leases.

```python
import requests

AZURE_DEVOPS_PAT = "pswd"
BASE_URL = "https://dev.azure.com/org/project"
BUILD_DEFINITION_ID = '750'

session = requests.Session()
session.headers.update({"Content-Type": "application/json-patch+json"})
session.auth = ("", AZURE_DEVOPS_PAT)

response = session.get(f"{BASE_URL}/_apis/build/builds?definitions={BUILD_DEFINITION_ID}")
builds = response.json()['value']

for build in builds:
    if not build['retainedByRelease']:
        continue
    response = session.get(f"{BASE_URL}/_apis/build/builds/{build['id']}/leases?api-version=7.1-preview.1")
    for lease in response.json()['value']:
        response = session.delete(f"{BASE_URL}/_apis/build/retention/leases?ids={lease['leaseId']}&api-version=6.0-preview.1")
```
