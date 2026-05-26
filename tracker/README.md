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