# Daily Performance Tracker

A Flask web app that tracks daily performance across 8 tasks, stores data in SQLite, and uses Groq AI to generate weekly analysis and actionable suggestions.

## Features
- Log 8 daily tasks with ratings (1-5) and notes
- View complete log history on report page
- Weekly AI analysis powered by Groq (llama-3.3-70b)
- Persistent AI chat coach with full performance history context
- Summaries compressed weekly for efficient AI processing

## Tech Stack
- Python, Flask
- SQLite
- Groq API (llama-3.3-70b-versatile)
- HTML, CSS, Jinja2
- python-dotenv, markdown

## Setup
1. Clone the repo
2. Create and activate virtual environment
3. Install dependencies: `pip install flask groq python-dotenv markdown`
4. Create `.env` file with `GROQ_API_KEY=your_key_here`
5. Run: `python app.py`
6. Visit: `http://127.0.0.1:5000`

## Project Structure
- `app.py` — Flask routes and application logic
- `database.py` — SQLite setup and connection
- `templates/` — HTML pages
- `static/` — CSS styling
- `tracker.db` — SQLite database (auto-created)

## 3. Directory Structure & Architecture

```text
tracker/
├── app.py              # Main Flask application entry point & routes
├── database.py         # SQLite connection setup and schema initialization
├── .env                # Environment variables (GROQ_API_KEY, FLASK_SECRET)
├── .gitignore          # Excludes venv/, .env, __pycache__, and *.db
├── templates/          # Jinja2 HTML templates
│   ├── index.html      # Daily dashboard & task completion toggles
│   ├── log.html        # Evening performance logger & rating entry
│   └── report.html     # Weekly AI-generated performance breakdown
└── static/             # Static UI assets
    ├── css/
    │   └── style.css   # Custom CSS styling
    └── js/
        └── main.js     # Client-side dynamic interactivity