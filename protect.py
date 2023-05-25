import os
from github import Github

def enable_branch_protection(repo_owner, repo_name, branch_name, access_token):
    g = Github(access_token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    branch = repo.get_branch(branch_name)
    branch.edit_protection(required_approving_review_count=1, dismiss_stale_reviews=True)

# Example usage
repo_owner = "kailash8465"
repo_name = "final_test"
branch_name = "develop"
github_access_token = os.environ.get('token')

enable_branch_protection(repo_owner, repo_name, branch_name, github_access_token)
