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
-Learn what "from flask import Flask" and "app = Flask(__name__)" actually means
-Write first route - home page