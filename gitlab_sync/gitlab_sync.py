"""
This is a helper script to git clone/pull gitlab-projects which
are in the specified group (includes all children).
"""
import gitlab
import os
import sys
import argparse
from git import Repo
from colorama import Fore, Style


def clone_projects(local_repo_path, projects, dry_run):
    """
    Clone/pull all projects in the group
    """

    for project in projects:
        local_repo_fullpath = os.path.join(
            local_repo_path, project.path_with_namespace)
        if os.path.exists(local_repo_fullpath):
            os.chdir(local_repo_fullpath)
            print(f'\t{Fore.CYAN}Pulling{Style.RESET_ALL}: %s' %
                  (local_repo_fullpath))
            if dry_run:
                print(f'\t\t{Fore.YELLOW}Skipping (dry-run){Style.RESET_ALL}')
            else:
                repo = Repo(local_repo_fullpath)
                o = repo.remotes.origin
                o.pull()
        else:
            print(f'\t{Fore.GREEN}Cloning{Style.RESET_ALL}: %s' %
                  (local_repo_fullpath))
            if dry_run:
                print(f'\t\t{Fore.YELLOW}Skipping (dry-run){Style.RESET_ALL}')
            else:
                Repo.clone_from(project.ssh_url_to_repo, local_repo_fullpath)


def sync_gitlab_repos(gl, args):
    """
    Get all groups / subgroups which we should sync
    """

    def get_groups(group, group_name):
        print(f'Group {Fore.YELLOW}%s (id: %s){Style.RESET_ALL}' %
              (group_name, group.id))

        projects = group.projects.list()
        clone_projects(args.local_repo_path, projects, args.dry_run)

        subgroups = group.subgroups.list(all=True)
        for subgroup in subgroups:
            real_g = gl.groups.get(subgroup.id, lazy=True)
            get_groups(real_g, subgroup.name)

    top_group = gl.groups.get(args.group_id)
    get_groups(top_group, top_group.name)


def main():
    """
    Init settings and start
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--group-id", help="group id", required=True),
    parser.add_argument("--local-repo-path",
                        help="local repo path (clone under this dir)",
                        required=True)
    parser.add_argument("--gitlab-token", help="gitlab private token",
                        default=os.environ.get('GITLAB_PRIVATE_TOKEN'))
    parser.add_argument("--dry-run", dest="dry_run",
                        action='store_true', default=True,
                        help="dry-run (do not do git commands)")
    parser.add_argument("--no-dry-run", dest="dry_run",
                        action='store_false', default=False,
                        help="no-dry-run (do git commands)")

    args = parser.parse_args()
    
    # Grab gitlab token from environment and exit if not set
    if not args.gitlab_token:
        parser.print_help(sys.stderr)
        print("gitlab-token not set via GITLAB_PRIVATE_TOKEN or --gitlab-token")
        sys.exit(1)

    gl = gitlab.Gitlab('https://gitlab.com',
                       private_token=args.gitlab_token)
    gl.auth()

    sync_gitlab_repos(gl, args)


if __name__ == '__main__':
    main()
