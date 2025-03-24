Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [Useful `aws` snippets](aws/aws-snippets.md)
* [CloudTrail](aws/cloudtrail.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Lambda logging](aws/lambda-logging.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)

## azure

* [Entra ID](azure/permissions.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [az login](azure/azure-login.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Set up Databricks via Bicep](azure/databricks-iac.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [az-104](azure/az-104.md)
* [Enterprise application](azure/enterprise-application.md)
* [Azure portal tenant url](azure/azure-portal-url.md)
* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Azure functions](azure/azure-functions.md)

## azure-devops

* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)
* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)

## bash

* [Replace variables](bash/replace-variables.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Tmux](bash/tmux.md)
* [nvim](bash/nvim.md)
* [Vim](bash/vim.md)
* [Bash snippets](bash/bash-snippets.md)
* [Modern PATH environment variable](bash/PATH.md)
* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)

## browser

* [Make a website fully editable with document.designMode](browser/document-design-mode.md)
* [Take screenshots right from the browser](browser/screenshots.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [How to center](css/center.md)
* [Border around every element using CSS selector](css/border.md)

## deno

* [Deno Jupyter](deno/jupyter.md)

## django

* [Django forms](django/forms.md)
* [Django User](django/user.md)
* [Django apps](django/apps.md)
* [Django queries](django/queries.md)
* [Django general](django/general.md)
* [Django models](django/models.md)
* [Django tests](django/tests.md)
* [Django urls](django/urls.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django admin](django/admin.md)

## git

* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Write proper commit messages](git/commit-messages.md)
* [safer alternative to git push --force](git/push-force.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Revert commit](git/revert-commit.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [Rename branch](git/rename-branch.md)

## github

* [Skip CI](github/skip-ci.md)
* [Debug GitHub Actions](github/debug-github-actions.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Download latest release](github/download-latest-release.md)

## html

* [Non-breaking space](html/non-breaking-space.md)
* [full height](html/full-height.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)
* [Run async function on top level](javascript/async-top-level.md)
* [Print current year](javascript/print-current-year.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
* [Subsetting/slicing lists](javascript/list-subset.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## linux

* [Get sizes of folder in current directory](linux/folder-sizes.md)

## llm

* [Summarize websites](llm/summarize-websites.md)
* [Prompt engineering](llm/prompt-engineering.md)
* [Pipe code and let explain](llm/pipe-code.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [XY Problem](misc/x-y-problem.md)
* [Idempotence](misc/idempotence.md)
* [Greppability](misc/greppability.md)
* [Exceptions](misc/exceptions.md)
* [Comments](misc/comments.md)
* [loops and variable names](misc/loops.md)
* [Database Fields](misc/database-fields.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Install different Python versions](python/install-python-versions.md)
* [uv - single file scripts](python/uv-single-file-scripts.md)
* [Walrus Operator](python/walrus-operator.md)
* [Python miscellanea](python/misc.md)
* [Align string output with f-strings](python/align-string-output.md)
* [Modules and Packages](python/modules-and-packages.md)
* [Datetime formats](python/datetime-formats.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [Generators](python/generators.md)
* [Functions](python/functions.md)
* [defaultdict](python/defaultdict.md)
* [Using `repr`](python/repr.md)
* [Monkey Patching](python/monkey-patching.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [pip install while developing](python/pip-install.md)
* [Pandas](python/pandas.md)
* [pdb interact command](python/pdb-interact.md)
* [nbdev](python/nbdev.md)
* [async](python/async.md)
* [Useful regex patterns](python/regex.md)
* [Jupyter notebook commands](python/jupyter.md)
* [Scope of variables](python/variables.md)
* [Python debugger](python/debugger.md)
* [Using `lambda`](python/lambda.md)

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

