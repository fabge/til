# Entra ID

## App permissions vs Delegated permissions

When you register an application in Azure AD, you need to define what permissions your application needs to access. There are two types of permissions: app permissions and delegated permissions.

### App permissions

App permissions are used when the application accesses resources on its own behalf. For example, an application that reads and writes data to a database. App permissions are also known as application permissions.

### Delegated permissions

Delegated permissions are used when the application accesses resources on behalf of a user. For example, an application that reads and writes data to a database on behalf of a user. Delegated permissions are also known as user permissions. These have to be consented by the user.
