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
* Filter events by type (`--type`)
* Limit number of results (`--limit`)
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
pip install -e .
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

Run directly from CLI:

```bash
github-activity <github-username>
```

### Examples

```bash
github-activity HarshNaidu
```

```bash
github-activity HarshNaidu --type push
```

```bash
github-activity HarshNaidu --limit 5
```

```bash
github-activity HarshNaidu --type pr --limit 3
```

---

## 📂 Project Structure

```
github-activity-cli/
│── github_activity/
│   │── __init__.py
│   │── main.py
│   │── eventHandler.py
│
│── setup.py
│── README.md
```

---

## ⚙️ How It Works

* Fetches events from:

  ```
  https://api.github.com/users/{username}/events
  ```
* Maps event types to dedicated handler functions
* Filters events based on CLI arguments
* Extracts structured information from event payloads
* Displays formatted CLI output

---

## ⚠️ Limitations

* Only recent public activity is available (~30 events)
* Some events may require additional API calls (e.g., commit count fallback)
* Rate limited to 60 requests/hour without authentication

---

## 🎯 Purpose of the Project

This project was built to strengthen core software engineering fundamentals through practical implementation. It focuses on:

* Designing a modular CLI-based application
* Working with external APIs (GitHub Events API)
* Parsing and transforming structured JSON data
* Implementing clean separation of concerns using handler-based architecture
* Managing environment variables and authentication securely
* Writing maintainable and extensible Python code

Additionally, the project emphasizes building real-world tooling rather than just solving isolated problems, with a focus on readability, scalability, and proper error handling.

---

## 🔮 Future Improvements

* Add colored terminal output
* Export results to JSON/CSV
* Add caching to reduce API calls
* Publish as a package on PyPI

---

## 📜 License

MIT License
<a href="https://roadmap.sh/projects/github-user-activity" style="display:inline-block;width:0;height:0;overflow:hidden;">​</a>
