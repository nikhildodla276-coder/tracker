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
Groq API will receive weekly log data and return AI analysis.
reminder table columns: id, title, due_date, done.
Flask templates will use Jinja2 to render dynamic data.
log.html will have a form with 8 task inputs and notes field.
report.html will display logs in a table format.
weekly.html will display Groq AI analysis as formatted text.
.env file will store GROQ_API_KEY securely.
python-dotenv will load .env variable into Flask app.
pylint will be run on all .py files before final commit.
README.md will include project purpose, stack, how to run.
racker.db will be added to .gitignore.

## Goal: Complete tracker project within 3 weeks of exam completion