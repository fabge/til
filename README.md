Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [Lambda logging](aws/lambda-logging.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [CloudTrail](aws/cloudtrail.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [Useful `aws` snippets](aws/aws-snippets.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)

## azure

* [Azure portal tenant url](azure/azure-portal-url.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [Entra ID](azure/permissions.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [az-104](azure/az-104.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Enterprise application](azure/enterprise-application.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [az login](azure/azure-login.md)
* [Azure functions](azure/azure-functions.md)

## azure-devops

* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)
* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)

## bash

* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)
* [nvim](bash/nvim.md)
* [Replace variables](bash/replace-variables.md)
* [Tmux](bash/tmux.md)
* [Bash snippets](bash/bash-snippets.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Vim](bash/vim.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)

## browser

* [Take screenshots right from the browser](browser/screenshots.md)
* [Make a website fully editable with document.designMode](browser/document-design-mode.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [Border around every element using CSS selector](css/border.md)
* [How to center](css/center.md)

## deno

* [Deno Jupyter](deno/jupyter.md)

## django

* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django tests](django/tests.md)
* [Django forms](django/forms.md)
* [Django User](django/user.md)
* [Django models](django/models.md)
* [Django urls](django/urls.md)
* [Django queries](django/queries.md)
* [Django general](django/general.md)
* [Django admin](django/admin.md)
* [Django apps](django/apps.md)

## git

* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Write proper commit messages](git/commit-messages.md)
* [Rename branch](git/rename-branch.md)
* [Revert commit](git/revert-commit.md)
* [safer alternative to git push --force](git/push-force.md)
* [Reference commits using the commit message](git/reference-by-commit-message.md)

## github

* [Download latest release](github/download-latest-release.md)
* [Skip CI](github/skip-ci.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Debug GitHub Actions](github/debug-github-actions.md)

## html

* [Non-breaking space](html/non-breaking-space.md)
* [full height](html/full-height.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Subsetting/slicing lists](javascript/list-subset.md)
* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
* [Run async function on top level](javascript/async-top-level.md)
* [Print current year](javascript/print-current-year.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## linux

* [Get sizes of folder in current directory](linux/folder-sizes.md)

## llm

* [Summarize websites](llm/summarize-websites.md)
* [Pipe code and let explain](llm/pipe-code.md)
* [Prompt engineering](llm/prompt-engineering.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [Idempotence](misc/idempotence.md)
* [Database Fields](misc/database-fields.md)

## programming

* [Exceptions](programming/exceptions.md)
* [Comments](programming/comments.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Monkey Patching](python/monkey-patching.md)
* [Walrus Operator](python/walrus-operator.md)
* [Modules and Packages](python/modules-and-packages.md)
* [async](python/async.md)
* [Align string output with f-strings](python/align-string-output.md)
* [Functions](python/functions.md)
* [Install different Python versions](python/install-python-versions.md)
* [Python debugger](python/debugger.md)
* [Using `lambda`](python/lambda.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [Jupyter notebook commands](python/jupyter.md)
* [defaultdict](python/defaultdict.md)
* [Pandas](python/pandas.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [Using `repr`](python/repr.md)
* [Generators](python/generators.md)
* [pdb interact command](python/pdb-interact.md)
* [nbdev](python/nbdev.md)
* [pip install while developing](python/pip-install.md)
* [Scope of variables](python/variables.md)
* [Datetime formats](python/datetime-formats.md)
* [Python miscellanea](python/misc.md)

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

* [VS Code workspace settings](vscode/workspace-settings.md)
* [VS Code shortcuts](vscode/shortcuts.md)

## zsh

* [zsh goodies](zsh/shortcuts.md)

