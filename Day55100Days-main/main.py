import json
import os
import random
import string
import time

todo = []

# Path for the main file and backup folder
main_file = "todos.txt"
backup_folder = "backup"
fileExists = False


def clear_console():
    """Clear the console for better UX."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_random_filename(extension=".txt"):
    """Generate a random filename."""
    random_string = ''.join(
        random.choices(string.ascii_letters + string.digits, k=8))
    return random_string + extension


def create_backup():
    """Create a backup of the to-do list file."""
    global fileExists
    if not fileExists:
        # Create the backup folder if it doesn't exist
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
            print(f"Backup folder '{backup_folder}' created!")

        # Generate a random filename and save the backup
        backup_filename = generate_random_filename()
        backup_path = os.path.join(backup_folder, backup_filename)
        with open(backup_path, "w") as file:
            json.dump(todo, file)
        fileExists = True
        print(f"Backup saved as '{backup_path}'!")


def save_to_file():
    """Save the to-do list to the main file."""
    create_backup()  # Create a backup before saving
    with open(main_file, "w") as file:
        json.dump(todo, file)
    print(f"Main file '{main_file}' saved!")


def load_from_file():
    """Load the to-do list from the main file."""
    global todo
    if os.path.exists(main_file):
        with open(main_file, "r") as file:
            todo = json.load(file)


def add():
    clear_console()
    print("Add a new To-Do")
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority (High, Medium, Low) > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    save_to_file()
    print("Task added successfully!")
    time.sleep(5)


def view():
    clear_console()
    if not todo:
        print("No to-dos available.\n")
        time.sleep(5)
        return

    print("View To-Dos")
    options = input("1: View All\n2: View by Priority\n> ")
    clear_console()
    if options == "1":
        print("# | Name | Due Date | Priority")
        for idx, row in enumerate(todo, 1):
            print(f"{idx} | {row[0]} | {row[1]} | {row[2]}")
        print()
    elif options == "2":
        priority = input("Which priority? (High, Medium, Low) > ").capitalize()
        filtered = [row for row in todo if row[2] == priority]
        if not filtered:
            print(f"No tasks found with priority: {priority}\n")
        else:
            print("# | Name | Due Date | Priority")
            for idx, row in enumerate(filtered, 1):
                print(f"{idx} | {row[0]} | {row[1]} | {row[2]}")
        print()
    else:
        print("Invalid option.")
    time.sleep(5)


def edit():
    clear_console()
    if not todo:
        print("No to-dos available to edit.\n")
        time.sleep(5)
        return

    print("Edit a To-Do")
    find = input("Name of to-do to edit > ")
    found = False
    for row in todo:
        if find == row[0]:
            found = True
            todo.remove(row)
            print(f"Editing '{find}'")
            name = input("New Name > ")
            date = input("New Due Date > ")
            priority = input(
                "New Priority (High, Medium, Low) > ").capitalize()
            todo.append([name, date, priority])
            save_to_file()
            print("Task updated successfully!")
            break
    if not found:
        print("Task not found.")
    time.sleep(5)


def remove():
    clear_console()
    if not todo:
        print("No to-dos available to remove.\n")
        time.sleep(5)
        return

    print("Remove a To-Do")
    find = input("Name of to-do to remove > ")
    found = False
    for row in todo:
        if find == row[0]:
            todo.remove(row)
            found = True
            save_to_file()
            print(f"Task '{find}' removed successfully!")
            break
    if not found:
        print("Task not found.")
    time.sleep(5)


# Load existing to-dos from the file at the start
load_from_file()

while True:
    clear_console()
    print("🌟 To-Do Manager 🌟")
    print("1: Add To-Do")
    print("2: View To-Dos")
    print("3: Edit To-Do")
    print("4: Remove To-Do")
    print("5: Quit")
    menu = input("> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()
    elif menu == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
        time.sleep(5)
