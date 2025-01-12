import os
import time
from colorama import Fore, Style

# Initialize the to-do list
todo_list = []


# Subroutine to display the to-do list
def display_todo_list():
    print(Fore.CYAN + "\nYour To-Do List:" + Style.RESET_ALL)
    if not todo_list:
        print(Fore.YELLOW + "  (Your to-do list is empty!)" + Style.RESET_ALL)
    else:
        for i, item in enumerate(todo_list, start=1):
            print(Fore.GREEN + f"  {i}. {item}" + Style.RESET_ALL)
    print()


# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main program loop
while True:
    clear_console()
    print(Fore.MAGENTA + "\n✨ To-Do List Manager ✨" + Style.RESET_ALL)
    print(Fore.BLUE + "What would you like to do?" + Style.RESET_ALL)
    print("  1. View your to-do list")
    print("  2. Add an item to your to-do list")
    print("  3. Remove an item from your to-do list")
    print("  4. Exit")

    choice = input(Fore.YELLOW + "\nEnter your choice (1-4): " +
                   Style.RESET_ALL)

    if choice == "1":
        # View the to-do list
        display_todo_list()
        input(Fore.YELLOW + "\nPress Enter to return to the menu..." +
              Style.RESET_ALL)

    elif choice == "2":
        # Add an item to the to-do list
        new_item = input(Fore.YELLOW + "\nEnter the item you want to add: " +
                         Style.RESET_ALL)
        todo_list.append(new_item)
        print(Fore.GREEN +
              f"\n'{new_item}' has been added to your to-do list!" +
              Style.RESET_ALL)
        time.sleep(1)

    elif choice == "3":
        # Remove an item from the to-do list
        display_todo_list()
        try:
            item_number = int(
                input(Fore.YELLOW +
                      "\nEnter the number of the item you completed: " +
                      Style.RESET_ALL))
            if 1 <= item_number <= len(todo_list):
                removed_item = todo_list.pop(item_number - 1)
                print(
                    Fore.GREEN +
                    f"\n'{removed_item}' has been removed from your to-do list!"
                    + Style.RESET_ALL)
            else:
                print(Fore.RED + "\nInvalid number. Please try again." +
                      Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "\nPlease enter a valid number." +
                  Style.RESET_ALL)
        time.sleep(1)

    elif choice == "4":
        # Exit the program
        print(Fore.CYAN +
              "\nThank you for using the To-Do List Manager. Goodbye!" +
              Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "\nInvalid choice. Please select a valid option." +
              Style.RESET_ALL)
        time.sleep(1)
