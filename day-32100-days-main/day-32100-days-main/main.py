# Step 1: Import the random library
import random

# Step 2: Create a list of greetings in different languages
greetings = [
    "Hello",           # English
    "Hola",            # Spanish
    "Bonjour",         # French
    "Hallo",           # German
    "Ciao",            # Italian
    "Olá",             # Portuguese
    "Привет",          # Russian
    "こんにちは",       # Japanese
    "안녕하세요",       # Korean
    "你好",             # Chinese
]

# Step 3: Generate a random number between 0 and the maximum number of items in the list
random_greeting = random.choice(greetings)

# Step 4: Print the selected greeting using f-string
print(f"Random Greeting: {random_greeting}")
