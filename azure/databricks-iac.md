# Set up Databricks via Bicep

When trying to set up Databricks via Bicep, I ran into the following error:

```text
Managed Resource group for the workspace: '/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/test-rg' doesn't have managed by property referring to Databricks workspace resource (Code: ApplianceProvisioningFailed)
```

This is because the managed resource group is not being created by the Databricks Bicep template.

To fix this, we need to construct the managed resource group name in a certain way and pass it to the Databricks Bicep template.

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
