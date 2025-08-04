# Update DynamoDB item

The [official AWS documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-4.html) example on how to update a DynamoDB item looks fairly cumbersome and complex:

```python
table.update_item(
    Key={"year": year, "title": title},
    UpdateExpression="set info.rating=:r, info.plot=:p",
    ExpressionAttributeValues={":r": Decimal(str(rating)), ":p": plot},
    ReturnValues="UPDATED_NEW",
)
```

If you don't want to define those parameters in as much detail, you can use the `put_item` method which allows you to pass the `Item` parameter as a dictionary. Note that it will replace the entire item with the new one or create a new one if it doesn't exist.

```python
import boto3

table = boto3.resource('dynamodb').Table('tablename')
items = table.scan()['Items']

for item in items:
    item['parameter_to_update'] = 'new_value'
    table.put_item(Item=item)
```
