import os
import requests
repo_owner = "kailash8465"
repo_name = "final_test"
api_token = os.environ.get('token')

def create_environment_with_reviewers(ENVIRONMENT_NAME):
    url = "https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {api_token}",
#         "X-GitHub-Api-Version": "2022-11-28"
    }
    
    data = {
#         "wait_timer": 30,
        "reviewers": [
            {"type": "User", "id": 60359651},
#             {"type": "Team", "id": 1}
        ],
#         "deployment_branch_policy": {
#             "protected_branches": False,
#             "custom_branch_policies": True
#         }
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Environment created successfully.")
    else:
        print(f"Failed to create environment. Status code: {response.status_code}")
        print(response.json())

create_environment_with_reviewers('stg-deploy')
