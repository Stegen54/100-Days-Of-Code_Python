import tkinter as tk

# Global variables
answer = 0
last_number = 0
operator = ""

def button_choice(value):
    """Handles numeric button clicks."""
    current = display_label["text"]
    if current == "0":
        display_label["text"] = str(value)
    else:
        display_label["text"] += str(value)

def operator_choice(op):
    """Handles operator button clicks."""
    global last_number, operator
    last_number = int(display_label["text"])
    operator = op
    display_label["text"] += f" {op} "

def calc():
    """Calculates the result based on the chosen operator."""
    global last_number, operator, answer
    expression = display_label["text"]
    try:
        answer = eval(expression.replace("x", "*").replace("\u00f7", "/"))
        display_label["text"] = f"{expression} = {answer}"
    except Exception as e:
        display_label["text"] = "Error"

# Create the main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x400")

# Display label
display_label = tk.Label(root, text="0", anchor="e", font=("Arial", 24), bg="white", relief="sunken")
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button click handling
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit():
        cmd = lambda t=text: button_choice(t)
    elif text == 'C':
        cmd = lambda: display_label.config(text="0")
    elif text == '=':
        cmd = calc
    else:
        cmd = lambda t=text: operator_choice(t)

    tk.Button(root, text=text, command=cmd, font=("Arial", 18), height=2, width=5).grid(row=row, column=col)

# Adjust grid weights for responsiveness
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
