Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [Useful `aws` snippets](aws/aws-snippets.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [CloudTrail](aws/cloudtrail.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [Lambda logging](aws/lambda-logging.md)

## azure

* [Azure portal tenant url](azure/azure-portal-url.md)
* [Entra ID](azure/permissions.md)
* [Enterprise application](azure/enterprise-application.md)
* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Azure functions](azure/azure-functions.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [az login](azure/azure-login.md)
* [az-104](azure/az-104.md)

## azure-devops

* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)
* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)

## bash

* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [Replace variables](bash/replace-variables.md)
* [nvim](bash/nvim.md)
* [Bash snippets](bash/bash-snippets.md)
* [Vim](bash/vim.md)
* [Tmux](bash/tmux.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)

## browser

* [Take screenshots right from the browser](browser/screenshots.md)
* [Make a website fully editable with document.designMode](browser/document-design-mode.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [How to center](css/center.md)
* [Border around every element using CSS selector](css/border.md)

## deno

* [Deno Jupyter](deno/jupyter.md)

## django

* [Django tests](django/tests.md)
* [Django admin](django/admin.md)
* [Django queries](django/queries.md)
* [Django general](django/general.md)
* [Django User](django/user.md)
* [Django models](django/models.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django forms](django/forms.md)
* [Django apps](django/apps.md)
* [Django urls](django/urls.md)

## git

* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Write proper commit messages](git/commit-messages.md)
* [safer alternative to git push --force](git/push-force.md)
* [Rename branch](git/rename-branch.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [Revert commit](git/revert-commit.md)

## github

* [Download latest release](github/download-latest-release.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Debug GitHub Actions](github/debug-github-actions.md)
* [Skip CI](github/skip-ci.md)

## html

* [full height](html/full-height.md)
* [Non-breaking space](html/non-breaking-space.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)
* [Run async function on top level](javascript/async-top-level.md)
* [Subsetting/slicing lists](javascript/list-subset.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
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
* [Greppability](misc/greppability.md)

## programming

* [Comments](programming/comments.md)
* [Exceptions](programming/exceptions.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [uv - single file scripts](python/uv-single-file-scripts.md)
* [Align string output with f-strings](python/align-string-output.md)
* [Generators](python/generators.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [async](python/async.md)
* [Monkey Patching](python/monkey-patching.md)
* [Using `lambda`](python/lambda.md)
* [Walrus Operator](python/walrus-operator.md)
* [Datetime formats](python/datetime-formats.md)
* [defaultdict](python/defaultdict.md)
* [Modules and Packages](python/modules-and-packages.md)
* [Install different Python versions](python/install-python-versions.md)
* [Python miscellanea](python/misc.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [Python debugger](python/debugger.md)
* [pdb interact command](python/pdb-interact.md)
* [nbdev](python/nbdev.md)
* [Scope of variables](python/variables.md)
* [Functions](python/functions.md)
* [pip install while developing](python/pip-install.md)
* [Jupyter notebook commands](python/jupyter.md)
* [Pandas](python/pandas.md)
* [Using `repr`](python/repr.md)

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

