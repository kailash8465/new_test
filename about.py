import requests
import os

def update_github_repository(repo_owner, repo_name, access_token, description=None, topics=None):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.mercy-preview+json"  # Required for working with topics
    }

    # Update description
    if description:
        data = {"description": description}
        response = requests.patch(f"https://api.github.com/repos/{repo_owner}/{repo_name}", headers=headers, json=data)
        response.raise_for_status()

    # Update topics
    if topics:
        data = {"names": topics}
        response = requests.put(f"https://api.github.com/repos/{repo_owner}/{repo_name}/topics", headers=headers, json=data)
        response.raise_for_status()

# Example usage
repo_owner = "kailash8465"
repo_name = "final_test"
github_access_token = os.environ.get('token')
if repo_name.startswith('c360'):
  new_description = f"c360-{repo_name}"
elif repo_name.startswith('cdp'):
  new_description = f"cdp-{repo_name}"
else:
  new_description = repo_name
new_topics = ['github-actions-enabled','owner-dq5209','mcost-center-1000505146','pg-digital-experiences']

update_github_repository(repo_owner, repo_name, github_access_token, description=new_description, topics=new_topics)
