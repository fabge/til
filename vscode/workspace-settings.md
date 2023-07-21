# Vscode workspace settings

## python.analysis.extraPaths

Sometimes there are packages which are correctly referenced in the deployed environment but not in the development environment. This can be solved by adding the path to the package to the `python.analysis.extraPaths` setting in the workspace settings.

```json
{
    "python.analysis.extraPaths": ["${workspaceFolder}/src/shared_library"],
}
```
