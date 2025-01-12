# Import necessary modules for colors and emojis
import emoji
from termcolor import colored


# Function to display the welcome message and explain the program
def display_welcome():
    print("\n" + "-" * 40)
    print(
        colored("🎓 Welcome to the Grade Generator! 🎓", "cyan", attrs=["bold"]))
    print("-" * 40)
    print("This program helps you calculate your grade for any test.\n")
    print(
        "Simply enter the name of the test, the maximum score, and the score you received."
    )
    print(
        "You'll receive your percentage, letter grade, and a personalized message!"
    )
    print("-" * 40 + "\n")


# Function to get user input and calculate grade
def grade_generator():
    # Display the welcome message
    display_welcome()

    # Ask user for details about the test
    test_name = input("Enter the name of the test: \n")
    max_score = float(input("Enter the maximum score possible: \n"))
    score_received = float(input("Enter the score you received: \n"))

    # Calculate the percentage score, rounding to 2 decimal places
    percentage = round((score_received / max_score) * 100, 2)

    # Determine grade, message, and color based on percentage
    if 90 <= percentage <= 100:
        grade = "A+"
        message = emoji.emojize(":star-struck: Amazing work! Keep it up!")
        color = "green"
    elif 80 <= percentage < 90:
        grade = "A"
        message = emoji.emojize(
            ":partying_face: Great job! You're doing awesome!")
        color = "green"
    elif 70 <= percentage < 80:
        grade = "B"
        message = emoji.emojize(":smile: Nice effort! Keep pushing!")
        color = "blue"
    elif 60 <= percentage < 70:
        grade = "C"
        message = emoji.emojize(
            ":thinking_face: Good attempt, but there's room for improvement!")
        color = "yellow"
    elif 50 <= percentage < 60:
        grade = "D"
        message = emoji.emojize(
            ":neutral_face: You passed, but try to study harder next time!")
        color = "magenta"
    else:
        grade = "U"
        message = emoji.emojize(
            ":pensive: Don't give up! Review your mistakes and try again!")
        color = "red"

    # Display the result to the user with a message and colored output
    print("\n" + "-" * 40)
    print(f"Test: {test_name}")
    print(f"Score: {score_received} out of {max_score}")
    print(f"Percentage: {percentage}%")
    print(colored(f"Grade: {grade}", color))
    print(colored(message, color))
    print("-" * 40)


# Run the grade generator function
grade_generator()
