import random
import time

# Initial ideas
initial_ideas = [
    "Build a treehouse community",
    "Start a podcast about unusual hobbies",
    "Invent a glow-in-the-dark umbrella"
]

# File to store ideas
idea_file = "my.ideas"

# Write initial ideas to the file if it's empty
try:
    with open(idea_file, "x") as file:
        for idea in initial_ideas:
            file.write(idea + "\n")
except FileExistsError:
    pass  # File already exists, no need to overwrite

def add_idea():
    """Prompt the user to input a new idea and store it in the file."""
    new_idea = input("Input your idea. > ")
    with open(idea_file, "a") as file:
        file.write(new_idea + "\n")
    print("Nice! Your idea has been stored.")

def load_random_idea():
    """Load a random idea from the file and display it."""
    try:
        with open(idea_file, "r") as file:
            ideas = file.read().strip().split("\n")
        if ideas:
            random_idea = random.choice(ideas)
            print(f"Random idea: {random_idea}")
            time.sleep(3)  # Show the idea for a few seconds
        else:
            print("No ideas found. Please add some first!")
    except FileNotFoundError:
        print("No ideas file found. Please add some ideas first!")

def menu():
    """Display the main menu for the idea storage system."""
    while True:
        print("\n🌟Idea Storage🌟")
        choice = input("Add an idea or see a random idea? a/r. > ").strip().lower()
        if choice == "a":
            add_idea()
        elif choice == "r":
            load_random_idea()
        else:
            print("Invalid choice. Please enter 'a' to add or 'r' to load a random idea.")

# Start the program
if __name__ == "__main__":
    menu()
