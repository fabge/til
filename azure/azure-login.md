# az login

Using `az cli`:

```bash
az login --tenant <tenant-id>
az account set --subscription <subscription-id>
```

Using Powershell:

```powershell
Connect-AzAccount -Tenant <tenant-id> -Subscription <subscription-id>
```

Using a service principal:

```bash
az login --service-principal -u <client-id> -p <client-secret> --tenant <tenant-id>
```

Using a service principal with federated authentication (against AWS):

```bash
identityPoolId=$(aws cognito-identity list-identity-pools --max-results 1 --query "IdentityPools[].IdentityPoolId" --output text)
federatedToken=$(aws cognito-identity get-open-id-token-for-developer-identity --token-duration 86400 --identity-pool-id $identityPoolId --logins federated-identities=<client-id> --query Token --output text)
az login --service-principal -u <client-id> -t <tenant-id> --federated-token $federatedToken
```
