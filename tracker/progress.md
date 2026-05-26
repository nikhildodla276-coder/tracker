# Tracker Progress

## Project Status: Complete

## What is Built
- Daily log form with 8 tasks (rating 1-5 + notes)
- SQLite database with 3 tables: logs, summaries, chat_history
- Report page showing complete log history
- Weekly AI analysis using Groq (llama-3.3-70b-versatile)
- Persistent AI chat coach with full performance history
- Navigation across all pages
- Dark theme CSS with green accent

## File Structure
- app.py — Flask routes, Groq integration, summarisation logic
- database.py — SQLite setup, table creation, connection management
- templates/index.html — home page
- templates/log.html — daily log form
- templates/report.html — log history table
- templates/weekly.html — AI analysis + chat box
- static/style.css — dark theme styling
- .env — Groq API key (not on GitHub)
- tracker.db — SQLite database (auto-created)

## Next Session
- Start Project 4: FastAPI + LangChain