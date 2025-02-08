from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Valid user credentials
users = {
    "admin": {"password": "admin123", "email": "admin@example.com"},
    "user1": {"password": "pass123", "email": "user1@example.com"},
    "user2": {"password": "pass456", "email": "user2@example.com"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    try:
        if username in users and users[username]["password"] == password and users[username]["email"] == email:
            return render_template('success.html', username=username)
        else:
            return render_template('error.html')
    except:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)