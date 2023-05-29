import requests
import os
api_token = os.environ.get('token')
def create_github_environment(repository, environment_name):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {api_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    data = {
#         "wait_timer": 30,
        "reviewers": [
            {"type": "User", "id": 60359651}
#             {"type": "Team", "id": 1}
        ]
#         "deployment_branch_policy": {
#             "protected_branches": False,
#             "custom_branch_policies": True
#         }
    }

    url = f"https://api.github.com/repos/{repository}/environments/{environment_name}"

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Environment created/updated successfully!")
    else:
        print("Failed to create/update environment. Error:", response.text)

# Example usage
repository = "kailash8465/final_test"
environment_name = ['stg-deploy','prod_deploy']

for i in environment_name:
    create_github_environment(repository, i)

