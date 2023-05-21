import requests
import json
import os
import base64

# GitHub access token with appropriate permissions
access_token = os.environ.get('token')

# Source and destination repositories information
source_owner = 'kailash8465'
source_repo = 'devops-essentials-sample-app'
source_branch = 'master'  # Add the source branch name here

destination_owner = 'kailash8465'
destination_repo = 'final_test'
destination_branches = ['feature/devops', 'feature/devops-master']  # Add the destination branch names here

# List of files to be copied
files_to_copy = [
    {
        'source_path': 'gradle/wrapper/gradle-wrapper.jar',
        'destination_path': 'gradle/wrapper/gradle-wrapper.jar'
    },
    {
        'source_path': 'Dockerfile',
        'destination_path': 'Dockerfile'
    }
    # Add more files as necessary
]

def set_default_branch(repo_owner, repo_name, default_branch):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {
        'Authorization': f'Token {access_token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    }
    payload = {
        'default_branch': default_branch
    }
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"Default branch set to {default_branch} successfully for repository {repo_name}.")
    else:
        print(f"Failed to set default branch. Error: {response.text}")


def copy_file(source_path, destination_path, destination_branch):
    source_url = f"https://api.github.com/repos/{source_owner}/{source_repo}/contents/{source_path}?ref={source_branch}"
    
    headers = {
        'Authorization': f'Token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(source_url, headers=headers)
    response_json = response.json()
    print(response_json)

    content = response_json['content']
    encoded_content = content.encode('utf-8')
    decoded_content = base64.b64decode(encoded_content)

    destination_url = f"https://api.github.com/repos/{destination_owner}/{destination_repo}/contents/{destination_path}"

    payload = {
        'message': 'Copy file',
        'content': base64.b64encode(decoded_content).decode('utf-8'),
        'branch': destination_branch
    }

    response = requests.put(destination_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print(f"File {destination_path} copied successfully to branch {destination_branch}.")
    else:
        print(f"Failed to copy file {destination_path} to branch {destination_branch}. Error: {response.text}")

        
set_default_branch(destination_owner, destination_repo, "develop")
# Copy files to each destination branch
for file in files_to_copy:
    source_path = file['source_path']
    destination_path = file['destination_path']
    for branch in destination_branches:
        copy_file(source_path, destination_path, branch)
