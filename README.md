# GitHub User Activity CLI

A simple command-line tool that fetches and displays recent activity of a GitHub user using the GitHub Events API.

## 🚀 Features

  * Fetches recent public activity of any GitHub user
  * Displays different event types:
  * Push events (with commit count)
  * Repository creation
  * Forks
  * Issues
  * Pull requests
  * Stars (watch events)
  * Clean and readable CLI output
  * Lightweight and fast (no unnecessary API calls)

---

## 🛠️ Tech Stack

* Python 3
* `requests` library
* GitHub REST API

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshNaidu/GitHub-User-Activity.git
   cd GitHub-User-Activity
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then enter the command in the following format:

```bash
github-activity <github-username>
```

### Example

```bash
github-activity HarshNaidu
```

### Sample Output

```
Checking GitHub activity for user: HarshNaidu
--------------------------------------------------------------
Pushed 3 commits to HarshNaidu/GitHub-User-Activity at 2026-04-10 14:32:10
--------------------------------------------------------------
Opened issue in HarshNaidu/GitHub-User-Activity at 2026-04-09 10:12:45
--------------------------------------------------------------
Starred HarshNaidu/GitHub-User-Activity at 2026-04-08 18:20:11
--------------------------------------------------------------
```

---

## 📂 Project Structure

```
github-activity-cli/
│── main.py
│── eventHandler.py
│── README.md
```

---

## ⚙️ How It Works

* Uses the GitHub Events API:

  ```
  https://api.github.com/users/{username}/events
  ```
* Parses event types and formats them into readable CLI output
* Extracts commit count directly from event payload (no extra API calls)

---

## ⚠️ Limitations

* Only fetches recent public activity (last ~30 events)
* Subject to GitHub API rate limits (60 requests/hour for unauthenticated users)

---

## 🔮 Future Improvements

* Add authentication (increase rate limits)
* Support CLI arguments instead of input prompt
* Filter events by type (e.g., only commits, only PRs)
* Export output to JSON or CSV
* Add colored terminal output

---

## 📜 License

This project is open-source and available under the MIT License.
