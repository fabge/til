# Step Function Monitoring

I recently found a neat way to monitor **all** Step Function in an AWS account with minimal overhead.

Usually every AWS Step Function is deployed with a matching Cloudwatch Alarm, which is triggered when the Step Function fails.

```yaml
ResourceComplianceMachineExecutionsFailed:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmDescription: !Sub |
      Checks whether the ${AWS::StackName} state machine fails.
    AlarmActions:
      - !Sub "arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${AlarmTopicName}"
    ComparisonOperator: GreaterThanOrEqualToThreshold
    EvaluationPeriods: 1
    MetricName: ExecutionsFailed
    Namespace: AWS/States
    Period: 300
    Statistic: Sum
    Threshold: 1
    TreatMissingData: missing
    Unit: Count
    Dimensions:
      - Name: StateMachineArn
        Value: !Ref YourStateMachine
```

This is a good start, but it has a few drawbacks:

* It only monitors a single Step Function
* It only monitors the number of failed executions
* It aggregates the number of failed executions over a period of time, resulting in a lagging notification

There is a better way to monitor all Step Functions in an AWS account.  
We can use an AWS EventBridge Rule to monitor specific State Changes of AWS Step Functions.
This EventBridge Rule triggers a Lambda function, which can e.g. parse the error message and include a link to the Step Function execution. This uses the AWS SAM framework.

```yaml
  StepFunctionEventParserFunction:
    Type: AWS::Serverless::Function
    Properties:
      Description: Event Parsing Lambda for Step Function Errors, sends parsed error message to SNS topic when a Step Function fails or times out.
      CodeUri: src/notification/
      Handler: step_function_event_parser.handler
      Runtime: python3.8
      Environment:
        Variables:
          SNS_ARN: !Ref AlarmTopic
      Events:
        Trigger:
          Type: EventBridgeRule
          Properties:
            Pattern:
              source:
                - aws.states
              detail-type:
                - Step Functions Execution Status Change
              detail:
                status:
                  - FAILED
                  - TIMED_OUT
```
