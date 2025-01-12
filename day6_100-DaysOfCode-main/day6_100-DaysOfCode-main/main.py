# Login system with hardcoded users and personalized messages

print("Welcome to my personalized login system!")

# Asks for username
username = input("Enter your username: ")

if username == "Stegen":
    # Ask for password
    password = input("Enter your password: ")
    if password == "goalkeeper1":
        print("\nLogin successful!")
        print("Welcome back, Stegen! Ready to guard the net? 🧤⚽")
    else:
        print("\nIncorrect password for Stegen!")

elif username == "Pique":
    password = input("Enter your password: ")
    if password == "defender3":
        print("\nLogin successful!")
        print("Hola, Pique! The defense wall is strong with you! 🛡️")
    else:
        print("\nIncorrect password for Pique!")

elif username == "Dennis":
    password = input("Enter your password: ")
    if password == "genius4":
        print("\nLogin successful!")
        print("Hello, Dennis! Ready to tackle today's challenges? 🧠💻")
    else:
        print("\nIncorrect password for Dennis!")

elif username == "Darkhorse":
    password = input("Enter your password: ")
    if password == "mystic7":
        print("\nLogin successful!")
        print("Ah, Darkhorse, the enigma returns! 🌌🐎")
    else:
        print("\nIncorrect password for Darkhorse!")

elif username == "Luffy":
    password = input("Enter your password: ")
    if password == "pirate5":
        print("\nLogin successful!")
        print("Yo ho ho, Luffy! Time to conquer the seas! 🏴‍☠️🍖")
    else:
        print("\nIncorrect password for Luffy!")

else:
    print("\nUsername not found. Are you sure you're registered?")
