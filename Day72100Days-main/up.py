import hashlib
import os
from datetime import datetime

from replit import db


# Function to hash passwords with salt
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a new user
def create_user():
    username = input("Create a username: ")
    if username in db:
        print("\nUsername already exists!\n")
        return None, None
    password = input("Create a password: ")
    salt = os.urandom(4).hex()
    hashed_password = hash_password(password, salt)
    db[username] = {"hash": hashed_password, "salt": salt, "entries": []}
    print("\nUser created successfully!\n")
    return username, db[username]

# Function to authenticate user
def authenticate_user():
    username = input("Enter your username: ")
    if username not in db:
        print("\nUser not found!\n")
        return None, None

    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        stored_salt = db[username]["salt"]
        stored_hash = db[username]["hash"]
        if hash_password(password, stored_salt) == stored_hash:
            print("\nLogin successful!\n")
            return username, db[username]
        else:
            attempts -= 1
            print(f"\nIncorrect password! {attempts} attempts remaining.\n")

    print("\nToo many failed attempts. Exiting...\n")
    return None, None

# Function to add a diary entry
def add_entry(user_data):
    entry = input("Type your diary entry: ")
    timestamp = datetime.now()
    user_data["entries"].append({"timestamp": timestamp, "entry": entry})
    db[user_data] = user_data
    print("\nDiary entry added successfully!\n")

# Function to view diary entries
def view_entries(user_data):
    if not user_data["entries"]:
        print("\nNo entries in the diary.\n")
        return

    index = len(user_data["entries"]) - 1
    while index >= 0:
        clear_screen()
        timestamp = user_data["entries"][index]["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        entry = user_data["entries"][index]["entry"]
        print(f"Date: {timestamp}\nEntry: {entry}\n")
        choice = input("Press 'n' for the next previous entry, 'q' to exit: ").lower()
        if choice == 'q':
            break
        elif choice == 'n':
            index -= 1
        else:
            print("\nInvalid input. Try again.")

# Function to view entries from a specific date
def view_from_date(user_data):
    if not user_data["entries"]:
        print("\nNo entries in the diary.\n")
        return

    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_entries = [entry for entry in user_data["entries"] if entry["timestamp"].date() >= filter_date.date()]
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
    if not db.keys():
        username, user_data = create_user()
    else:
        username, user_data = authenticate_user()

    if not username:
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
            add_entry(user_data)
        elif choice == "2":
            view_entries(user_data)
        elif choice == "3":
            view_from_date(user_data)
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()
