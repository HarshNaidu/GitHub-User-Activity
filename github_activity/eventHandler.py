import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"token {token}"
}

def get_created_time(event):
    return datetime.strptime(
        event['created_at'],'%Y-%m-%dT%H:%M:%SZ'
        ).strftime('%Y-%m-%d %H:%M:%S')

def get_info_from_event(event):
    username = event['repo']['name'].split('/')[0]
    repo = event['repo']['name'].split('/')[1]
    return username, repo

def print_separator():
    print("-" * 60)

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        response = requests.get(
                        url,
                        headers=headers,
                        timeout=5
                    )
        
        if response.status_code == 200:
            return response.json()
        
        else:
            print(f"Failed to retrieve activity. Status code: {response.status_code}")
            return []
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to retrieve activity for user {username}: {e}")
        return []

def count_commits(username, repo, fallback_count):
    if fallback_count:
        return fallback_count
    
    url = f"https://api.github.com/repos/{username}/{repo}/commits"

    try:
        response = requests.get(
                        url,
                        headers=headers,
                        timeout=5
                    )
            
        if response.status_code == 200:
            return len(response.json())
        
        else:
            print(f"Failed to retrieve commits. Status code: {response.status_code}")
            return 0
        
    except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to retrieve commits for {username}/{repo}: {e}")
            return 0

def handle_push_event(event):
    username, repo = get_info_from_event(event)
    created_time = get_created_time(event)
    payload = event.get('payload', {})
    fallback_count = payload.get('size', 0)
    commit_count = count_commits(username, repo, fallback_count)
    
    print(f"Pushed to {username}/{repo} at {created_time}"
        f" | Commits: {commit_count}")
    
    print_separator()

def handle_create_event(event):
    username,repo = get_info_from_event(event)
    created_time = get_created_time(event)
    payload = event.get('payload', {})
    ref_type = payload.get('ref_type', 'unknown')
    ref = payload.get('ref', 'unknown')
    branch = f"{ref_type} {ref}"
    
    print(f"Created {branch} in {username}/{repo} at {created_time}")
    
    print_separator()

def handle_public_event(event):
    username, repo = get_info_from_event(event)
    created_time = get_created_time(event)
    
    print(f"Made {username}/{repo} public at {created_time}")
    
    print_separator()

def handle_delete_event(event):
    username, repo = get_info_from_event(event)
    payload = event.get('payload', {})
    ref_type = payload.get('ref_type', 'unknown')
    ref = payload.get('ref', 'unknown')
    branch = f"{ref_type} {ref}"
    created_time = get_created_time(event)
    
    print(f"Deleted {branch} in {username}/{repo} at {created_time}")
    
    print_separator()

def handle_issues_event(event):
    username, repo = get_info_from_event(event)
    payload = event.get('payload', {})
    action = payload.get('action')
    created_time = get_created_time(event)
    
    print(f"{action.capitalize()} issue in {username}/{repo} at {created_time}")
    
    print_separator()

def handle_pull_request_event(event):
    username, repo = get_info_from_event(event)
    payload = event.get('payload', {})
    action = payload.get('action')
    created_time = get_created_time(event)
    
    print(f"{action.capitalize()} pull request in {username}/{repo} at {created_time}")
    
    print_separator()

def handle_watch_event(event):
    username, repo = get_info_from_event(event)
    created_time = get_created_time(event)
    
    print(f"Starred {username}/{repo} at {created_time}")
    
    print_separator()

event_handler = {
    "PushEvent": handle_push_event,
    "CreateEvent": handle_create_event,
    "PublicEvent": handle_public_event,
    "DeleteEvent": handle_delete_event,
    "IssuesEvent": handle_issues_event,
    "PullRequestEvent": handle_pull_request_event,
    "WatchEvent": handle_watch_event
}

def display_activity(events):
    if not events:
        print("No recent activity found for this user.")
        return
    
    for event in events:
        event_type = event.get('type')
        handler = event_handler.get(event_type)
        
        if handler:
            handler(event)
        
        else:
            print(f"Unhandled event type: {event_type}")
            
            print_separator()

def load_activity(username, event_type=None, limit=None):
    events = fetch_activity(username)

    if event_type:
        event_map = {
            "push" : "PushEvent",
            "issues" : "IssuesEvent",
            "pr" : "PullRequestEvent",
            "create" : "CreateEvent",
            "public" : "PublicEvent",
            "delete" : "DeleteEvent",
            "watch" : "WatchEvent"
        }

        target_event = event_map.get(event_type)
        events = [e for e in events if e.get("type") == target_event]

    if limit:
        events = events[:limit]

    display_activity(events)
