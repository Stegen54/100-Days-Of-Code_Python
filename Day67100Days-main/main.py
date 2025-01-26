import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Guess Who")
root.geometry("400x400")

# Function to display the image or an error message
def display_image():
    new_image = name_entry.get()
    print(f"User input: {new_image}")  # Debugging line

    # File path assumed to be Guess_Who/<name>.jpg
    path = f"GuessWho/{new_image}.jpg"
    try:
        # Load the image using PIL
        pil_image = Image.open(path)
        # Convert PIL image to PhotoImage
        image = ImageTk.PhotoImage(pil_image)
        # Update the label with the new image
        image_label.config(image=image)
        image_label.image = image  # Keep a reference!
        message_label.config(text="")  # Clear any error message
    except Exception as e:
        # Show an error message
        message_label.config(text=f"Error loading image for '{new_image}'!", fg="red")
        print(f"Error: {e}")  # For debugging

# Create a label for the instructions
instruction_label = tk.Label(root, text="Enter a name (Charlotte, Gerald, Kate, Mo):", font=("Arial", 12))
instruction_label.pack(pady=10)

# Create an entry widget for the name input
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=10)

# Create a button to load the image
load_button = tk.Button(root, text="Load Image", command=display_image, font=("Arial", 12))
load_button.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack(pady=20)

# Create a label for error messages
message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.pack(pady=10)

# Run the application
root.mainloop()
