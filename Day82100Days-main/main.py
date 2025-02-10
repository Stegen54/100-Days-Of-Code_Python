from flask import Flask, render_template

app = Flask(__name__)

# Content dictionary for different languages
content = {
    "english": {
        "title": "Welcome to My Website",
        "greeting": "Hello!",
        "message": "This is a bilingual website example."
    },
    "spanish": {
        "title": "Bienvenido a Mi Sitio Web",
        "greeting": "¡Hola!",
        "message": "Este es un ejemplo de sitio web bilingüe."
    }
}

@app.route('/')
def home():
    # Default to English content
    return render_template('page.html', data=content["english"])

@app.route('/<language>')
def language_page(language):
    # Check if URL has a valid language parameter
    if language.lower() in content:
        return render_template('page.html', data=content[language.lower()])
    return render_template('page.html', data={})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
