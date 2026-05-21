from datetime import date
from flask import Flask, render_template, request
from database import init_db, get_db_connection

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
    return "Weekly report - coming soon."

@app.route("/weekly")
def weekly():
    return "Weekly summary - coming soon."

if __name__ == "__main__":
    app.run(debug=True)