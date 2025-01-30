import hashlib
import os
from replit import db

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def add_user():
    username = input("Username: > ")
    if username in db:
        print("User already exists!")
        return
    password = input("Password: > ")
    salt = str(os.urandom(4).hex())  # Generate a random 4-byte salt
    hashed_password = hash_password(password, salt)
    db[username] = {"hash": hashed_password, "salt": salt}
    print("Details stored.")

def login():
    username = input("Username: > ")
    if username not in db:
        print("User not found!")
        return
    password = input("Password: > ")
    stored_salt = db[username]["salt"]
    stored_hash = db[username]["hash"]
    if hash_password(password, stored_salt) == stored_hash:
        print("Login successful")
    else:
        print("Incorrect password!")

def main():
    while True:
        print("\n🌟Login System🌟")
        choice = input("1: Add User, 2: Login, 3: Exit > ")
        if choice == "1":
            add_user()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
