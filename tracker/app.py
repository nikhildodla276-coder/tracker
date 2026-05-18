from flask import Flask, render_template
from database import init_db, get_db_connection

app = Flask(__name__)

app.config["SECRET_KEY"] = "tracker-dev-key"
app.config["DEBUG"] = True

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/log")
def log():
    return " Daily log page - coming soon."

@app.route("/report")
def report():
    return "Weekly report - coming soon."

@app.route("/weekly")
def weekly():
    return "Weekly summary - coming soon."

if __name__ == "__main__":
    app.run(debug=True)