# gcp basics

## commands

## authentication

```bash
# for cli usage
gcloud auth login

# for sdk/library usage (e.g. python google-cloud or terraform/tofu)
gcloud auth application-default login
```

### config

set project

```bash
# for cli usage
gcloud config set project my-project-id

# for sdk/library usage (e.g. python google-cloud or terraform/tofu)
gcloud auth application-default set-quota-project my-project-id

# verify
gcloud config get-value project

cat ~/.config/gcloud/application_default_credentials.json
```

### storage

list buckets

```bash
gsutil ls
# or newer, unified version
gcloud storage ls
```

### iam

```bash
# List all roles
gcloud iam roles list

# Describe a role
gcloud iam roles describe roles/storage.admin

# List predefined roles for a service
gcloud iam roles list --filter="name:roles/storage.*"
```

## concepts

### hierarchy

```text
Organization
  └─ Folder
      └─ Project
          └─ Resource (bucket, instance, etc.)
```

```bash
gcloud organizations ...
gcloud resource-manager folders ...
gcloud projects ...
gcloud <service> ... # e.g., compute, iam, storage ...
```

### iam

`WHO (Principal) + WHAT (Role) + WHERE (Resource)`

#### principals (WHO)

```bash
# User
user:fabian@enbw.com

# Service Account (like AWS IAM role + Azure Managed Identity)
serviceAccount:my-sa@project-id.iam.gserviceaccount.com

# Group
group:cloud-team@enbw.com

# Domain
domain:enbw.com

# All authenticated users
allAuthenticatedUsers

# Public
allUsers
```

user accounts vs service accounts

user accounts

- real people's identities
- live in cloud identity (similiar to entra id)
- used for interactive login
- format `user:fa.geiger@enbw.com``

service accounts

- non-human identities for applications/workloads
- live in gcp project
- not real email addresses (though they look like it)
- used for
    - applications running on GCP (VMs, Cloud Run, GKE)
    - applications running outside GCP (via keys or federation)
    - cross-project access
    - automation/CI-CD pipelines
- format `serviceAccount:my-app@PROJECT_ID.iam.gserviceaccount.com`

#### roles (WHAT)

1. Basic Roles (legacy, avoid in production)

    roles/viewer - Read-only access
    roles/editor - Read-write access
    roles/owner - Full control

2. Predefined Roles (use these!)

    roles/storage.admin - Full control of Cloud Storage
    roles/compute.instanceAdmin.v1 - Manage VM instances
    roles/iam.serviceAccountUser - Use service account

3. Custom Roles (for specific needs)

    Define your own permissions

#### resources (WHERE)

IAM policies can be set at multiple levels (inheritance flows down):

```text
Organization
  └─ Folder
      └─ Project
          └─ Resource (bucket, instance, etc.)
```

Service accounts are both:

- An identity (runs workloads)
- A resource (can be impersonated)

#### aws assume role analogy

```bash
# Grant permission for SA1 to impersonate SA2
gcloud iam service-accounts add-iam-policy-binding sa2@project-b.iam.gserviceaccount.com \
    --member="serviceAccount:sa1@project-a.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"

# Now workload using SA1 can impersonate SA2
gcloud storage ls --impersonate-service-account=sa2@project-b.iam.gserviceaccount.com
```

#### workload identitfy federation

e.g. external access to gcp

```bash
# Allow AWS IAM role to impersonate GCP service account
gcloud iam service-accounts add-iam-policy-binding my-app@PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/iam.workloadIdentityUser" \
    --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/arn:aws:sts::AWS_ACCOUNT:assumed-role/ROLE_NAME"
```
