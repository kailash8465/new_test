import requests
import os
def create_branch(access_token, owner, repo_name, base_branch, new_branch):
    branch_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/refs"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "ref": f"refs/heads/{new_branch}",
        "sha": f"refs/heads/{base_branch}"
    }
    response = requests.post(branch_url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"Branch '{new_branch}' created successfully!")
    else:
        print(f"Failed to create branch '{new_branch}'")
        print(f"Response: {response.status_code} - {response.text}")


# Replace YOUR_PAT with your personal access token
access_token = os.environ.get('token')

 
# Replace OWNER and REPO_NAME with your repository details
owner = "kailash8465"
repo_name = "final_test"

# Create the feature/devops branch from the develop branch
base_branch = "develop"
new_branch = "feature/devops"
create_branch(access_token, owner, repo_name, base_branch, new_branch)

 
# Create the feature/master-devops branch from the master branch
base_branch = "main"
new_branch = "feature/master"
create_branch(access_token, owner, repo_name, base_branch, new_branch)
