import os
import requests
repo_owner = "kailash8465"
repo_name = "final_test"
api_token = os.environ.get('token')
def create_environment_with_reviewers(environment):
    # Define the API endpoint for creating an environment
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/environments"

    # Set up the required headers including authentication
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {api_token}"
    }

    # Set up the required data for creating the environment
    data = {
        "name": environment,
        "required reviewers": [
            "c360-admins",
        ]
    }

    # Send a POST request to create the environment
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 201:
        print("Environment created successfully.")
    else:
        print(f"Failed to create environment. Status code: {response.status_code}")
        print(response.json())
create_environment_with_reviewers('stg-repo-deploy')
