from flask import Flask, render_template

app = Flask(__name__)

# Dictionary to store reflection data
reflections = {
    "78": {
        "name": "Day 78",
        "title": "Building a Reflection Journal",
        "text": "Today I learned how to create dynamic routes in Flask and use them to build a reflection journal.",
        "link": "https://github.com/Stegen54/100-Days-Of-Code_Python/tree/main/Day78100Days-main",
        "image": "Zoro.jpg"
    }
    # I will add more days as needed
}

@app.route('/')
def home():
    return render_template('index.html', days=sorted(reflections.keys()))

@app.route('/<dayNumber>')
def portfolio(dayNumber):
    if dayNumber in reflections:
        return render_template('portfolio.html', **reflections[dayNumber])
    return "Day not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
