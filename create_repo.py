import os
import requests

token=os.environ.get('token')
owner='kailash8465'
def create_private_repo_with_auto_init(repo_name):
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    headers = {"Accept: application/vnd.github+json",
               'Authorization': f'token {token}'
              }
    payload = {
        'name': repo_name,
        'private': True,
        'auto_init': True
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"Private repository '{owner}/{repo_name}' with auto initialization created successfully!")
    else:
        print(f"Error creating repository: {response.status_code} - {response.text}")

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
# Replace 'your-username' with the desired owner or organization name
# Replace 'your-repo-name' with the desired repository name

create_private_repo_with_auto_init('testing-repo')
