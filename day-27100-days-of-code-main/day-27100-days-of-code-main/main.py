import random
import os
import time

def roll_dice(sides):
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

def generate_health():
    """Calculate the health stat using random dice rolls."""
    health_stat = ((roll_dice(10) * roll_dice(8)) / 3) + 15
    return round(health_stat)

def generate_strength():
    """Calculate the strength stat using random dice rolls."""
    strength_stat = ((roll_dice(12) * roll_dice(4)) / 2) + 10
    return round(strength_stat)

def create_character():
    """Generate the character's name and type."""
    name = input("Enter your Legend's Name:\n")
    char_type = input("Choose a Character Type (Human, Elf, Wizard, Orc, Imp):\n")
    return name, char_type

def display_character(name, char_type, health, strength):
    """Display the generated character stats."""
    os.system("clear")
    print("⚔️  LEGEND CREATED ⚔️")
    print(f"Name: {name}")
    print(f"Type: {char_type}")
    print(f"HEALTH: {health}")
    print(f"STRENGTH: {strength}")
    print("May your name go down in Legend...")
    print()

def main():
    """Main loop to generate and display characters."""
    while True:
        os.system("clear")
        print("🎲⚔️ CHARACTER CREATOR ⚔️🎲\n")
        name, char_type = create_character()
        health = generate_health()
        strength = generate_strength()
        display_character(name, char_type, health, strength)

        play_again = input("Do you want to create another Legend? (Yes/No):\n").lower()
        if play_again not in ["yes", "y"]:
            print("Thank you for playing! Farewell, brave adventurer.")
            time.sleep(2)
            break
        time.sleep(1)

if __name__ == "__main__":
    main()