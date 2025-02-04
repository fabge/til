Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [Lambda logging](aws/lambda-logging.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [CloudTrail](aws/cloudtrail.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Pagination using AWS boto3](aws/pagination.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [Useful `aws` snippets](aws/aws-snippets.md)

## azure

* [Set up Databricks via Bicep](azure/databricks-iac.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [Enterprise application](azure/enterprise-application.md)
* [Azure portal tenant url](azure/azure-portal-url.md)
* [az login](azure/azure-login.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Azure functions](azure/azure-functions.md)
* [Entra ID](azure/permissions.md)
* [az-104](azure/az-104.md)

## azure-devops

* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)
* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)

## bash

* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [nvim](bash/nvim.md)
* [Tmux](bash/tmux.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Modern PATH environment variable](bash/PATH.md)
* [Replace variables](bash/replace-variables.md)
* [Bash snippets](bash/bash-snippets.md)
* [Vim](bash/vim.md)

## browser

* [Make a website fully editable with document.designMode](browser/document-design-mode.md)
* [Take screenshots right from the browser](browser/screenshots.md)

## cloudflare

* [ERR_TOO_MANY_REDIRECTS](cloudflare/err_too_many_redirects.md)

## css

* [Border around every element using CSS selector](css/border.md)
* [How to center](css/center.md)

## deno

* [Deno Jupyter](deno/jupyter.md)

## django

* [Django forms](django/forms.md)
* [Django general](django/general.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django urls](django/urls.md)
* [Django admin](django/admin.md)
* [Django models](django/models.md)
* [Django User](django/user.md)
* [Django tests](django/tests.md)
* [Django apps](django/apps.md)
* [Django queries](django/queries.md)

## git

* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [Rename branch](git/rename-branch.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Write proper commit messages](git/commit-messages.md)
* [safer alternative to git push --force](git/push-force.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Revert commit](git/revert-commit.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)

## github

* [Skip CI](github/skip-ci.md)
* [Debug GitHub Actions](github/debug-github-actions.md)
* [Download latest release](github/download-latest-release.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)

## html

* [Non-breaking space](html/non-breaking-space.md)
* [full height](html/full-height.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Subsetting/slicing lists](javascript/list-subset.md)
* [Run async function on top level](javascript/async-top-level.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)
* [Print current year](javascript/print-current-year.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## linux

* [Get sizes of folder in current directory](linux/folder-sizes.md)

## llm

* [Prompt engineering](llm/prompt-engineering.md)
* [Pipe code and let explain](llm/pipe-code.md)
* [Summarize websites](llm/summarize-websites.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [Database Fields](misc/database-fields.md)
* [Idempotence](misc/idempotence.md)
* [Exceptions](misc/exceptions.md)
* [XY Problem](misc/x-y-problem.md)
* [Greppability](misc/greppability.md)
* [Comments](misc/comments.md)
* [loops and variable names](misc/loops.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Jupyter notebook commands](python/jupyter.md)
* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [Install different Python versions](python/install-python-versions.md)
* [Datetime formats](python/datetime-formats.md)
* [Using `lambda`](python/lambda.md)
* [defaultdict](python/defaultdict.md)
* [nbdev](python/nbdev.md)
* [uv - single file scripts](python/uv-single-file-scripts.md)
* [Pandas](python/pandas.md)
* [Functions](python/functions.md)
* [Generators](python/generators.md)
* [Align string output with f-strings](python/align-string-output.md)
* [Scope of variables](python/variables.md)
* [Python miscellanea](python/misc.md)
* [Walrus Operator](python/walrus-operator.md)
* [Monkey Patching](python/monkey-patching.md)
* [Using `repr`](python/repr.md)
* [pdb interact command](python/pdb-interact.md)
* [async](python/async.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [pip install while developing](python/pip-install.md)
* [Modules and Packages](python/modules-and-packages.md)
* [Python debugger](python/debugger.md)

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

