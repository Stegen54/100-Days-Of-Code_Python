from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True  # Enable debug mode

@app.route('/')
def index():
    try:
        return render_template('portfolio.html')
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/verify', methods=['POST'])
def verify():
    is_robot = False
    
    # Check metal question
    if request.form.get('metal') == 'yes':
        is_robot = True
    
    # Check dream question
    dream = request.form.get('dream').lower()
    if 'ed-209' in dream or 'robot' in dream or 'terminator' in dream:
        is_robot = True
    
    # Check manufacturer
    if request.form.get('manufacturer') in ['sirius', 'cyberdyne']:
        is_robot = True
    
    result = "You're a robot!" if is_robot else "You're not a robot!"
    color = "red" if is_robot else "green"
    return f"""
    <html>
        <body style="background: linear-gradient(135deg, #6496f6, #9198e5); 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    height: 100vh; 
                    margin: 0;">
            <h1 style="color: {color}; 
                       font-family: Arial; 
                       padding: 20px; 
                       background: white; 
                       border-radius: 10px; 
                       box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                {result}
            </h1>
        </body>
    </html>
    """
