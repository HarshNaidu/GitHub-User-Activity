# GitHub User Activity CLI

A Python-based command-line tool that fetches and displays recent public activity of any GitHub user using the GitHub Events API.

---

## 🚀 Features

* Fetches recent public activity (~30 latest events)
* Supports multiple GitHub event types:

  * Push events (with commit count)
  * Repository creation and deletion
  * Issues and pull requests
  * Stars (watch events)
  * Public repository updates
* Modular event handling system (clean separation of logic)
* Graceful error handling with request timeouts
* Optional GitHub token support for higher rate limits

---

## 🛠️ Tech Stack

* Python 3
* `requests`
* GitHub REST API
* `python-dotenv` (for authentication)

---

## 📦 Installation

```bash
git clone https://github.com/HarshNaidu/GitHub-User-Activity.git
cd GitHub-User-Activity
pip install requests python-dotenv
```

---

## 🔐 (Optional) Setup GitHub Token

Create a `.env` file in the root directory:

```
GITHUB_TOKEN=your_personal_access_token
```

This increases API rate limits and avoids request throttling.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then enter:

```bash
github-activity <github-username>
```

### Example

```bash
github-activity HarshNaidu
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

* Fetches events from:

  ```
  https://api.github.com/users/{username}/events
  ```
* Maps event types to dedicated handler functions
* Extracts structured information from event payloads
* Displays formatted CLI output

---

## ⚠️ Limitations

* Only recent public activity is available (~30 events)
* Some events may require additional API calls (e.g., commit count fallback)
* Rate limited to 60 requests/hour without authentication

---

## 🔮 Future Improvements

* Replace input-based command with proper CLI arguments (argparse)
* Add event filtering (e.g., only commits, PRs)
* Export results to JSON/CSV
* Add colored terminal output
* Package as an installable CLI tool

---

## 📜 License

MIT License
