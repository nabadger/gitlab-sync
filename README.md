# Gitlab Sync

This is a helper python program which downloads remote Gitlab repo(s) with support for group / sub-groups.

The program accepts a single top-level `group-id`, which it will use 
to traverse through the sub-groups to perform a`git [clone|pull]` command using ssh.

## Requires

* pipx for installation
* gitlab api token
* gitlab configured with ssh-key

## Install

Use `pipx` to install into `$HOME/.local/bin/gitlab-sync`

```
pipx install --spec git+https://github.com/nabadger/gitlab-sync.git gitlab-sync
```

To uninstall:

```
pipx uninstall gitlab-sync
```

## Run
```
gitlab-sync --help

usage: gitlab-sync [-h] [--group-id GROUP_ID]
                      [--local-repo-path LOCAL_REPO_PATH]
                      [--gitlab-token GITLAB_TOKEN] [--dry-run] [--no-dry-run]

optional arguments:
  -h, --help            show this help message and exit
  --group-id GROUP_ID   group id
  --local-repo-path LOCAL_REPO_PATH
                        local repo path (clone under this dir)
  --gitlab-token GITLAB_TOKEN
                        gitlab private token
  --dry-run             dry-run (do not do git commands)
  --no-dry-run          no-dry-run (do git commands)
```

## Example

```
gitlab-sync \
	--group-id <numeric-gitlab-group-id> \
	--local-repo-path /tmp/mycheckouts \
	--gitlab-token <gitlab-api-token> \
	--no-dry-run 

```
## Finding the Group Id on Gitlab

The Group ID can be found by navigating to the Group (or SubGroup) settings page
and expanding the General settings.
