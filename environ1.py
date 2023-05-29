import requests
import os
api_token = os.environ.get('token')

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {api_token}"
    "X-GitHub-Api-Version": "2022-11-28"
}

data = {
    "wait_timer": 30,
    "reviewers": [
        {"type": "User", "id": 60359651}
    ],
    "deployment_branch_policy": {
        "protected_branches": False,
        "custom_branch_policies": True
    }
}

url = "https://api.github.com/repos/kailash8465/final_test/environments/stg-deploy"

response = requests.put(url, headers=headers, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())
