import random
from colorama import Fore, Style


def roll_dice(sides):
    """Roll a dice with a given number of sides."""
    return random.randint(1, sides)


def generate_health():
    """Roll a 6-sided dice and an 8-sided dice, and return their product as health stats."""
    roll_6 = roll_dice(6)
    roll_8 = roll_dice(8)
    return roll_6 * roll_8


def main():
    """Main function to generate character health stats."""
    while True:
        # Ask for character's name
        name = input(Fore.YELLOW + "Name your warrior: " + Style.RESET_ALL)

        # Generate health stats
        health = generate_health()

        # Display character stats
        print(Fore.GREEN + f"Their health is: {health}hp" + Style.RESET_ALL)

        # Ask if the user wants to create another character
        another = input(
            Fore.CYAN +
            "Do you want to generate stats for another character? (yes/no): " +
            Style.RESET_ALL).strip().lower()
        if another != 'yes':
            print(Fore.RED + "Goodbye, brave warrior!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    main()
