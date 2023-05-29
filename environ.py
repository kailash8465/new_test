import os
import requests
repo_owner = "kailash8465"
repo_name = "final_test"
api_token = os.environ.get('token')

import requests

def create_environment_with_reviewers(ENVIRONMENT_NAME):
    url = "https://api.github.com/repos/OWNER/REPO/deployments/ENVIRONMENT_NAME/statuses"
#     api_token = "YOUR-TOKEN"
    user_id = 60359651  # Replace with the actual team ID

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {api_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    data = {
        "state": "pending",
#         "environment_url": "https://example.com",
        "required_reviewers": [
            {
                "type": "User",
                "id": user_id
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Environment created successfully.")
    else:
        print(f"Failed to create environment. Status code: {response.status_code}")
        print(response.json())

create_environment_with_reviewers('stg-deploy')

