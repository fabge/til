Things I've learned, collected in [fabge/til](https://github.com/fabge/til).

## aws

* [Lambda logging](aws/lambda-logging.md)
* [Useful `aws` snippets](aws/aws-snippets.md)
* [AWS SigV4 using `curl`](aws/aws-sigv4.md)
* [Search CloudWatch logs](aws/search-cloudwatch-logs.md)
* [Display EC2 instance costs per month](aws/instance-costs-per-month.md)
* [Step Function Monitoring](aws/step-function-monitoring.md)
* [CloudTrail](aws/cloudtrail.md)
* [DynamoDB table scan](aws/dynamo-scan.md)
* [Reference AWS account](aws/reference-aws-account.md)
* [DynamoDB Global Secondary Indexes](aws/dynamo-global-secondary-indexes.md)
* [CloudFormation default values](aws/cloudformation-default-value.md)
* [Have pretty URLs when using S3 and CloudFront](aws/s3-cloudfront-pretty-urls.md)
* [Access AWS resources from Azure without credentials](aws/cross-cloud-access.md)
* [Assume a role across AWS accounts](aws/assume-cross-account-role.md)
* [Pagination using AWS boto3](aws/pagination.md)

## azure

* [Find permissions in RBAC roles easily](azure/permissions-in-rbac-roles.md)
* [Restrict your Microsoft Entra app to a set of users in a Microsoft Entra tenant](azure/restrict-user-access.md)
* [az-104](azure/az-104.md)
* [Azure functions](azure/azure-functions.md)
* [Invoke the Azure API via HTTP endpoints](azure/rest-api.md)
* [Entra ID](azure/permissions.md)
* [Databricks authentication with Azure](azure/databricks.md)
* [Enterprise application](azure/enterprise-application.md)
* [Azure portal tenant url](azure/azure-portal-url.md)
* [Set up Databricks via Bicep](azure/databricks-iac.md)
* [Find Azure Tenant Id by Subscription Id](azure/azure-tenant-id.md)
* [az login](azure/azure-login.md)

## azure-devops

* [Remove Azure DevOps Retention Leases](azure-devops/remove-retention-leases.md)
* [Contribute from a pipeline](azure-devops/contribute-from-pipeline.md)
* [Change workingDirectory for AWSShellScript](azure-devops/change-working-directory-aws-shell-script.md)

## bash

* [Vim](bash/vim.md)
* [Tmux](bash/tmux.md)
* [Modern PATH environment variable](bash/PATH.md)
* [nvim](bash/nvim.md)
* [`set -euo pipefail`](bash/set-euo-pipefail.md)
* [Replace variables](bash/replace-variables.md)
* [Do some action when changing directory (cd)](bash/change-directory-actions.md)
* [Escaping strings in Bash using `!:q`](bash/escape-string.md)
* [Bash snippets](bash/bash-snippets.md)
* [Run bash script in specific directory](bash/cd-and-run-in-directory.md)

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

* [Django apps](django/apps.md)
* [Django admin](django/admin.md)
* [Django forms](django/forms.md)
* [Django models](django/models.md)
* [Django queries](django/queries.md)
* [Django general](django/general.md)
* [Django tests](django/tests.md)
* [Safely Pass Data to JavaScript in a Django Template](django/safely-pass-data-to-javascript-in-a-django-template.md)
* [Django urls](django/urls.md)
* [Django User](django/user.md)

## git

* [Revert commit](git/revert-commit.md)
* [fatal: Need to specify how to reconcile divergent branches](git/reconcile-divergent-branches.md)
* [Rename branch](git/rename-branch.md)
* [Using Multiple SSH Keys](git/multiple-ssh-keys.md)
* [safer alternative to git push --force](git/push-force.md)
* [Squash/rebase commits](git/squash-rebase-commits.md)
* [Reference commits using the commit message](git/reference-by-commit-message.md)
* [Write proper commit messages](git/commit-messages.md)

## github

* [Debug GitHub Actions](github/debug-github-actions.md)
* [Download latest release](github/download-latest-release.md)
* [Commit a file if it changed](github/commit-if-file-changed.md)
* [Skip CI](github/skip-ci.md)

## html

* [full height](html/full-height.md)
* [Non-breaking space](html/non-breaking-space.md)

## htmx

* [Loading button](htmx/loading-button.md)

## img

* [Shrink/reduce/compress image sizes](img/shrink-images.md)

## javascript

* [Subsetting/slicing lists](javascript/list-subset.md)
* [Run async function on top level](javascript/async-top-level.md)
* [Print current year](javascript/print-current-year.md)
* [Pythonic Javascript](javascript/pythonic-javascript.md)
* [Write Javascript/Node in a notebook](javascript/javascript-in-notebook.md)

## json

* [Pretty-print JSON blobs](json/pretty-print-json.md)

## linux

* [Get sizes of folder in current directory](linux/folder-sizes.md)

## llm

* [Prompt engineering](llm/prompt-engineering.md)
* [Summarize websites](llm/summarize-websites.md)
* [Pipe code and let explain](llm/pipe-code.md)

## macos

* [MacOS shortcuts](macos/shortcuts.md)

## misc

* [Idempotence](misc/idempotence.md)
* [Exceptions](misc/exceptions.md)
* [Comments](misc/comments.md)
* [Greppability](misc/greppability.md)
* [loops and variable names](misc/loops.md)
* [Database Fields](misc/database-fields.md)
* [XY Problem](misc/x-y-problem.md)

## pytest

* [How to cheat at unit tests](pytest/cheating-at-unit-tests.md)

## python

* [Parallel HTTP requests in Python](python/parallel-http-requests.md)
* [Walrus Operator](python/walrus-operator.md)
* [Using `lambda`](python/lambda.md)
* [Jupyter notebook commands](python/jupyter.md)
* [Functions](python/functions.md)
* [Using `repr`](python/repr.md)
* [Scope of variables](python/variables.md)
* [Python debugger](python/debugger.md)
* [Pandas](python/pandas.md)
* [async](python/async.md)
* [Python miscellanea](python/misc.md)
* [defaultdict](python/defaultdict.md)
* [Datetime formats](python/datetime-formats.md)
* [Generators](python/generators.md)
* [Virtual environment setup](python/virtual-environment-setup.md)
* [Monkey Patching](python/monkey-patching.md)
* [uv - single file scripts](python/uv-single-file-scripts.md)
* [Install different Python versions](python/install-python-versions.md)
* [nbdev](python/nbdev.md)
* [pip install while developing](python/pip-install.md)
* [Align string output with f-strings](python/align-string-output.md)
* [Modules and Packages](python/modules-and-packages.md)
* [pdb interact command](python/pdb-interact.md)

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

