# Access AWS resources from Azure without credentials

To access resources inside an AWS account from Azure, there is the possibility of using an IAM User, creating Access Key Id and Secret Access Key.
This solution comes with the disadvantage of static credentials.  
In an enterprise setting and in the security best practice sense as well, it is recommended to regularly rotate ones secrets and credentials.  
Rotating those credentials results in a lot of overhead and boilerplate code with the possibility of breaking the functionality.

Azure and AWS make it possible to circumvent static credentials by using Azure Managed Identities on one side and AWS Identity Provider on the other.  
[This post](https://blog.identitydigest.com/azuread-access-aws/) goes into more detail.

Create a Managed Identity on the Azure and pass the Client Id and Object Id into the following AWS Cloudformation template:

```yaml
Version: '2012-10-17'
Statement:
- Effect: Allow
  Principal:
    Federated: arn:aws:iam::<aws-account-id>:oidc-provider/sts.windows.net/<tenant-id>
  Action: sts:AssumeRoleWithWebIdentity
  Condition:
    StringEquals:
      sts.windows.net/<tenant-id>:aud: "<client-id-managed-identity>"
      sts.windows.net/<tenant-id>:sub: "<object-id-managed-identity>"

```
