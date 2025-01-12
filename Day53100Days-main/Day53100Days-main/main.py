import os

# Define the inventory file name
INVENTORY_FILE = "inventory.txt"

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_inventory():
    """Load the inventory from the file."""
    try:
        with open(INVENTORY_FILE, "r") as file:
            return [item.strip() for item in file.readlines()]
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    """Save the inventory to the file."""
    with open(INVENTORY_FILE, "w") as file:
        file.write("\n".join(inventory))

def add_item(inventory):
    """Add an item to the inventory."""
    item = input(f"{Colors.OKCYAN}Input the item to add: > {Colors.ENDC}").strip().capitalize()
    inventory.append(item)
    save_inventory(inventory)
    print(f"{Colors.OKGREEN}{item} has been added to your inventory.{Colors.ENDC}")

def remove_item(inventory):
    """Remove an item from the inventory."""
    item = input(f"{Colors.OKCYAN}Input the item to remove: > {Colors.ENDC}").strip().capitalize()
    if item in inventory:
        inventory.remove(item)
        save_inventory(inventory)
        print(f"{Colors.OKGREEN}{item} has been removed from your inventory.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}{item} is not in your inventory.{Colors.ENDC}")

def view_item(inventory):
    """View the count of a specific item in the inventory."""
    item = input(f"{Colors.OKCYAN}Input the item to view: > {Colors.ENDC}").strip().capitalize()
    count = inventory.count(item)
    if count > 0:
        print(f"{Colors.OKBLUE}You have {count} {item}(s).{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING}You do not have any {item}.{Colors.ENDC}")

def populate_inventory():
    """Populate the inventory with predefined items."""
    initial_items = ["Sword", "Shield", "Potion", "Bow", "Arrow", "Helmet", "Armor"]
    save_inventory(initial_items)
    print(f"{Colors.OKGREEN}Inventory has been populated with initial items.{Colors.ENDC}")

def main():
    """Main program loop."""
    populate_inventory()  # Populate the inventory at the start
    inventory = load_inventory()
    print(f"\n{Colors.HEADER}🌟 RPG Inventory 🌟{Colors.ENDC}")
    while True:
        print(f"{Colors.BOLD}1: Add  2: Remove  3: View  4: Exit{Colors.ENDC}")
        choice = input(f"{Colors.OKCYAN}> {Colors.ENDC}").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            view_item(inventory)
        elif choice == "4":
            print(f"{Colors.OKGREEN}Exiting the program. Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}Invalid choice. Please select 1, 2, 3, or 4.{Colors.ENDC}")

if __name__ == "__main__":
    main()
