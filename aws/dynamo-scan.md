# DynamoDB table scan

There are two ways to scan a DynamoDB table. The first is to use the `scan` method on the table object. The second is to use the `scan` method on the client object.  
I prefer the first one because the response is easier to work with.

## Scan method on the table object

```python
import boto3
table = boto3.resource('dynamodb').Table('my-table')
response = table.scan()
print(response['Items'])
# {'Items': [{'id': 'a8cea0e8-2d5f-4772-9440-2820c0ef44b9'},
# ...
```

## Scan method on the client object

```python
import boto3
client = boto3.client('dynamodb')
response = client.scan(TableName='my-table')
print(response['Items'])
# {'Items': [{'id': {'S': 'a8cea0e8-2d5f-4772-9440-2820c0ef44b9'}},
# ...
```
