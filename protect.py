import requests

def protect_github_branch(repo_owner, repo_name, branch_name, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.luke-cage-preview+json"  # Required for working with branch protection API
    }

    # Get branch protection settings
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/{branch_name}/protection", headers=headers)
    response.raise_for_status()
    branch_protection = response.json()

    # Update branch protection settings
    if branch_name == "develop":
        branch_protection["required_pull_request_reviews"] = {"dismiss_stale_reviews": True, "require_code_owner_reviews": True}
        branch_protection["required_status_checks"] = None
    else:
        branch_protection["required_pull_request_reviews"] = None
        branch_protection["required_status_checks"] = {"strict": True, "contexts": []}
    
    branch_protection["enforce_admins"] = False
    branch_protection["restrictions"] = None

    response = requests.put(f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/{branch_name}/protection", headers=headers, json=branch_protection)
    response.raise_for_status()

# Example usage
repo_owner = "kailash8465"
repo_name = "final_test"
branch_name = "develop"
github_access_token = os.environ.get('token')

protect_github_branch(repo_owner, repo_name, branch_name, github_access_token)
