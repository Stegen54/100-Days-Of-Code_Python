# Color codes for terminal
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"

print(CYAN +
      "Ahoy! Welcome to your daily One Piece-inspired affirmation generator!\n" +
      RESET)
name = input("What is your name, brave sailor? ")

# Adding spacing and colorful affirmations
if name == "Luffy" or name == "luffy":
    DOW = input("What is the day of the week? ")
    if DOW == "monday" or DOW == "Monday":
        print("\n" + GREEN + "It’s going to be a legendary Monday, captain",
              name + "!" + RESET + "\n")
    elif DOW == "tuesday" or DOW == "Tuesday":
        print(
            "\n" + YELLOW +
            "Set your sights on adventure, for it's a glorious Tuesday, captain",
            name + "!" + RESET + "\n")
    elif DOW == "wednesday" or DOW == "Wednesday":
        print(
            "\n" + BLUE +
            "The sea's vastness calls to you, never forget your dreams on this Wednesday, captain",
            name + "!" + RESET + "\n")
    elif DOW == "thursday" or DOW == "Thursday":
        print(
            "\n" + CYAN +
            "Your journey’s far from over. Keep sailing forward, captain",
            name + "!" + RESET + "\n")
    elif DOW == "friday" or DOW == "Friday":
        print("\n" + RED + "It’s Friday, captain",
              name + "! The world is yours to conquer!" + RESET + "\n")
    else:
        print(
            "\n" + BOLD +
            "Even the Pirate King rests now and then. Rest up for the journey ahead, captain",
            name + "!" + RESET + "\n")

elif name == "Zoro" or name == "zoro":
    DOW = input("What is the day of the week? ")
    if DOW == "monday" or DOW == "Monday":
        print("\n" + GREEN + "Stay sharp and steady this Monday, swordsman",
              name + ". Your strength is unmatched!" + RESET + "\n")
    elif DOW == "tuesday" or DOW == "Tuesday":
        print(
            "\n" + YELLOW +
            "Never lose sight of your path, even if you get lost, swordsman",
            name + "!" + RESET + "\n")
    elif DOW == "wednesday" or DOW == "Wednesday":
        print(
            "\n" + BLUE +
            "Today is the perfect day to test your mettle, swordsman",
            name + "!" + RESET + "\n")
    elif DOW == "thursday" or DOW == "Thursday":
        print(
            "\n" + CYAN +
            "With each passing day, you are closer to your goal, swordsman",
            name + "!" + RESET + "\n")
    elif DOW == "friday" or DOW == "Friday":
        print(
            "\n" + RED +
            "It’s Friday! Let nothing stand in your way, swordsman",
            name + "!" + RESET + "\n")
    else:
        print(
            "\n" + BOLD +
            "Even the strongest swordsman rests. Take a break, swordsman",
            name + "." + RESET + "\n")

elif name == "Nami" or name == "nami":
    DOW = input("What is the day of the week? ")
    if DOW == "monday" or DOW == "Monday":
        print("\n" + GREEN + "It’s a bright Monday, navigator",
              name + ". Set your course for greatness!" + RESET + "\n")
    elif DOW == "tuesday" or DOW == "Tuesday":
        print(
            "\n" + YELLOW +
            "With your skill, you can navigate any storm, navigator",
            name + "!" + RESET + "\n")
    elif DOW == "wednesday" or DOW == "Wednesday":
        print("\n" + BLUE + "Your dreams are as vast as the sea, navigator",
              name + ". Keep reaching for them!" + RESET + "\n")
    elif DOW == "thursday" or DOW == "Thursday":
        print("\n" + CYAN + "Stay true to your course, navigator",
              name + "! Nothing can stop you!" + RESET + "\n")
    elif DOW == "friday" or DOW == "Friday":
        print("\n" + RED + "It’s Friday, navigator",
              name + "! May the winds be in your favor!" + RESET + "\n")
    else:
        print(
            "\n" + BOLD +
            "Even the best navigator needs a break. Take a rest, navigator",
            name + "." + RESET + "\n")

else:
    print(
        "\n" + BOLD +
        "I may not know your name, but today, be as fearless as the Straw Hat Pirates and as daring as a journey on the Grand Line! Adventure awaits you!"
        + RESET + "\n")
