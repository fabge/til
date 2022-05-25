# `set -euo pipefail`

By default, bash will continue after errors.  
`set -e` stops the script on errors.

By default, unset variables don't error.  
`set -u` stops the script on unset variables.

By default, a command failing doesn't fail the whole pipeline.  
`set -o pipefail` prevents this.