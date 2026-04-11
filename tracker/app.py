from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Tracker is running."

@app.route("/log")
def log():
    return " Daily log page - coming soon."

if __name__ == "__main__":
    app.run(debug=True)