import random

def roll_dice(sides=6):
    """Roll a dice with a specified number of sides."""
    return random.randint(1, sides)

def pretty_print(message, decoration="*"):
    """Print a message with decorative borders."""
    print(f"{decoration * len(message)}")
    print(message)
    print(f"{decoration * len(message)}")

def generate_random_insult():
    """Generate a random 'baldy' insult."""
    insults = [
        "You're so bald, you make a bowling ball jealous!",
        "You're so bald, even the sun needs sunglasses!",
        "You're so bald, I mistook your head for a mirror!"
    ]
    return random.choice(insults)
