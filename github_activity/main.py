import argparse
from github_activity.eventHandler import load_activity

def main():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="A CLI tool to fetch and display GitHub user activity."
    )

    parser.add_argument(
        "username",
        help="GitHub username to fetch activity for."
    )

    parser.add_argument(
        "--type",
        choices=["push", "issues", "pr", "watch", "create", "public", "delete"],
        help="Filter activity by event type."
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit the number of activities to display."
    )

    args = parser.parse_args()

    print(f"Fetching activity for user: {args.username}")
    load_activity(args.username, event_type=args.type, limit=args.limit)
