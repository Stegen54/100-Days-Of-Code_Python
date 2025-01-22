import os
from datetime import datetime

# Password for the diary
correct_password = "mySecret123"
diary_entries = []

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to add a diary entry
def add_entry():
    entry = input("Type your diary entry: ")
    timestamp = datetime.now()
    diary_entries.append({"timestamp": timestamp, "entry": entry})
    print("\nDiary entry added successfully!\n")

# Function to view diary entries
def view_entries():
    if not diary_entries:
        print("\nNo entries in the diary.\n")
        return

    index = len(diary_entries) - 1
    while index >= 0:
        clear_screen()
        timestamp = diary_entries[index]["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        entry = diary_entries[index]["entry"]
        print(f"Date: {timestamp}\nEntry: {entry}\n")
        choice = input("Press 'n' for the next previous entry, 'q' to exit: ").lower()
        if choice == 'q':
            break
        elif choice == 'n':
            index -= 1
        else:
            print("\nInvalid input. Try again.")

# Function to view entries from a specific date
def view_from_date():
    if not diary_entries:
        print("\nNo entries in the diary.\n")
        return

    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_entries = [entry for entry in diary_entries if entry["timestamp"].date() >= filter_date.date()]
        if not filtered_entries:
            print("\nNo entries found from this date.\n")
            return
        for entry in filtered_entries:
            clear_screen()
            timestamp = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"Date: {timestamp}\nEntry: {entry['entry']}\n")
            input("Press Enter to continue...")
    except ValueError:
        print("\nInvalid date format. Try again.\n")

# Main function
def main():
    print("Welcome to Your Private Diary!")
    password_entered = input("Enter your password: ")
    if password_entered != correct_password:
        print("\nIncorrect password. Exiting...\n")
        return

    while True:
        clear_screen()
        print("Diary Menu:")
        print("1. Add a diary entry")
        print("2. View diary entries")
        print("3. View entries from a specific date")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            view_from_date()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()
