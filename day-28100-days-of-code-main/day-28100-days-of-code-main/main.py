import os
import random
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
    char_type = input(
        "Choose a Character Type (Human, Elf, Wizard, Orc, Imp):\n")
    health = generate_health()
    strength = generate_strength()
    return {
        "name": name,
        "type": char_type,
        "health": health,
        "strength": strength
    }


def display_character(character):
    """Display the generated character stats."""
    os.system("clear")
    print("⚔️  LEGEND CREATED ⚔️")
    print(f"Name: {character['name']}")
    print(f"Type: {character['type']}")
    print(f"HEALTH: {character['health']}")
    print(f"STRENGTH: {character['strength']}")
    print("May your name go down in Legend...\n")


def battle(char1, char2):
    """Simulate a battle between two characters."""
    round_counter = 0

    while True:
        round_counter += 1
        os.system("clear")
        print(f"⚔️  BATTLE ROUND {round_counter} ⚔️\n")

        # Roll dice for both characters
        roll1 = roll_dice(6)
        roll2 = roll_dice(6)

        print(f"{char1['name']} rolls: {roll1}")
        print(f"{char2['name']} rolls: {roll2}\n")

        if roll1 > roll2:
            damage = abs(char1['strength'] - char2['strength']) + 1
            char2['health'] -= damage
            print(
                f"{char1['name']} wins the round and deals {damage} damage to {char2['name']}!"
            )
        elif roll2 > roll1:
            damage = abs(char2['strength'] - char1['strength']) + 1
            char1['health'] -= damage
            print(
                f"{char2['name']} wins the round and deals {damage} damage to {char1['name']}!"
            )
        else:
            print("It's a tie! No damage this round.\n")

        # Display current stats
        print(f"{char1['name']}\nHEALTH: {char1['health']}\n")
        print(f"{char2['name']}\nHEALTH: {char2['health']}\n")

        # Check for a winner
        if char1['health'] <= 0:
            print(f"\nOh no! {char1['name']} has fallen!")
            print(
                f"{char2['name']} is victorious after {round_counter} rounds! 🏆\n"
            )
            break
        elif char2['health'] <= 0:
            print(f"\nOh no! {char2['name']} has fallen!")
            print(
                f"{char1['name']} is victorious after {round_counter} rounds! 🏆\n"
            )
            break

        print("And they're both standing for the next round!\n")
        time.sleep(2)


def main():
    """Main loop to set up and execute battles."""
    while True:
        os.system("clear")
        print("🎲⚔️ CHARACTER BATTLE CREATOR ⚔️🎲\n")

        print("Create your first Legend:\n")
        char1 = create_character()
        display_character(char1)

        print("Create your second Legend:\n")
        char2 = create_character()
        display_character(char2)

        print("\nThe battle begins in 3 seconds... Prepare yourself! ⚔️\n")
        time.sleep(3)

        battle(char1, char2)

        play_again = input(
            "Do you want to start another battle? (Yes/No):\n").lower()
        if play_again not in ["yes", "y"]:
            print("Thank you for playing! Farewell, brave adventurer.")
            time.sleep(2)
            break


if __name__ == "__main__":
    main()
