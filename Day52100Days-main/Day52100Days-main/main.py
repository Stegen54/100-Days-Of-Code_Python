import json
import os

# Constants
SAVE_FILE = "pizza_orders.json"
COST_PER_PIZZA = 10  # Example cost per pizza

# Load orders from file
def load_orders():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading save file. Starting fresh.")
    return []

# Save orders to file
def save_orders(orders):
    with open(SAVE_FILE, "w") as file:
        json.dump(orders, file, indent=4)

# Add order subroutine
def add_order(orders):
    while True:
        try:
            quantity = int(input("How many pizzas? > "))
            break
        except ValueError:
            print("You must input a numerical character, try again.")

    size = input("What size? (Small/Medium/Large) > ").capitalize()
    name = input("Name please > ")

    cost = quantity * COST_PER_PIZZA
    print(f"Thanks {name}, your pizzas will cost ${cost}.")

    # Add to 2D list
    orders.append([name, quantity, size, cost])
    save_orders(orders)

# View orders subroutine
def view_orders(orders):
    if not orders:
        print("No orders to display.")
        return

    print("\nCurrent Orders:")
    for i, order in enumerate(orders, start=1):
        name, quantity, size, cost = order
        print(f"{i}. Name: {name}, Quantity: {quantity}, Size: {size}, Cost: ${cost}")

# Main program
def main():
    print("\n✨ Welcome to Dave's Dodgy Pizzas! ✨")
    orders = load_orders()

    while True:
        print("\nMain Menu:")
        print("1. Add an order")
        print("2. View orders")
        print("3. Exit")

        choice = input("Select an option (1/2/3): > ")

        if choice == "1":
            add_order(orders)
        elif choice == "2":
            view_orders(orders)
        elif choice == "3":
            print("Goodbye! See you next time.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
