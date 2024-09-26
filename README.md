Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [CloudFormation default values](aws/cloudformation-default-value.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [Useful `aws` snippets](aws/aws-snippets.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [CloudTrail](aws/cloudtrail.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Lambda logging](aws/lambda-logging.md)

## azure

* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Entra ID](azure/permissions.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [az login](azure/azure-login.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [Azure functions](azure/azure-functions.md)
* [Azure portal tenant url](azure/azure-portal-url.md)
* [az-104](azure/az-104.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Enterprise application](azure/enterprise-application.md)

## azure-devops

* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)
* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)

## bash

* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Vim](bash/vim.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)
* [Replace variables](bash/replace-variables.md)
* [Bash snippets](bash/bash-snippets.md)
* [Tmux](bash/tmux.md)
* [nvim](bash/nvim.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)

## browser

* [Make a website fully editable with document.designMode](browser/document-design-mode.md)
* [Take screenshots right from the browser](browser/screenshots.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [How to center](css/center.md)
* [Border around every element using CSS selector](css/border.md)

## django

* [Django queries](django/queries.md)
* [Django general](django/general.md)
* [Django User](django/user.md)
* [Django tests](django/tests.md)
* [Django models](django/models.md)
* [Django urls](django/urls.md)
* [Django forms](django/forms.md)
* [Django apps](django/apps.md)
* [Django admin](django/admin.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)

## git

* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [Revert commit](git/revert-commit.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [Rename branch](git/rename-branch.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Write proper commit messages](git/commit-messages.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [safer alternative to git push --force](git/push-force.md)

## github

* [Download latest release](github/download-latest-release.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Debug GitHub Actions](github/debug-github-actions.md)
* [Skip CI](github/skip-ci.md)

## html

* [Non-breaking space](html/non-breaking-space.md)
* [full height](html/full-height.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Run async function on top level](javascript/async-top-level.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
* [Print current year](javascript/print-current-year.md)
* [Subsetting/slicing lists](javascript/list-subset.md)
* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## llm

* [Pipe code and let explain](llm/pipe-code.md)
* [Prompt engineering](llm/prompt-engineering.md)
* [Summarize websites](llm/summarize-websites.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [Idempotence](misc/idempotence.md)

## programming

* [Comments](programming/comments.md)
* [Exceptions](programming/exceptions.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Using `lambda`](python/lambda.md)
* [Align string output with f-strings](python/align-string-output.md)
* [pdb interact command](python/pdb-interact.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [Datetime formats](python/datetime-formats.md)
* [Monkey Patching](python/monkey-patching.md)
* [async](python/async.md)
* [Python debugger](python/debugger.md)
* [Install different Python versions](python/install-python-versions.md)
* [defaultdict](python/defaultdict.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [pip install while developing](python/pip-install.md)
* [Jupyter notebook commands](python/jupyter.md)
* [Pandas](python/pandas.md)
* [Modules and Packages](python/modules-and-packages.md)
* [Generators](python/generators.md)
* [Functions](python/functions.md)
* [Python miscellanea](python/misc.md)
* [nbdev](python/nbdev.md)
* [Walrus Operator](python/walrus-operator.md)
* [Using `repr`](python/repr.md)
* [Scope of variables](python/variables.md)

## regex

* [Useful regex patterns](regex/basics.md)

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

