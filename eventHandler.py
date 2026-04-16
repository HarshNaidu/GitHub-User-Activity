import requests
from datetime import datetime

def load_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        activity = response.json()
        display_activity(activity)
    else:
        print(f"Failed to retrieve activity for user {username}. Status code: {response.status_code}")

def count_commits(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        print(f"Failed to retrieve commits. Status code: {response.status_code}")
        return 0

def display_activity(activity):
    for event in activity:
        if event['type'] == 'PushEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Pushed to {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')} | Commits: {count_commits(event['repo']['name'].split('/')[0], event['repo']['name'].split('/')[1])}\n--------------------------------------------------------------")
        elif event['type'] == 'CreateEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Created {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'PublicEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Made {event['repo']['name']} public at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'DeleteEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Deleted {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'ForkEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Forked {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'IssuesEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Issue {event['payload']['action']} in {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'PullRequestEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Pull request {event['payload']['action']} in {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
        elif event['type'] == 'WatchEvent':
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Started watching {event['repo']['name']} at {created_at.strftime('%Y-%m-%d %H:%M:%S')}\n--------------------------------------------------------------")
