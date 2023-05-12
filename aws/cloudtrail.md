# CloudTrail

Sometimes API calls which are expected to be found in CloudTrail are missing.  
Most of the time the reason is that the API call was made in a different region, e.g. all IAM actions are logged in `us-east-1` regardless of the region the action was performed in.
