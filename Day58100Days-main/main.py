import random

# Initialize total attempts
totalAttempts = 0


# Game function
def game():
    attempts = 0
    number = random.randint(
        1, 100
    )  
# Generate the random number once to avoid changing it in every loop iteration
    while True:
        try:
            guess = int(input("Pick a number between 1 and 100: ")
                        )  # Ensure user input is converted to an integer
            if guess > number:
                print("Too high")
                attempts += 1  # Increment attempts on incorrect guess
            elif guess < number:
                print("Too low")
                attempts += 1  # Increment attempts on incorrect guess
            else:
                print("Just right!")
                print(f"{attempts} attempts this round")
                return attempts  # Return attempts to update totalAttempts in the main loop
        except ValueError:
            print("Please enter a valid number."
                  )  # Handle invalid input to prevent crashes


# Main loop
while True:
    # Display menu options
    print("\n1: Guess the random number game")
    print("2: Total Score")
    print("3: Exit")
    menu = input(
        "> ")  # Input returns a string, so compare it with string values

    if menu == "1":
        # Add the result of the game (number of attempts) to totalAttempts
        totalAttempts += game()
    elif menu == "2":
        # Show the total number of attempts so far
        print(f"You've had {totalAttempts} attempts.")
    elif menu == "3":
        # Exit the program
        print("Thanks for playing!")
        break
    else:
        # Handle invalid menu options
        print("Invalid option. Please select 1, 2, or 3.")

# Debugging Fixes:
# 1. Corrected the input type for 'menu' to match string comparisons.
# 2. Moved random number generation outside the game loop to avoid changing the target number during each iteration.
# 3. Handled ValueError for invalid inputs in the game to prevent crashes.
# 4. Ensured 'totalAttempts' updates correctly by returning attempts from the game function.
