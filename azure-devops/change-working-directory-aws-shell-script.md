# Change workingDirectory for AWSShellScript

It is straightforward to change the working Directory for regular shell scripts:

```yaml
    - script: |
        pwd
    workingDirectory: new-dir
```

For the AWSShellScript task however, you have to add an additional parameter `disableAutoCwd`:

```yaml
    - task: AmazonWebServices.aws-vsts-tools.AWSShellScript.AWSShellScript@1
    inputs:
        awsCredentials: your-service-connection
        regionName: eu-central-1
        scriptType: inline
        workingDirectory: technical-user-sync
        disableAutoCwd: true
        inlineScript: |
            pwd
```
