from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my blog! Visit /ai-future or /ai-effects"

@app.route('/ai-future')
def ai_future():
    blog_data = {
        'title': 'AI and the Future',
        'date': datetime.now().strftime('%B %d, %Y'),
        'content': '''
        Artificial Intelligence is reshaping our world at an unprecedented pace. 
        From autonomous vehicles to advanced medical diagnostics, AI is becoming 
        increasingly integrated into our daily lives. The future holds endless 
        possibilities as we continue to develop more sophisticated AI systems.
        '''
    }
    return render_template('blog_template.html', **blog_data)

@app.route('/ai-effects')
def ai_effects():
    blog_data = {
        'title': 'The Effects of AI in the World',
        'date': datetime.now().strftime('%B %d, %Y'),
        'content': '''
        As AI technology continues to evolve, its effects on society become more 
        pronounced. While AI brings numerous benefits like improved efficiency 
        and automation, it also raises important questions about privacy, 
        employment, and ethical considerations that we must address as a society.
        '''
    }
    return render_template('blog_template.html', **blog_data)

if __name__ == '__main__':
    app.run(debug=True)
