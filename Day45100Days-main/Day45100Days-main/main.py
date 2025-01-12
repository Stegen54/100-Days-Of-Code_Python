import os
import time

todo = []

def clear_console():
    """Clear the console for better UX."""
    os.system("cls" if os.name == "nt" else "clear")

def add():
    clear_console()
    print("Add a new To-Do")
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority (High, Medium, Low) > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Task added successfully!")
    time.sleep(1)

def view():
    clear_console()
    if not todo:
        print("No to-dos available.\n")
        time.sleep(1)
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
    time.sleep(1)

def edit():
    clear_console()
    if not todo:
        print("No to-dos available to edit.\n")
        time.sleep(1)
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
            priority = input("New Priority (High, Medium, Low) > ").capitalize()
            todo.append([name, date, priority])
            print("Task updated successfully!")
            break
    if not found:
        print("Task not found.")
    time.sleep(1)

def remove():
    clear_console()
    if not todo:
        print("No to-dos available to remove.\n")
        time.sleep(1)
        return

    print("Remove a To-Do")
    find = input("Name of to-do to remove > ")
    found = False
    for row in todo:
        if find == row[0]:
            todo.remove(row)
            found = True
            print(f"Task '{find}' removed successfully!")
            break
    if not found:
        print("Task not found.")
    time.sleep(1)

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
        time.sleep(1)
