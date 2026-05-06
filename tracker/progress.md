WHAT WE SET UP:
Created folder ~/tracker in WSL
Created virtual environment inside it — venv/
Activated venv and installed Flask
Created folder structure — static/, templates/, app.py, .env, .gitignore
.gitignore tells Git to ignore venv/, .env, __pycache__/, *.pyc
Initialized Git, renamed branch to main, connected to GitHub remote, pushed first commit
Added README.md

WHY EACH FOLDER EXISTS:
templates/ — HTML pages Flask sends to the browser
static/ — CSS, fonts, icons that style those pages
venv/ — isolated Python environment for this project
.env — will store Groq API key privately
app.py — the brain of the app, all Flask code goes here

## Next Session
database.py - SQLite setup for daily logs.
database.py will have: get_db_connected(), init_db(), logs table with id, date, task_name, rating, notes.
Flask routes to build: /log (POST), /report (GET), /weekly (GET).
SQLite stores data in a single .db file, no server needed.
logs table columns: id, date, task_name, rating, notes
init_db() creates tables if they don't already exist.
Flask route /log will accept POST request with form data.
rating input will be validated: must be integer between 1-5.
/report route will fetch all logs from database and display.

## Goal: Complete tracker project within 3 weeks of exam completion