import sys
from eventHandler import load_activity

cmd = input("Welcome to GitHub User Access Checker! Please enter a GitHub username along with the command 'github-activity': ")
sys.argv = cmd.split()

if sys.argv[0] != "github-activity":
    print(f"{sys.argv[0]} is not a valid command. Please use 'github-activity' followed by a GitHub username.")

else:
    username = sys.argv[1]
    print(f"Checking GitHub activity for user: {username}\n--------------------------------------------------------------")
    load_activity(username)