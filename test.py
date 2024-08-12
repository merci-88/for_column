import requests
import json

# Set your variables
owner = 'merci-88'
repo = 'Testing-Repo'
issue_number = 11  # Example issue number
org = 'VBS-Tech-Solutions-India-Pvt-Ltd' # this is org

# Request headers with authentication and preview accept header
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.inertia-preview+json'  # Required for Projects API
}

def getProjects():

# GitHub API URL for repository projects
    url = f'https://api.github.com/repos/{owner}/{repo}/projects'

# Make the request to get repository projects
    response = requests.get(url, headers=headers)

# Check the response status
    if response.status_code == 200:
        projects = response.json()
        if projects:
            for project in projects:
                print(f"Project ID: {project['id']}, Name: {project['name']}, URL: {project['html_url']}")
        else:
            print("No projects found for this repository.")
    else:
        print(f"Failed to get repository projects: {response.status_code}")
        print(response.json())  # Print the error message


def repoDetails():

    # GitHub API URL for the repository
    url = f'https://api.github.com/repos/{owner}/{repo}'
    print('\n url = ', url)
    # Request headers with authentication
    headers = {
        'Authorization': f'token {token}'
    }

    # Make the request to get repository information
    response = requests.get(url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        repo_info = response.json()
        print('\n repo_info = ',json.dumps(repo_info))

        # Check if Projects are enabled
        if repo_info.get('has_projects'):
            print("Projects are enabled for this repository.")
        else:
            print("Projects are disabled for this repository.")
    else:
        print(f"Failed to get repository info: {response.status_code}")

def listOrganizationProjects():
# GitHub API URL for organization projects
    url = f'https://api.github.com/orgs/{org}/projects'

# Request headers with authentication
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.inertia-preview+json'  # Required for Projects API
    }

# Make the request to get organization projects
    response = requests.get(url, headers=headers)
    print('\n listOrganizationProjects response = ',response.json())
# Check the response status
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            print(f"Project ID: {project['id']}, Name: {project['name']}")
    else:
        print(f"Failed to get organization projects: {response.status_code}")


def fetchingRepositoryProjects():

# GitHub API URL for repository projects
    url = f'https://api.github.com/repos/{owner}/{repo}/projects'

# Request headers with authentication
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.inertia-preview+json'  # Required for Projects API
    }

# Make the request to get repository projects
    response = requests.get(url, headers=headers)

# Check the response status
    if response.status_code == 200:
        projects = response.json()
        print('\n projects = ', projects)
        if projects:
            for project in projects:
                print(f"Project ID: {project['id']}, Name: {project['name']}")
        else:
            print("No projects found for this repository.")
    else:
        print(f"Failed to get repository projects: {response.status_code}")
        print(response.json())  # Print the error message

def getOrgDetails():
# GitHub API URL for organization details
    url = f'https://api.github.com/orgs/{org}'

# Request headers with authentication
    headers = {
        'Authorization': f'token {token}'
    }

# Make the request to get organization details
    response = requests.get(url, headers=headers)

# Check the response status
    if response.status_code == 200:
        org_info = response.json()
        print('\n org_info = ', json.dumps(org_info))
        #print(f"Organization Name: {org_info['name']}")
    
    else:
        print(f"Failed to get organization details: {response.status_code}")


def graphQL():
# Define the GraphQL endpoint
    url = f'https://api.github.com/repos/merci-88/Testing-Repo/projects'

# Define the GraphQL query
    query = """
    query {
      repository(name: "Testing-Repo", owner: "merci-88") {
        name
        issue(number: 1){
          projectItems(first: 100) {
            nodes {
              effort: fieldValueByName(name: "Status") {
                ... on ProjectV2ItemFieldNumberValue {
                  number
                }
              }
            }
          }
        }
      }
    }"""

# Make the HTTP request
    response = requests.post(
        url,
        json={'query': query},
        headers=headers
    )

# Check for errors
    print('\n response = ', response.json())
    if response.status_code == 200:
        data = response.json()
        print(data)
        if 'errors' in data:
            print('Errors:', data['errors'])
        else:
            print('Data:', data['data'])
    else:
        print(f"Query failed with status code {response.status_code}")

# Handle the response data
    


#repoDetails()
#getProjects()
#getOrgDetails()
#listOrganizationProjects()
graphQL()