# Azure functions

There are quite some tricky things to get right when deploying Azure Functions, especially using Linux as the runtime.

When deploying via Bicep templates, following parameters have to be set explicitly:

You don't need to explicitly define a Consumption hosting plan resource. When you skip this resource definition, a plan is automatically either created or selected on a per-region basis when you create the function app resource itself.  
If you do however want to define a hosting plan, you have to explicitly set the `reserved` property to `true` when deploying a Linux function app.

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

When running the function app on Linux, you must:
