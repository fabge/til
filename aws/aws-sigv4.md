# AWS SigV4 using `curl`

`curl` supports AWS SigV4 natively. This allows you to make requests to AWS APIs directly without having to use the AWS SDKs.

Below is an example equest to an IAM-authenticated API Gateway REST API:

```bash
curl --request POST \
'https://<api-id>.execute-api.<aws-region>.amazonaws.com/prod/search' \
--aws-sigv4 'aws:amz:<aws-region>:execute-api' \
--user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
--header "x-amz-security-token: ${AWS_SESSION_TOKEN}" \
--header 'Accept: application/json' \
--data '{"query": "sports"}' \
| jq .
```
