import random
from prettytable import PrettyTable # type: ignore
from termcolor import colored # type: ignore

def generate_random_numbers():
    """Generate a sorted list of unique random numbers between 1 and 90."""
    numbers = random.sample(range(1, 91), 8)  # Generate 8 unique numbers
    numbers.sort()
    return numbers

def create_card(numbers):
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

def check_bingo(bingo_card):
    """Check if the bingo card has all 'X's."""
    for row in bingo_card:
        for item in row:
            if item != 'X' and item != "BINGO!":
                return False
    return True

def update_bingo_card(bingo_card, number):
    """Update the bingo card by replacing the matched number with 'X'."""
    for row in bingo_card:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = 'X'

def main():
    """Main function to generate and display the Bingo card."""
    numbers = generate_random_numbers()
    bingo_card = create_card(numbers)
    pretty_print_bingo(bingo_card)

    while True:
        next_number = int(input("Enter the next number: "))
        update_bingo_card(bingo_card, next_number)
        pretty_print_bingo(bingo_card)
        if check_bingo(bingo_card):
            print("Congratulations! You've won!")
            break

if __name__ == "__main__":
    main()
