from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")

def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%B %d, %Y %H:%M")

@app.route('/')
def index():
    current_time = get_current_datetime()
    return f'Welcome! Visit /portfolio or /linktree<br><br>Current time: {current_time}'

@app.route('/portfolio')
def portfolio():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>My Portfolio</title>
        <link href="static/css/portfolio.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <h1>Onyeali Emmanuel - Portfolio</h1>
        
        <div class="projects-grid">
            <section class="project">
                <a href="https://github.com/Stegen54/Day69100Days">
                    <h2>Day 69 - Visual Novel Game</h2>
                    <img src="static/images/day69.png" alt="Visual Novel Game Screenshot">
                    <p>A text-based adventure game built with Python and Tkinter that features multiple story paths and endings.</p>
                </a>
            </section>

            <section class="project">
                <a href="https://github.com/Stegen54/Day68100Days">
                    <h2>Day 68 - Guess Who Game</h2>
                    <img src="static/images/days68.png" alt="Guess Who Game Screenshot">
                    <p>An interactive game where players try to guess characters based on image clues using Python and image processing.</p>
                </a>
            </section>

            <section class="project">
                <a href="https://github.com/Stegen54/Day45100Days">
                    <h2>Day 45 - To-Do Manager</h2>
                    <img src="static/images/45.png" alt="To-Do Manager Screenshot">
                    <p>A simple to-do list application with add, view, edit, and remove functionalities.</p>
                </a>
            </section>

            <section class="project">
                <a href="https://github.com/Stegen54/Day39100Days">
                    <h2>Day 39 - Hangman Game</h2>
                    <img src="static/images/39.png" alt="Hangman Game Screenshot">
                    <p>A classic hangman game implemented in Python with a random word generator and hints.</p>
                </a>
            </section>

            <section class="project">
                <a href="https://github.com/Stegen54/Day17100Days">
                    <h2>Day 17 - Rock, Paper, Scissors</h2>
                    <img src="static/images/17.png" alt="Rock Paper Scissors Screenshot">
                    <p>An extended version of the classic game with multiple rounds and scorekeeping.</p>
                </a>
            </section>
        </div>
    </body>
    </html>
    """
    return page

@app.route('/linktree')
def linktree():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>My Link Tree</title>
        <link href="static/css/linktree.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="container">
            <img src="static/images/Onyeali.jpg" alt="Profile Picture" class="profile-img">
            <h1>Onyeali Emmanuel</h1>
            <p class="social-handle">My Socials</p>
            
            <div class="links">
                <a href="https://github.com/Stegen54" class="link-item">GitHub</a>
                <a href="https://www.linkedin.com/in/emmanuel-onyeali-29b243211/" class="link-item">LinkedIn</a>
                <a href="https://x.com/ChimezieOnyeali" class="link-item">Twitter</a>
                <a href="https://medium.com/@emmanuel.onyeali" class="link-item">Blog</a>
            </div>
        </div>
        <script src="static/js/script.js"></script>
    </body>
    </html>
    """
    return page

app.run(host='0.0.0.0', port=81)