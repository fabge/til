# Using Multiple SSH Keys

I have a single computer and different GitHub accounts. I cannot use the same SSH key twice, which means I have to create a new SSH key for each GitHub account.

1. Create a new SSH key. Use your respective **GitHub email adress**.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. Add the public SSH key to your GitHub account: `Settings` -> `SSH and GPG keys` -> `New SSH key`

3. Configure your SSH config (`~/.ssh/config`).

```text
Host gh_work
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519_work

Host gh_personal
    HostName github.com
    IdentityFile ~/.ssh/id_ed25519_personal
```

4. **Clone repository using a specific ssh key**. This is the important part - clone your repository with a specific GitHub user:

```bash
git clone git@gh_work:foo/bar.git
```

If you have an existing repository, change the remote url.

```bash
git remote set-url origin git@gh_work:foo/bar.git
```
