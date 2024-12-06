# Set up Databricks via Bicep

```bicep
param workspaceName string = 'databricks-workspace'
param location string = resourceGroup().location

var managedResourceGroupName = 'databricks-rg-${workspaceName}-${uniqueString(workspaceName, resourceGroup().id)}'

resource ws 'Microsoft.Databricks/workspaces@2018-04-01' = {
 name: workspaceName
 location: location
 sku: {
   name: 'standard'
 }
 properties: {
   managedResourceGroupId: managedResourceGroup.id
   parameters: {
     enableNoPublicIp: {
       value: false
     }
   }
 }
}

resource managedResourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' existing = {
 scope: subscription()
 name: managedResourceGroupName
}

```
