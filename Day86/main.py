
from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

# Sample blog posts
initial_posts = [
    {
        "title": "Attack on Titan: A Masterpiece of Storytelling",
        "content": "Attack on Titan has redefined what anime can be. With its intricate plot, complex characters, and mind-bending twists, it's no wonder this series has become a global phenomenon. The way it handles themes of freedom, sacrifice, and the cycle of violence is truly masterful.",
        "timestamp": "2024-01-15T10:00:00.000Z"
    },
    {
        "title": "Why Fullmetal Alchemist: Brotherhood is Perfect",
        "content": "Fullmetal Alchemist: Brotherhood remains the gold standard for anime adaptations. Its perfect blend of action, philosophy, and emotional storytelling creates an unforgettable experience. The concept of equivalent exchange has never been more beautifully explored.",
        "timestamp": "2024-01-14T15:30:00.000Z"
    },
    {
        "title": "Death Note: The Psychology of Justice",
        "content": "Death Note's exploration of morality and justice through Light Yagami's descent into megalomania is a psychological thriller masterpiece. The cat-and-mouse game between L and Light keeps viewers on the edge of their seats.",
        "timestamp": "2024-01-13T18:45:00.000Z"
    },
    {
        "title": "One Piece: The Journey to 1000 Episodes",
        "content": "One Piece's achievement of reaching 1000 episodes is a testament to its incredible world-building and character development. Eiichiro Oda's ability to maintain quality and excitement over such a long series is unprecedented in anime history.",
        "timestamp": "2024-01-12T12:20:00.000Z"
    }
]

# Initialize posts in local storage equivalent
try:
    with open('posts.json', 'r') as f:
        posts = json.load(f)
except:
    posts = initial_posts
    with open('posts.json', 'w') as f:
        json.dump(posts, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/posts')
def get_posts():
    return json.dumps(posts)

if __name__ == '__main__':
    app.run(debug=True)