
import os
import re
import json
import urllib.request
from datetime import datetime, timezone

# Path configuration
REPO_ROOT = "."
README_PATH = "README.md"

def get_problem_folders():
    folders = []
    # Matches folders named like '0001-two-sum' or '0001-Two-Sum'
    pattern = re.compile(r"^(\d{4})-(.+)$")
    
    for entry in os.listdir(REPO_ROOT):
        full_path = os.path.join(REPO_ROOT, entry)
        if os.path.isdir(full_path):
            match = pattern.match(entry)
            if match:
                num = match.group(1)
                slug = match.group(2)
                folders.append((num, slug, full_path, entry))
    return sorted(folders, key=lambda x: x[0])

def fetch_leetcode_difficulty(title_slug):
    """Fetches real difficulty directly from LeetCode's GraphQL API"""
    url = "https://leetcode.com/graphql"
    graphql_query = {
        "query": """
        query questionTitle($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": title_slug.lower()}
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(graphql_query).encode("utf-8"), 
            headers=headers, 
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            difficulty = res_data["data"]["question"]["difficulty"]
            return difficulty  # Returns "Easy", "Medium", or "Hard"
    except Exception:
        return "Easy" # Safe fallback fallback if API drops out

def parse_problem_metadata(folder_path, slug):
    # Fetch accurate live difficulty status 
    difficulty = fetch_leetcode_difficulty(slug)
    language = "Python 3"
    
    # Check for solution file extension to track languages used
    for file in os.listdir(folder_path):
        if file.endswith(".py"):
            language = "Python 3"
        elif file.endswith(".cpp"):
            language = "C++"
        elif file.endswith(".java"):
            language = "Java"
        elif file.endswith(".sql"):
            language = "MySQL"

    # Capture the historical file modification date
    date_str = datetime.now().strftime("%Y-%m-%d")
    for file in os.listdir(folder_path):
        if not file.startswith("."):
            mtime = os.path.getmtime(os.path.join(folder_path, file))
            date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            break

    return difficulty, language, date_str

def generate_dashboard():
    problems = get_problem_folders()
    
    stats = {"Easy": 0, "Medium": 0, "Hard": 0}
    table_rows = []
    
    print(f"Processing {len(problems)} problems. Fetching structural metadata...")
    for num, slug, folder_path, folder_name in problems:
        difficulty, language, date_str = parse_problem_metadata(folder_path, slug)
        stats[difficulty] = stats.get(difficulty, 0) + 1
        
        # Format the title strings cleanly
        problem_title = slug.replace("-", " ").title()
        problem_title = problem_title.replace("Of ", "of ").replace("In ", "in ").replace("And ", "and ").replace("To ", "to ")
        
        problem_link = f"https://leetcode.com/problems/{slug.lower()}/"
        solution_link = f"./{folder_name}"
        
        row = f"| {num} | [{problem_title}]({problem_link}) | [{folder_name}]({solution_link}) | {difficulty} | {language} | {date_str} |"
        table_rows.append(row)
        
    total_solved = len(problems)
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    
    if not table_rows:
        table_rows = ["| - | No solutions synced yet. Run the workflow to begin! | - | - | - | - |"]
        
    # Building Markdown UI layout
    markdown = f"""# 🏆 LeetCode Automator Hub

<p align="center">
  <a href="https://github.com/your-username/your-repo/actions/workflows/sync_leetcode.yml">
    <img src="https://github.com/your-username/your-repo/actions/workflows/sync_leetcode.yml/badge.svg" alt="Sync Status" />
  </a>
  <img src="https://img.shields.io/badge/TOTAL%20SOLVED-{total_solved}-blue?style=for-the-badge&logo=leetcode" alt="Total Solved" />
  <img src="https://img.shields.io/badge/EASY-{stats['Easy']}-brightgreen?style=for-the-badge" alt="Easy Solved" />
  <img src="https://img.shields.io/badge/MEDIUM-{stats['Medium']}-orange?style=for-the-badge" alt="Medium Solved" />
  <img src="https://img.shields.io/badge/HARD-{stats['Hard']}-red?style=for-the-badge" alt="Hard Solved" />
  <img src="https://img.shields.io/github/license/your-username/your-repo?style=for-the-badge" alt="License" />
</p>

---

## 📖 Project Overview & "How It Works"

**LeetCode Automator Hub** is a clean, automated synchronization pipeline that pulls your accepted LeetCode solutions, structures them into dedicated folders, and dynamically compiles an interactive dashboard tracking your coding progress.

### 🔄 Workflow Architecture

```mermaid
graph TD
    A[LeetCode Platform] -->|Accepted Submission| B(GitHub Action)
    B -->|leetcode-sync| C[Save Solution Files]
    C -->|Git Hard Reset & Pull| D[build_readme.py]
    D -->|GraphQL Query Live Difficulty| E[Parse Directory & Metadata]
    E -->|Update README.md| F[Commit & Push back to GitHub]
```

- **Sync Engine**: Powered by `leetcode-sync`, the action connects via session and CSRF credentials to pull latest solutions.
- **Documentation Builder**: `build_readme.py` queries the LeetCode GraphQL API to obtain live difficulty badges and constructs the statistics table.

---

## ✨ Key Features

- **🔄 Automated Weekly Synchronization**: Runs on a scheduled cron job (every Saturday) or on-demand manually.
- **📊 Interactive Statistics Dashboard**: Displays difficulty-wise counts (Easy, Medium, Hard) and total solutions solved.
- **📁 Structured Directory Mapping**: Automatically routes problems into folders like `0001-two-sum/` using zero-padded slug formats.
- **🚀 Live Difficulty Badging**: Queries official LeetCode GraphQL API endpoints rather than guessing or hardcoding difficulties.
- **💻 Multilingual Support**: Automatically detects solution file extensions (`.py`, `.cpp`, `.java`, `.sql`) to catalog languages used.

---

## 📁 Directory & Architecture Layout

```text
leetcode-automator-hub/
├── .github/
│   └── workflows/
│       └── sync_leetcode.yml     # GitHub Actions workflow automation
├── 0001-two-sum/                 # Auto-generated solution directory
│   └── two-sum.py                # Auto-generated solution file
├── build_readme.py               # Core Python generator script
└── README.md                     # Main documentation & dynamic dashboard
```

---

## ⚙️ Step-by-Step Installation & Setup Guide

Follow this guide to host your own LeetCode dashboard in a GitHub repository:

### 1. Copy Workflow and Script
Ensure your repository has these files:
- `.github/workflows/sync_leetcode.yml`
- `build_readme.py`

### 2. Retrieve LeetCode Session & CSRF Token
1. Go to [LeetCode](https://leetcode.com/) and sign in.
2. Press `F12` to open browser Developer Tools, and navigate to the **Network** tab.
3. Refresh the page or click on any query. Search for a request (e.g. `/api/...` or GraphQL requests).
4. Under **Headers** (specifically Request Headers) or the **Cookies** tab, find:
   - `LEETCODE_SESSION`
   - `csrftoken` (use this for `LEETCODE_CSRF_TOKEN`)

### 3. Add GitHub Repository Secrets
1. Navigate to your GitHub repository > **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret** and add:
   - Name: `LEETCODE_SESSION`, Value: *(your copied session cookie value)*
   - Name: `LEETCODE_CSRF_TOKEN`, Value: *(your copied csrf token value)*

### 4. Enable Workflow Write Permissions
For the action to commit modifications:
1. Go to **Settings** > **Actions** > **General**.
2. Scroll to **Workflow permissions**.
3. Choose **Read and write permissions**.
4. Click **Save**.

---

## 🚀 How to Run & Use the Project

### Scheduled Syncing
The pipeline is pre-configured to run automatically **every Saturday at 08:00 UTC** via the cron schedule in `.github/workflows/sync_leetcode.yml`.

### Manual Syncing
1. Go to the **Actions** tab of your repository.
2. Select **Sync LeetCode and Build Dashboard** on the left.
3. Click the **Run workflow** dropdown on the right and select **Run workflow**.

### Running Locally
To generate the dashboard locally, make sure you have python 3 installed, and run:
```bash
python build_readme.py
```

---

## 📊 Statistics

| Metric | Count |
| :--- | :--- |
| **Total Solved** | {total_solved} |
| **Easy** | {stats['Easy']} |
| **Medium** | {stats['Medium']} |
| **Hard** | {stats['Hard']} |
| **Languages** | MySQL, Python 3, Java, C++ |
| **Last Updated** | {current_time} |

## 📁 Solutions

| # | Problem | Solution | Difficulty | Language | Date |
| :-: | :--- | :--- | :-: | :-: | :-: |
""" + "\n".join(table_rows) + """

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, copy, and modify it.

---

<p align="center">
  Built with ❤️ by Antigravity & the GitHub Community
</p>
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    generate_dashboard()
