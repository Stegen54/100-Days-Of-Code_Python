from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure random key

# Local storage instead of replit db
users = {}

def check_login():
    if not session.get("loggedIn"):
        return False
    username = session.get("username")
    return username and username in users

@app.route("/")
def index():
    if check_login():
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if check_login():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        form = request.form
        if form["username"] not in users:
            users[form["username"]] = {
                "name": form["name"],
                "password": form["password"]
            }
            return redirect(url_for("login"))
        return "Username already exists"
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if check_login():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        form = request.form
        if form["username"] in users:
            if users[form["username"]]["password"] == form["password"]:
                session["loggedIn"] = True
                session["username"] = form["username"]
                return redirect(url_for("dashboard"))
            return "Invalid password"
        return "User not found"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not check_login():
        session.clear()  # Clear any invalid session data
        return redirect(url_for("login"))
    
    username = session.get("username")
    if username not in users:  # Double check user exists
        session.clear()
        return redirect(url_for("login"))
        
    return render_template("dashboard.html", name=users[username]["name"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)