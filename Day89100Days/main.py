from flask import Flask, render_template, request, redirect
import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import os

app = Flask(__name__)
# Use environment variable if exists, otherwise use default key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-default-secret-key')
login_manager = LoginManager()
login_manager.init_app(app)

# Using dictionary instead of Replit DB for local development
messages_db = {}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect('/login')
    messages = []
    # Sort messages by timestamp
    sorted_messages = sorted(messages_db.items(), reverse=True)[:5]
    for _, msg in sorted_messages:
        messages.append(msg)
    is_admin = current_user.id == "admin"  # Change to your desired admin username
    return render_template("chat.html", messages=messages, is_admin=is_admin)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple authentication for testing
        if password == "password":  # Change this to your desired password
            user = User(username)
            login_user(user)
            return redirect('/')
    return render_template("login.html")

@app.route('/post', methods=['POST'])
@login_required
def post():
    message = request.form.get('message')
    timestamp = datetime.datetime.now().timestamp()
    messages_db[timestamp] = {
        "message": message,
        "username": current_user.id,
        "timestamp": timestamp
    }
    return redirect('/')

@app.route('/delete/<timestamp>')
@login_required
def delete(timestamp):
    if current_user.id == "admin":  # Change to your desired admin username
        messages_db.pop(float(timestamp), None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
