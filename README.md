Tracker

A Python tool that logs, monitors, and visualizes daily task execution metrics to keep your workflow clean.

What It Does

Accepts user task input via CLI

Validates and processes input fields

Saves tasks to a local data file (SQLite/JSON)

Generates colorful console tables to view progress

Tech Stack

ToolPurposePython 3Core languageSQLite3/JSONLocal data persistence layerTabulate/RichVisual CLI layout engine python-dotenvSecure local environment paths

Project Status

Complete. Tested across local development iterations. Pylint score: 10/10

Setup and Usage

1. Clone the repository

git clone https://github.com/nikhildodla276-coder/tracker.git
cd tracker

2. Create virtual environment and install dependencies

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Create your .env file

LOCAL_DB_PATH=data/tracker.db

4. Run the tracker tool

python tracker.py --add "Task description here"

Author

Nikhil Dodla — BTech CSE AIML, Kalinga University
