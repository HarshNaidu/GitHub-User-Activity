import json, requests

fileName = "events.json"
API_URL = "https://api.github.com/users/{username}/events"

def load_activity(username):
    url = API_URL.format(username=username)
    response = requests.get(url)

    if response.status_code == 200:
        activity = response.json()
        save_activity(username, activity)
    else:
        print(f"Failed to retrieve activity for user {username}. Status code: {response.status_code}")

def save_activity(username, activity):
    with open(fileName, 'w') as f:
        json.dump(activity, f, indent=4)
    print(f"Activity for user {username} has been saved to {fileName}.")