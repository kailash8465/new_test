import requests
import json
import os

api_token = os.environ.get('token')

def create_github_environment(repository, environment_name):
    api_url = f"https://api.github.com/repos/{repository}/environments"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {api_token}"
    }
    payload = {
        "name": environment_name,
        "auto_merge": False,
        "short_name": environment_name[:20],
        "production": False
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Environment created successfully!")
    else:
        print("Failed to create environment. Error:", response.text)

# Example usage
repository = "kailash8465/final_test"
environment_name = "my-new-environment"

create_github_environment(repository, environment_name)
