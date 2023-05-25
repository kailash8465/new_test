import os
from github import Github

def enable_branch_protection(repo_owner, repo_name, branch_name, access_token):
    g = Github(access_token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    branch = repo.get_branch(branch_name)

    if branch_name == "develop":
        # Apply branch protection settings for "develop" branch
        branch.edit_protection(
            required_approving_review_count=1,
            dismiss_stale_reviews=True,
        )
    elif branch_name == "feature/devops-master":
        # Apply branch protection settings for "master" branch
        branch.edit_protection(
            required_approving_review_count=1,
            dismiss_stale_reviews=True,
            require_code_owner_reviews=True,
            restrictions={
#                 "users": [],
                "teams": ['procter-gamble/teams/c360-repo-admins']
#                 "apps": [],
#                 "users_url": [],
#                 "teams_url": [],
#                 "apps_url": [],
#                 "url": "https://api.github.com/orgs/procter-gamble/teams/c360-repo-admins"
            }
        )

# Example usage
repo_owner = "kailash8465"
repo_name = "final_test"
branch_name = "feature/devops-master"  # or "master"
github_access_token = os.environ.get('token')

enable_branch_protection(repo_owner, repo_name, branch_name, github_access_token)
