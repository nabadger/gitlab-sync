# Gitlab Sync

This is a helper python program which downloads remote Gitlab repo(s) with support for group / sub-groups.

The program accepts a single top-level `group-id`, which it will use 
to traverse through the sub-groups to perform a`git [clone|pull]` command using ssh.

## Reqiures

* pipenv (for python)
* gitlab api token
* gitlab configured with ssh-key

## Install

```
pipenv install
```

## Run
```
pipenv run python src/gitlab-sync.py --help

usage: gitlab-sync.py [-h] [--group-id GROUP_ID]
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
pipenv run python src/gitlab-sync.py \
	--group-id <numeric-gitlab-group-id> \
	--local-repo-path /tmp/mycheckouts \
	--gitlab-token <gitlab-api-token> \
	--no-dry-run 

```
