# Daily Performance Tracker

A Flask web app that tracks daily performance across 8 fixed tasks, generates AI-powered weekly analysis using Groq LLM, and keeps you accountable with a clean rating system.

## What It Does

- Displays 8 fixed daily tasks every night for rating
- Accepts a score of 1–5 per task along with optional notes
- Stores all entries in a local SQLite database
- Supports one-time task reminders (non-rated)
- Sends all weekly data to Groq LLM API for AI-generated performance analysis
- Displays the AI analysis summary inside the app

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Flask | Web framework and routing |
| SQLite | Local database for storing daily ratings |
| Groq API | LLM for weekly AI performance analysis |
| python-dotenv | Secure API key management |
| HTML/CSS | Frontend UI |

## Project Status

Complete. Tested with real daily tracking data. Tasks, ratings, and AI analysis fully functional.

## Setup and Usage

### 1. Clone the repository

```bash
git clone https://github.com/nikhildodla276-coder/tracker.git
cd tracker
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create your .env file

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## Author

Nikhil Dodla — BTech CSE AIML, Kalinga University
