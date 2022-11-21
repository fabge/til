
# Assume a role across AWS accounts

Assuming a role in another account can be tricky.

```python
import boto3
sts_client = boto3.client('sts')
assumed_role_object = sts_client.assume_role(
    RoleArn=f'arn:aws:iam::{AWS_ACCOUNT_ID}:role/{ROLE_TO_ASSUME}',
    RoleSessionName='AssumedRoleSession'
)
```

The above snippet returns an object which contains the credentials. With those credentials the client with the respective service can be assumed. Below the example uses the `lambda` service.

```python
credentials = assumed_role_object['Credentials']
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)
```
