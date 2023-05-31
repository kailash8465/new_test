import os
import requests

api_token = os.environ.get('token')
owner = 'kailash8465'

def create_private_repo_with_auto_init(repository_name):
    headers = {
        "Authorization": f"token {api_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "name": repository_name,
        "auto_init": True,
        "private": True
    }

    create_repo_url = f"https://api.github.com/user/{owner}/repos"
    response = requests.post(create_repo_url, headers=headers, json=data)

    if response.status_code == 201:
        print("New repository created successfully!")
    else:
        print("Failed to create repository:", response.json()["message"])

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
# Replace 'your-username' with the desired owner or organization name
# Replace 'your-repo-name' with the desired repository name

create_private_repo_with_auto_init('testing-repo')
