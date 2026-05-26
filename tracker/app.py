"""Daily Performance Tracker application"""

import os
from datetime import date, datetime
from dotenv import load_dotenv
import groq
from flask import Flask, render_template, request
import markdown
from database import init_db, get_db_connection

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = "tracker-dev-key"
app.config["DEBUG"] = True

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        today = date.today().strftime("%Y-%m-%d")
        gita_rating = request.form["gita_reading_rating"]
        gita_notes = request.form["gita_reading_notes"]
        health_rating = request.form["health_rating"]
        health_notes = request.form["health_notes"]
        project_rating = request.form["project_rating"]
        project_notes = request.form["project_notes"]
        exercise_rating = request.form["exercise_rating"]
        exercise_notes = request.form["exercise_notes"]
        english_rating = request.form["english_rating"]
        english_notes = request.form["english_notes"]
        distraction_rating = request.form["distraction_rating"]
        distractions_notes = request.form["distractions_notes"]
        mindful_rating = request.form["mindful_rating"]
        mindful_notes = request.form["mindful_notes"]
        reflection_rating = request.form["reflection_rating"]
        reflection_notes = request.form["reflection_notes"]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Gita Reading", gita_rating, gita_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Health & Nutrition ", health_rating, health_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Project Work", project_rating, project_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Physical Exercise", exercise_rating, exercise_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "English Practice", english_rating, english_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "NO Distraction", distraction_rating, distractions_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Mindful Response", mindful_rating, mindful_notes))
        cursor.execute("""
            INSERT INTO logs (date, task_name, rating, notes)
            VALUES (?, ?, ?, ?)
        """, (today, "Daily Reflection", reflection_rating, reflection_notes))
        conn.commit()
        conn.close()
    return render_template("log.html")


@app.route("/report")
def report():
    conn = get_db_connection()
    logs = conn.execute("SELECT * FROM logs").fetchall()
    conn.close()
    return render_template("report.html", logs=logs)

def generate_summaries():
    conn = get_db_connection()
    logs = conn.execute("SELECT * FROM logs ORDER BY date ASC").fetchall()

    weeks = {}
    for log in logs:
        d = datetime.strptime(log["date"], "%Y-%m-%d")
        week_label = d.strftime("%Y-W%W")
        if week_label not in weeks:
            weeks[week_label] = []
        weeks[week_label].append(log)

    existing = conn.execute("SELECT period_label FROM summaries").fetchall()
    existing_labels = [row["period_label"] for row in existing]

    for week_label, week_logs in weeks.items():
        if week_label in existing_labels:
            continue
        summary_lines = []
        for log in week_logs:
            line = f"{log['date']} | {log['task_name']} | Rating: {log['rating']} | Notes: {log['notes']}"
            summary_lines.append(line)
        summary_text = "\n".join(summary_lines)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.execute(
            "INSERT INTO summaries (period_type, period_label, summary_text, created_at) VALUES (?, ?, ?, ?)",
            ("weekly", week_label, summary_text, now)
        )
    conn.commit()
    conn.close()

@app.route("/weekly")
def weekly():
    generate_summaries()
    conn = get_db_connection()
    summaries = conn.execute("SELECT * FROM summaries ORDER BY period_label ASC").fetchall()
    conn.close()

    all_summaries_text = ""
    for s in summaries:
        all_summaries_text += f"\n{s['period_label']}:\n{s['summary_text']}\n"

    client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"""You are a personal performance coach. Below is a user's daily performance log summarised by week from day 1 till today.

{all_summaries_text}

Analyse this data and provide:
1. Overall performance trends
2. Tasks where performance is consistently poor
3. Specific actionable suggestions to improve
4. Patterns you notice across weeks"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    analysis = markdown.markdown(response.choices[0].message.content)
    return render_template("weekly.html", analysis=analysis)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    conn = get_db_connection()
    summaries = conn.execute("SELECT * FROM summaries ORDER BY period_label ASC").fetchall()
    history = conn.execute("SELECT * FROM chat_history ORDER BY created_at ASC").fetchall()

    all_summaries_text = ""
    for s in summaries:
        all_summaries_text += f"\n{s['period_label']}:\n{s['summary_text']}\n"
    
    messages = [{"role": "system", "content": f"""You are a personal performance coach and domain expert.
You have access to the user's complete performance history:
{all_summaries_text}
When answering, combine the user's personal data with deep domain knowledge in philosophy, biology, psychology etc."""}]

    for h in history:
        messages.append({"role": h["role"], "content": h["content"]})

    messages.append({"role": "user", "content": user_message})


    client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    assistant_message = response.choices[0].message.content

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO chat_history (role, content, created_at) VALUES (?, ?, ?)",
        ("user", user_message, now)
    )
    conn.execute(
        "INSERT INTO chat_history (role, content, created_at) VALUES (?, ?, ?)",
        ("assistant", assistant_message, now)
    )
    conn.commit()
    conn.close()

    assistant_message = markdown.markdown(assistant_message)
    return {"response": assistant_message}


if __name__ == "__main__":
    app.run(debug=True)
