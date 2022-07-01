# Pagination using AWS boto3

When the returned instances of an AWS boto3 call exceed a certain threshold, the response is paginated and additionally returns a `NextToken`.

I used to walk through those paginated responses in a fairly cumbersome way:

```python
client = boto3.client('cloudformation')
stacks = client.list_stack_instances(StackSetName='test-stack')
stack_instances = response['Summaries']
while 'NextToken' in response:
    response = cloudformation.list_stack_instances(StackSetName='test-stack', NextToken=response.get('NextToken'))
    stack_instances += response['Summaries']
```

The problem above is the duplicate `list_stack_instances` method call.  
Another way without having to call the method twice would look like this:

```python
client = boto3.client('cloudformation')
stack_instances = []
next_token = None
first = True
while first or next_token:
    first = False
    kwargs = {"StackSetName": test-stack}
    if next_token:
        kwargs["NextToken"] = next_token
    response = cloudformation.list_stack_instances(**kwargs)
    stack_instances.extend(response["Summaries"])
    next_token = response.get("NextToken")
```

The code looks too verbose to me though.
There is a convenient `get_pagination()` method, which makes the API call more succinct:

```python
client = boto3.client('cloudformation')
paginator = client.get_paginator("list_stack_instances")
for response in paginator.paginate(StackSetName='test-stack'):
    for stack_instances in response["Summaries"]:
        print(stack_instances)
```
