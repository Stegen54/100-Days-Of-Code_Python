from tkinter import *
from PIL import Image, ImageTk

# Initialize main window
window = Tk()
window.title("Visual Novel Game")
window.geometry("800x600")

# Load images using PIL
def load_webp(filename):
    """Load and resize webp images to a standard size"""
    image = Image.open(filename)
    # Calculate new dimensions maintaining aspect ratio
    target_width = 600
    target_height = 400
    
    # Get original dimensions
    width, height = image.size
    
    # Calculate aspect ratios
    aspect = width / height
    target_aspect = target_width / target_height
    
    if aspect > target_aspect:
        # Image is wider than target
        new_width = target_width
        new_height = int(target_width / aspect)
    else:
        # Image is taller than target
        new_height = target_height
        new_width = int(target_height * aspect)
    
    # Resize image with antialiasing
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

# Load images
start_image = load_webp("StartScreen.webp")
unhappy_ending_image = load_webp("UnhappyEnding.webp")
good_ending_image = load_webp("GoodEnding.webp")

# Create global labels
image_label = Label(window)
text_label = Label(window, wraplength=700, font=("Arial", 12))

def clear_screen():
    """Remove all widgets from screen"""
    for widget in window.winfo_children():
        widget.pack_forget()

def start_scene():
    """Display start scene"""
    clear_screen()
    image_label.configure(image=start_image)
    image_label.pack(pady=10)
    
    text_label.configure(text="You find yourself at a crossroads in your journey. Which path will you choose?")
    text_label.pack(pady=10)
    
    Button(window, text="Take the forest path", command=forest_path).pack(pady=5)
    Button(window, text="Follow the river", command=river_path).pack(pady=5)

def forest_path():
    """Forest path branch"""
    clear_screen()
    text_label.configure(text="The forest is dark and mysterious. You hear strange noises...")
    text_label.pack(pady=10)
    
    Button(window, text="Investigate the sounds", command=unhappy_ending).pack(pady=5)
    Button(window, text="Run away quickly", command=unhappy_ending).pack(pady=5)

def river_path():
    """River path branch"""
    clear_screen()
    text_label.configure(text="The river flows peacefully. You see something glinting in the water...")
    text_label.pack(pady=10)
    
    Button(window, text="Reach for the shiny object", command=good_ending).pack(pady=5)
    Button(window, text="Continue walking", command=unhappy_ending).pack(pady=5)

def unhappy_ending():
    """Unhappy ending scene"""
    clear_screen()
    image_label.configure(image=unhappy_ending_image)
    image_label.pack(pady=10)
    
    text_label.configure(text="Oh no! Your journey ends in failure!")
    text_label.pack(pady=10)
    
    Button(window, text="Start Again", command=start_scene).pack(pady=5)

def good_ending():
    """Good ending scene"""
    clear_screen()
    image_label.configure(image=good_ending_image)
    image_label.pack(pady=10)
    
    text_label.configure(text="Congratulations! You found the treasure and completed your journey!")
    text_label.pack(pady=10)
    
    Button(window, text="Start Again", command=start_scene).pack(pady=5)

# Start the game
start_scene()
window.mainloop()