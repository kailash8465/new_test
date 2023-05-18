from github import Github
import os


# Replace 'ACCESS_TOKEN' with your actual access token
access_token = os.environ.get('ACCESS_TOKEN')
# Create a PyGithub instance using the access token
g = Github(access_token)

# Replace 'OWNER' and 'REPO' with the owner and repository name
owner = 'kailash8465'
repo_name = 'final_test'
# Get the repository
repo = g.get_repo(f'{owner}/{repo_name}')

# Create the 'developer' branch from 'main'
main_branch = repo.get_branch('main')

repo.create_git_ref(ref='refs/heads/develop', sha=main_branch.commit.sha)

# Create the 'master' branch from 'main'
repo.create_git_ref(ref='refs/heads/master', sha=main_branch.commit.sha)

# Create the 'feature/devops' branch from 'developer'
developer_branch = repo.get_branch('develop')

repo.create_git_ref(ref='refs/heads/feature/devops',
sha=developer_branch.commit.sha)

# Create the 'feature/devops-master' branch from 'master'
master_branch = repo.get_branch('master')

repo.create_git_ref(ref='refs/heads/feature/devops-master',
sha=master_branch.commit.sha)
