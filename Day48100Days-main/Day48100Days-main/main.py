# Program to create and update a high score table

def save_high_score(initials, score):
    """Saves the user's initials and score to the 'high.score' file."""
    with open('high.score', 'a') as file:
        file.write(f"{initials} {score}\n")

print("\u2729 HIGH SCORE TABLE \u2729")

while True:
    # Get user input for initials and score in one line
    user_input = input("Enter your initials and score (e.g., ABC 12345): ")
    try:
        initials, score = user_input.split()
        score = int(score)  # Validate that score is an integer

        if not initials.isalpha() or len(initials) != 3:
            raise ValueError("Initials must be exactly 3 letters.")

        save_high_score(initials.upper(), score)
        print("Added to high score table.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        continue

    # Ask if the user wants to add another score
    add_another = input("Add another? y/n: ").strip().lower()
    if add_another == 'n':
        print("All scores have been saved.")
        break
