from eventHandler import load_activity

def main():
    cmd = input("Welcome to GitHub User Activity Checker! Please enter a GitHub username along with the command 'github-activity': ")
    
    parts = cmd.split()

    if len(parts) < 2 or parts[0] != "github-activity":
        print(f"Invalid command. Please use 'github-activity' followed by a GitHub username.")
    
    else:
        username = parts[1]
        print(f"Fetching activity for user: {username}...")
        load_activity(username)

if __name__ == "__main__":
    main()