# Search CloudWatch logs

One way to search CloudWatch logs is to click on Log groups in the AWS Console, select a log group and use `ctrl` + `f` or use the search field to search for a string. This is not very efficient, especially if you have a lot of log groups.

Logs Insights allows you to search for a string across all log groups. You can also use the query language to search for more complex queries.

This query will search for all log groups that contain the string `time`, e.g. if you want to find out if there were Lambdas that timed out.

```text
fields @timestamp, @message
| filter @message like 'time'
| sort @timestamp desc
| limit 20
```
