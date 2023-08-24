# DynamoDB Global Secondary Indexes

The following table has two global secondary indexes, `account-email-idx` and `workspace-project-idx`. The first index is a simple index that allows you to query by `AccountEmail`. The second index is a composite index that allows you to query by `WorkspaceId` and `ProjectId`.

```yaml
  AccountTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: AccountId
          AttributeType: S
        - AttributeName: AccountEmail
          AttributeType: S
        - AttributeName: WorkspaceId
          AttributeType: S
        - AttributeName: ProjectId
          AttributeType: S
      KeySchema:
        - AttributeName: AccountId
          KeyType: HASH
      GlobalSecondaryIndexes:
        - IndexName: account-email-idx
          KeySchema:
            - AttributeName: AccountEmail
              KeyType: HASH
          Projection:
            ProjectionType: KEYS_ONLY
        - IndexName: workspace-project-idx
          KeySchema:
            - AttributeName: WorkspaceId
              KeyType: HASH
            - AttributeName: ProjectId
              KeyType: RANGE
          Projection:
            ProjectionType: ALL
      StreamSpecification:
        StreamViewType: KEYS_ONLY
```

The below query will return all items that have the `WorkspaceId` of `workspace`. The `ProjectId` is the range key, so the results will be sorted by `ProjectId`.

```python
    items = account_table().query(
        IndexName='workspace-project-idx',
        KeyConditionExpression=Key('WorkspaceId').eq(workspace),
    ).get('Items', [])
```

If you also want to filter by ProjectId, you could set the `ProjectId` as the `HASH` key in the index of the CloudFormation template and then can add a `FilterExpression` to your query:

```python
    items = account_table().query(
        IndexName='workspace-project-idx',
        KeyConditionExpression=Key('WorkspaceId').eq(workspace),
        FilterExpression=Attr('ProjectId').eq(project),
    ).get('Items', [])
```
