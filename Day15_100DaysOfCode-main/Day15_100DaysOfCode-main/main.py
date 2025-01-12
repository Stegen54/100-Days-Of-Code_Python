# 🐾 Animal Sound Challenge - Day 15

# Welcome message to welcom users
print("\033[1;36;40mWelcome to the Animal Sound Challenge! 🎉\n")
print("In this game, you'll get to hear different animal sounds. 🐶🐱🐄")
print("Type the name of an animal and I'll tell you what sound it makes! 😄")
print("If you're ready to start, just type an animal name!\n")
print("To exit, type 'exit' when asked.\n")

# Start a loop that will continue running until the user decides to exit
while True:
    # Ask the user what animal sound they want to hear
    animal = input("What animal do you want to hear?: ").strip().lower()

    # 🐄 Handling specific animal sounds with fun responses
    if animal == "cow":
        print("\033[1;32;40mA cow goes moo! 🐄\033[0m")  # Green text with black background for Cow
    elif animal == "dog":
        print("\033[1;33;40mA dog goes woof! 🐕\033[0m")  # Yellow text with black background for Dog
    elif animal == "cat":
        print("\033[1;34;40mA cat goes meow! 🐱\033[0m")  # Blue text with black background for Cat
    elif animal == "sheep":
        print("\033[1;35;40mA sheep goes baa! 🐑\033[0m")  # Magenta text with black background for Sheep
    elif animal == "duck":
        print("\033[1;36;40mA duck goes quack! 🦆\033[0m")  # Cyan text with black background for Duck
    elif animal == "exit":
        print("\033[1;31;40mGoodbye! 👋\033[0m")  # Red text with black background for exit message
        break
    else:
        # For lesser-known or exotic animals, add a fun response
        print(f"\033[1;37;40mUmmm...the {animal.capitalize()} goes awooga! 🤔\033[0m")

    # Ask if the user wants to exit or continue
    exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()

    # If the user types 'yes', break the loop and end the program
    if exit_choice == "yes":
        print("\033[1;31;40mGoodbye! 👋\033[0m")  # Red text with black background for exit message
        break
