import random

def draw_hangman(lives):
    stages = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """
    ]
    return stages[6 - lives]

def hangman():
    words = {
        "python": "A popular programming language",
        "programming": "What developers do",
        "developer": "Someone who writes code",
        "hangman": "The name of this game",
        "challenge": "A task that tests skill"
    }
    word, hint = random.choice(list(words.items()))
    guessed_word = ["_" for _ in word]
    guessed_letters = []
    lives = 6

    print("\nWelcome to 🌟 Hangman 🌟")
    print("Guess the word letter by letter.")

    while lives > 0:
        print(draw_hangman(lives))
        print(" ".join(guessed_word))
        print(f"Hint: {hint}")
        print(f"Used letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Choose a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess

            if "_" not in guessed_word:
                print("\nYou won! The word was:", word)
                break
        else:
            print("Nope, not in there.")
            lives -= 1
            print(f"{lives} lives left.")
    else:
        print(draw_hangman(lives))
        print("\nYou lost! The word was:", word)

# Run the game
hangman()
import random

def draw_hangman(lives):
    stages = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """
    ]
    return stages[6 - lives]

def hangman():
    words = {
        "python": "A popular programming language",
        "programming": "What developers do",
        "developer": "Someone who writes code",
        "hangman": "The name of this game",
        "challenge": "A task that tests skill"
    }
    word, hint = random.choice(list(words.items()))
    guessed_word = ["_" for _ in word]
    guessed_letters = []
    lives = 6

    print("\nWelcome to 🌟 Hangman 🌟")
    print("Guess the word letter by letter.")

    while lives > 0:
        print(draw_hangman(lives))
        print(" ".join(guessed_word))
        print(f"Hint: {hint}")
        print(f"Used letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Choose a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess

            if "_" not in guessed_word:
                print("\nYou won! The word was:", word)
                break
        else:
            print("Nope, not in there.")
            lives -= 1
            print(f"{lives} lives left.")
    else:
        print(draw_hangman(lives))
        print("\nYou lost! The word was:", word)

# Run the game
hangman()
