import os
import time
from colorama import Fore, Style

# Initialize the to-do list
todo_list = []


def manage_todo_list():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + "\n✨ To-Do List Manager ✨" + Style.RESET_ALL)
        print(Fore.BLUE + "What would you like to do?" + Style.RESET_ALL)
        print("  1. View your to-do list")
        print("  2. Add an item to your to-do list")
        print("  3. Remove an item from your to-do list")
        print("  4. Edit an item in your to-do list")
        print("  5. Erase the entire to-do list")
        print("  6. Exit")

        choice = input(Fore.YELLOW + "\nEnter your choice (1-6): " +
                       Style.RESET_ALL)

        if choice == "1":
            print(Fore.CYAN + "\nYour To-Do List:" + Style.RESET_ALL)
            if not todo_list:
                print(Fore.YELLOW + "  (Your to-do list is empty!)" +
                      Style.RESET_ALL)
            else:
                for i, item in enumerate(todo_list, start=1):
                    print(Fore.GREEN + f"  {i}. {item}" + Style.RESET_ALL)
            input(Fore.YELLOW + "\nPress Enter to return to the menu..." +
                  Style.RESET_ALL)

        elif choice == "2":
            new_item = input(Fore.YELLOW +
                             "\nEnter the item you want to add: " +
                             Style.RESET_ALL).strip()
            if new_item in todo_list:
                print(Fore.RED +
                      f"\n'{new_item}' is already in your to-do list." +
                      Style.RESET_ALL)
            else:
                todo_list.append(new_item)
                print(Fore.GREEN +
                      f"\n'{new_item}' has been added to your to-do list!" +
                      Style.RESET_ALL)
            time.sleep(1)

        elif choice == "3":
            print(Fore.CYAN + "\nYour To-Do List:" + Style.RESET_ALL)
            if not todo_list:
                print(Fore.YELLOW + "  (Your to-do list is empty!)" +
                      Style.RESET_ALL)
            else:
                for i, item in enumerate(todo_list, start=1):
                    print(Fore.GREEN + f"  {i}. {item}" + Style.RESET_ALL)
                try:
                    item_number = int(
                        input(
                            Fore.YELLOW +
                            "\nEnter the number of the item you want to remove: "
                            + Style.RESET_ALL))
                    if 1 <= item_number <= len(todo_list):
                        item_to_remove = todo_list[item_number - 1]
                        confirm = input(
                            Fore.RED +
                            f"\nAre you sure you want to remove '{item_to_remove}'? (yes/no): "
                            + Style.RESET_ALL).strip().lower()
                        if confirm == 'yes':
                            todo_list.pop(item_number - 1)
                            print(
                                Fore.GREEN +
                                f"\n'{item_to_remove}' has been removed from your to-do list."
                                + Style.RESET_ALL)
                        else:
                            print(Fore.YELLOW + "\nNo changes made." +
                                  Style.RESET_ALL)
                    else:
                        print(Fore.RED +
                              "\nInvalid number. Please try again." +
                              Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "\nPlease enter a valid number." +
                          Style.RESET_ALL)
            time.sleep(1)

        elif choice == "4":
            print(Fore.CYAN + "\nYour To-Do List:" + Style.RESET_ALL)
            if not todo_list:
                print(Fore.YELLOW + "  (Your to-do list is empty!)" +
                      Style.RESET_ALL)
            else:
                for i, item in enumerate(todo_list, start=1):
                    print(Fore.GREEN + f"  {i}. {item}" + Style.RESET_ALL)
                try:
                    item_number = int(
                        input(
                            Fore.YELLOW +
                            "\nEnter the number of the item you want to edit: "
                            + Style.RESET_ALL))
                    if 1 <= item_number <= len(todo_list):
                        new_text = input(
                            Fore.YELLOW +
                            "\nEnter the new text for the item: " +
                            Style.RESET_ALL).strip()
                        todo_list[item_number - 1] = new_text
                        print(
                            Fore.GREEN +
                            f"\nItem {item_number} has been updated to '{new_text}'."
                            + Style.RESET_ALL)
                    else:
                        print(Fore.RED +
                              "\nInvalid number. Please try again." +
                              Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "\nPlease enter a valid number." +
                          Style.RESET_ALL)
            time.sleep(1)

        elif choice == "5":
            confirm = input(
                Fore.RED +
                "\nAre you sure you want to erase the entire to-do list? (yes/no): "
                + Style.RESET_ALL).strip().lower()
            if confirm == 'yes':
                todo_list.clear()
                print(Fore.GREEN + "\nThe to-do list has been erased." +
                      Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "\nNo changes made." + Style.RESET_ALL)
            time.sleep(1)

        elif choice == "6":
            print(Fore.CYAN +
                  "\nThank you for using the To-Do List Manager. Goodbye!" +
                  Style.RESET_ALL)
            break

        else:
            print(Fore.RED +
                  "\nInvalid choice. Please select a valid option." +
                  Style.RESET_ALL)
            time.sleep(1)


manage_todo_list()
