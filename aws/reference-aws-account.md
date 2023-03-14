# Reference AWS account

In some IAM policies, you need to permit an AWS account to perform an action. There are two common ways to do this (from the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)):

```json
"Principal": { "AWS": "arn:aws:iam::123456789012:root" }
```

```json
"Principal": { "AWS": "123456789012" }
```

The account ARN and the shortened account ID behave the same way. Both delegate permissions to the account. Using the account ARN in the Principal element **does not limit permissions to only the root user of the account**.
