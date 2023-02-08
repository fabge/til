# Access AWS resources from Azure without credentials

To access resources inside an AWS account from Azure, there is the possibility of using an IAM User, creating Access Key Id and Secret Access Key.
This solution comes with the disadvantage of static credentials.  
In an enterprise setting and in the security best practice sense as well, it is recommended to regularly rotate ones secrets and credentials.  
Rotating those credentials results in a lot of overhead and boilerplate code with the possibility of breaking the functionality, especially if multiple parties are involved.

Azure and AWS make it possible to circumvent static credentials by using Azure Managed Identities on one side and AWS Identity Provider on the other. [This post](https://blog.identitydigest.com/azuread-access-aws/) goes into more detail.
Some Azure Services, like Azure Synapse, do not allow to use Managed Identities. Instead you can use an Azure App Registration to authenticate against AWS.

Create an Azure App Registration pass the Application ID URI, Azure Active Directory Tenant Id and Thumbprint into an AWS CloudFormation Template.  
The Thumbprint has to be generated once by going into the AWS Console -> `IAM` -> `Identity Providers` -> `Add provider` -> `OpenID Connect`, enter the Provider URL `https://sts.windows.net/[your-tenant-id]` and click on `Get thumbprint`.

```yaml
AppRegistrationOidc:
  Type: AWS::IAM::OIDCProvider
  Properties:
    ClientIdList:
      - !Ref AppRegistrationIdUri
    ThumbprintList:
      - !Ref Thumbprint
    Url: !Sub 'https://sts.windows.net/${TenantId}/'

AppRegistrationRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument: !Sub
      - |
        {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Federated": "${AppRegistrationOidc}"
                  },
                  "Action": "sts:AssumeRoleWithWebIdentity",
                  "Condition": {
                      "StringEquals": {
                        "sts.windows.net/${TenantId}/:aud": "${AppRegistrationIdUri}"
                      }
                  }
              }
          ]
        }
      - {
          "AppRegistrationOidc": !Ref AppRegistrationOidc,
          "AppRegistrationIdUri": !Ref AppRegistrationIdUri,
          "TenantId": !Ref TenantId
        }
```

The AssumeRolePolicyDocument is formatted via !Sub and JSON to be able to substitute the `TenantId` in the key of the `StringEquals` condition.

To assume the role, you have to generate a token with the correct audience and then use the `sts:AssumeRoleWithWebIdentity` action.

```python
from azure.identity import ClientSecretCredential
import boto3

credential = ClientSecretCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
    client_secret="<client-secret>"
)

result = credential.get_token("<AppRegistrationIdUri>")
token = result[0]

sts_client = boto3.client('sts')
assumed_role_object = sts_client.assume_role_with_web_identity(
    RoleArn='arn:aws:iam::<aws-account-id>:role/<arn of the AppRegistrationRole>',
    RoleSessionName='CoolSession',
    WebIdentityToken=token)

credentials = assumed_role_object['Credentials']

s3_client = boto3.client(
  's3',
  aws_access_key_id=credentials['AccessKeyId'],
  aws_secret_access_key=credentials['SecretAccessKey'],
  aws_session_token=credentials['SessionToken']
)
```
