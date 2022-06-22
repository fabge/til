# Various `aws cli` snippets

Deploy cloudformation template:

```bash
aws cloudformation deploy --template-file template.yaml --stack-name my-stack --parameter-overrides file://my-stack-parameters.json --capabilities CAPABILITY_NAMED_IAM
```
