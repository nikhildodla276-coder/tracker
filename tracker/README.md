# Daily Performance Tracker

A personal web app to log, measure, and improve daily habits — built with Flask, SQLite, and Groq AI.

---

## What It Does

Most habit trackers only tell you if you did something or not. This one goes deeper.

Every night, you open this app and honestly rate how each of your 8 fixed daily tasks actually went — not just done or not done, but a score from 1 to 5 with a short note in your own words. At the end of the week, Groq AI reads your scores and your actual notes and tells you where you are slipping, why, and how to fix it.

---

## Features

- Log 8 fixed daily tasks every night with yes/no, rating 1–5, and a short note
- Auto-sets rating to 0 if a task was not done
- Add one-time reminders for specific dates (groceries, laundry, etc.) — these don't affect your score
- Weekly report showing scores, streaks, and which tasks you consistently struggle with
- AI analysis powered by Groq (Llama 3.3) — based on your real notes, not generic advice
- Mobile-friendly UI so you can log from your phone at night

---

## Tech Stack

| Layer | Tool |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML, CSS |
| AI Analysis | Groq API (Llama 3.3-70b) |

---

## Project Structure

```
tracker/
├── static/          # CSS and other static files
├── templates/       # HTML pages
├── venv/            # Virtual environment (not pushed to GitHub)
├── app.py           # Main Flask application
├── .env             # API keys (not pushed to GitHub)
├── .gitignore
└── requirements.txt
```

---

## Setup

1. Clone the repository
```
git clone https://github.com/nikhildodla276-coder/tracker.git
cd tracker
```

2. Create and activate virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Add your Groq API key to `.env`
```
GROQ_API_KEY=your_key_here
```

5. Run the app
```
flask run
```

---

## The 8 Daily Tasks

1. Water Intake
2. Dry Fruits
3. Full Body Workout
4. Meditation
5. Gita Reading
6. Exam Preparation
7. Project Work
8. Typing Practice

---

## Status

Currently in active development.

| Phase | Status |
|---|---|
| Project setup | Done |
| Database design | In progress |
| Daily log page | Pending |
| Weekly report | Pending |
| AI analysis | Pending |
| UI polish | Pending |

---

## Author

Nikhil Dodla — BTech CSE (AIML), Kalinga University
Building toward financial independence through real skills, one project at a time.