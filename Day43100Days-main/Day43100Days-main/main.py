import random
from prettytable import PrettyTable
from termcolor import colored


def generate_random_numbers():
    """Generate a sorted list of unique random numbers between 1 and 90."""
    numbers = random.sample(range(1, 91), 8)  # Generate 8 unique numbers
    numbers.sort()
    return numbers


def create_bingo_card(numbers):
    """Create a 3x3 Bingo card with a center 'BINGO!' slot."""
    bingo_card = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BINGO!", numbers[4]],
        [numbers[5], numbers[6], numbers[7]],
    ]
    return bingo_card


def colorize_value(value):
    """Apply colors to values for display."""
    if value == "BINGO!":
        return colored(value, "white", "on_red", attrs=["bold"])
    return colored(value, "cyan", attrs=["bold"])


def pretty_print_bingo(bingo_card):
    """Pretty-print the Bingo card using PrettyTable with colored values."""
    table = PrettyTable()
    table.title = "Onyeali's Nan Bingo Card"
    table.field_names = ["Column 1", "Column 2", "Column 3"]

    for row in bingo_card:
        colored_row = [colorize_value(item) for item in row]
        table.add_row(colored_row)

    print(table)


def main():
    """Main function to generate and display the Bingo card."""
    numbers = generate_random_numbers()
    bingo_card = create_bingo_card(numbers)
    pretty_print_bingo(bingo_card)


if __name__ == "__main__":
    main()
