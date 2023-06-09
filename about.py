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
repo_name = os.environ.get('REPO')
repos = repo_name.split(',')
github_access_token = os.environ.get('token')
for repo in repos:
    if repo.startswith('c360'):
      new_description = f"c360-{repo}"
    elif repo.startswith('cdp'):
      new_description = f"cdp-{repo}"
    else:
      new_description = repo
    new_topics = ['github-actions-enabled','owner-dq5209','mcost-center-1000505146','pg-digital-experiences','test_topic']
    update_github_repository(repo_owner, repo, github_access_token, description=new_description, topics=new_topics)
