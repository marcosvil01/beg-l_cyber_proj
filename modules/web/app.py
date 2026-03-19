from flask import Flask, render_template, request, escape
import sqlite3

app = Flask(__name__)

# Basic in-memory DB for demo
db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
db.execute("INSERT INTO users VALUES (1, 'admin', 'cyberhub_secure_123')")

@app.route("/")
def index():
    return """
    <h1>CyberHub: Secure vs Vulnerable Demo</h1>
    <ul>
        <li><a href='/search?q=test'>XSS Demo</a></li>
        <li><a href='/login'>SQL Injection Demo</a></li>
    </ul>
    """

@app.route("/search")
def search():
    query = request.args.get("q", "")
    # VULNERABLE TO XSS:
    return f"<h2>Search Results for: {query}</h2><p>Vulnerable version reflects raw input.</p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        # VULNERABLE TO SQLi:
        query = f"SELECT * FROM users WHERE username = '{user}'"
        cursor = db.execute(query)
        result = cursor.fetchone()
        if result:
            return f"Welcome {result[1]}! (Logged in via SQLi)"
        else:
            return "Login Failed"
    return '<form method="post">Username: <input name="username"><input type="submit"></form>'

if __name__ == "__main__":
    app.run(port=5000)
