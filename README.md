Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [CloudTrail](aws/cloudtrail.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [Update DynamoDB item](aws/dynamo-update-item.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Lambda logging](aws/lambda-logging.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)

## azure

* [Azure functions](azure/azure-functions.md)
* [az login](azure/azure-login.md)
* [Azure portal tenant url](azure/azure-portal-url.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [Set up Databricks via Bicep](azure/databricks-iac.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Enterprise application](azure/enterprise-application.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [Entra ID](azure/permissions.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)

## azure-devops

* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)
* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)

## bash

* [Modern PATH environment variable](bash/PATH.md)
* [Bash snippets](bash/bash-snippets.md)
* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [nvim](bash/nvim.md)
* [Replace variables](bash/replace-variables.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)
* [Tmux](bash/tmux.md)
* [Vim](bash/vim.md)

## browser

* [Make a website fully editable with document.designMode](browser/document-design-mode.md)
* [Take screenshots right from the browser](browser/screenshots.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [Border around every element using CSS selector](css/border.md)
* [How to center](css/center.md)

## django

* [Django admin](django/admin.md)
* [Django apps](django/apps.md)
* [Django forms](django/forms.md)
* [Django general](django/general.md)
* [Django models](django/models.md)
* [Django queries](django/queries.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django tests](django/tests.md)
* [Django urls](django/urls.md)
* [Django User](django/user.md)

## git

* [Write proper commit messages](git/commit-messages.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [safer alternative to git push --force](git/push-force.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [Rename branch](git/rename-branch.md)
* [Revert commit](git/revert-commit.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)

## github

* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Debug GitHub Actions](github/debug-github-actions.md)
* [Download latest release](github/download-latest-release.md)
* [Github pages](github/github-pages.md)
* [Skip CI](github/skip-ci.md)

## html

* [full height](html/full-height.md)
* [Non-breaking space](html/non-breaking-space.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Run async function on top level](javascript/async-top-level.md)
* [Deno Jupyter](javascript/jupyter.md)
* [Subsetting/slicing lists](javascript/list-subset.md)
* [Print current year](javascript/print-current-year.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## linux

* [Get sizes of folder in current directory](linux/folder-sizes.md)

## llm

* [Pipe code and let explain](llm/pipe-code.md)
* [Prompt engineering](llm/prompt-engineering.md)
* [Summarize websites](llm/summarize-websites.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [Comments](misc/comments.md)
* [Database Fields](misc/database-fields.md)
* [Exceptions](misc/exceptions.md)
* [Greppability](misc/greppability.md)
* [Idempotence](misc/idempotence.md)
* [improve http call speed](misc/improve-http-call-speed.md)
* [loops and variable names](misc/loops.md)
* [XY Problem](misc/x-y-problem.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Align string output with f-strings](python/align-string-output.md)
* [async](python/async.md)
* [Datetime formats](python/datetime-formats.md)
* [Python debugger](python/debugger.md)
* [defaultdict](python/defaultdict.md)
* [Functions](python/functions.md)
* [Generators](python/generators.md)
* [Jupyter notebook commands](python/jupyter.md)
* [Using `lambda`](python/lambda.md)
* [Python miscellanea](python/misc.md)
* [Modules and Packages](python/modules-and-packages.md)
* [Monkey Patching](python/monkey-patching.md)
* [nbdev](python/nbdev.md)
* [Pandas](python/pandas.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [pdb interact command](python/pdb-interact.md)
* [pip install while developing](python/pip-install.md)
* [Useful regex patterns](python/regex.md)
* [Using `repr`](python/repr.md)
* [uv - single file scripts](python/uv-single-file-scripts.md)
* [Scope of variables](python/variables.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [Walrus Operator](python/walrus-operator.md)

## sqlite

* [Setup](sqlite/setup.md)

## ssh

* [Setup SSH keys via ssh-copy-id](ssh/setup-ssh.md)

## terraform

* [Loop files](terraform/loop-files.md)

## ubuntu

* [Linux file system](ubuntu/linux-file-system.md)

## vscode

* [VS Code shortcuts](vscode/shortcuts.md)
* [VS Code workspace settings](vscode/workspace-settings.md)

## zsh

* [zsh goodies](zsh/shortcuts.md)

