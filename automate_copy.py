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
destination_branch = 'feature/devops'  # Add the destination branch name here

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

def copy_file(source_path, destination_path):
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
        print(f"File {destination_path} copied successfully.")
    else:
        print(f"Failed to copy file {destination_path}. Error: {response.text}")

for file in files_to_copy:
    source_path = file['source_path']
    destination_path = file['destination_path']
    copy_file(source_path, destination_path)
