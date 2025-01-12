import random

# Generate a random number between 0 and 1,000,000
target_number = random.randint(0, 1000000)
attempts = 0  # Counter for attempts

print("Welcome to the 'Guess the Number' game!")
print("I've chosen a number between 0 and 1,000,000. Can you guess it?")

while True:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess (or a negative number to quit): "))
        
        if guess < 0:  # Exit if the user enters a negative number
            print("Goodbye! Thanks for playing. 👋")
            break
        
        attempts += 1  # Increment attempts counter
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {target_number} correctly in {attempts} attempts. 🎉")
            break
    except ValueError:
        print("Please enter a valid integer.")
