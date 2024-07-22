# Azure functions

There are quite some tricky things to get right when deploying Azure Functions via Bicep templates, especially using Linux as runtime.

If you want to define a hosting plan, you have to explicitly set the `reserved` property to `true` when deploying a Linux function app.

```bicep
resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
  properties: {
    reserved: true
  }
}
```

However, you **don't need** to explicitly define a Consumption hosting plan resource. When you skip this resource definition, a plan is automatically either created or selected on a per-region basis when you create the function app resource itself.

So the function app resource is defined by a resource of type `Microsoft.Web/sites` and kind that includes `functionapp`, at a minimum.

When running the function app on Linux, you must:

- Set kind to `functionapp,linux`.
- Set `reserved` to `true`.
- Set the `linuxFxVersion` property under siteConfig to the correct value for your runtime stack in the format of `<runtime>|<runtimeVersion>` (e.g. `Python|3.11`).

If you choose to optionally define your Consumption plan, you must set the `serverFarmId` property on the app so that it points to the resource ID of the plan. Make sure that the function app has a `dependsOn` setting that also references the plan. **If you didn't explicitly define a plan, one gets created for you.**

So a minimal end-to-end function app definition in a Bicep template can look like this:

```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-05-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: storageAccountType
  }
  kind: 'Storage'
}

resource applicationInsight 'Microsoft.Insights/components@2020-02-02' = {
  name: applicationInsightsName
  location: location
  properties: {
    Application_Type: 'web'
  }
  kind: 'web'
}

resource functionApp 'Microsoft.Web/sites@2022-09-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  properties: {
    reserved: true
    siteConfig: {
      linuxFxVersion: 'Python|3.11'
      appSettings: [
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: applicationInsight.properties.ConnectionString
        }
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTAZUREFILECONNECTIONSTRING'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTSHARE'
          value: toLower(functionAppName)
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
      ]
    }
  }
}
```

I would expect to be able to deploy my local source code/zip file to the function app by defining it in the the bicep template. Unfortunately there is a limitation with Azure Functions running in a Linux Consumption Plan, which makes the the appSetting `WEBSITE_RUN_FROM_PACKAGE=1` not supported. We instead would have to define a URL to the zip file in the appSetting `WEBSITE_RUN_FROM_PACKAGE=<URL>`, secure the blob storage and give the function access to the storage account. This feels to me cumbersome and increases complexity.  
In this current state I would opt to deploy the function code separately:

```bash
zip -r functionapp.zip .
az functionapp deployment source config-zip -g <resource_group> -n <app_name> --src <zip_file_path>
```

or using azure functions core tools, skipping the zip file creation:

```bash
func azure functionapp publish <app_name>
```
