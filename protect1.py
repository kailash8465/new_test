import os
from graphqlclient import GraphQLClient

def enable_branch_protection(repo_owner, repo_name, branch_name, access_token):
    client = GraphQLClient('https://api.github.com/graphql')
    client.inject_token(f'Bearer {access_token}')

    query = """
    mutation {
      updateBranchProtectionRule(input: {
        repositoryId: "<repository_id>",
        pattern: "<branch_name>",
        requiresCodeOwnerReviews: true,
        isAdminEnforced: false,
        dismissesStaleReviews: true,
        requiresApprovingReviews: true,
        restrictsReviewDismissals: true,
        reviewDismissalActorIds: ["procter-gamble/c360-repo-admins"]
      }) {
        branchProtectionRule {
          id
        }
      }
    }
    """

    response = client.execute(query.replace("<repository_id>", repo_owner+"/"+repo_name).replace("<branch_name>", branch_name).replace("<team_id>", "<team_id>"))
    print(response)

# Example usage
repo_owner = "kailash8465"
repo_name = "final_test"
branch_name = "feature/devops-master"  # or "master"
github_access_token = so.environ.get('token')

enable_branch_protection(repo_owner, repo_name, branch_name, github_access_token)
