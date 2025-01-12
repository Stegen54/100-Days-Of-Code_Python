# 👾 MokéBeast Mokédex - Day 46 Challenge 👾

# ANSI color codes for different beast types
colors = {
    "fire": "\033[31m",  # Red
    "water": "\033[34m",  # Blue
    "air": "\033[37m",  # White
    "earth": "\033[32m",  # Green
    "spirit": "\033[35m",  # Magenta
    "default": "\033[0m"  # Reset
}

def prettyPrint(mokédex):
    """Print the Mokédex in a formatted style."""
    print("\n🌟 Full Mokédex 🌟")
    for idx, beast in enumerate(mokédex, 1):
        print(f"{idx}. name: {beast['name']:<15} | element: {beast['type']:<10} | "
              f"special move: {beast['special_move']:<15} | HP: {beast['starting_hp']} | MP: {beast['starting_mp']}")

# Welcome message
print("\033[33m👾 Welcome to the MokéBeast Mokédex Challenge! 👾\033[0m")

# List to store multiple MokéBeasts
mokédex = []

while True:
    # Input prompt for the user
    print("\nInput your beast's details in the format: name,type,special move,starting HP,starting MP")

    try:
        user_input = input("> ").strip()  # Strip to remove leading/trailing whitespace
        details = user_input.split(",")  # Parse input into a list

        # Validate the number of inputs
        if len(details) != 5:
            raise ValueError(
                f"You must provide exactly 5 details separated by commas. You provided {len(details)}."
            )

        # Unpack and clean the details
        name, beast_type, special_move, starting_hp, starting_mp = [item.strip() for item in details]

        # Validate beast type
        valid_types = {"fire", "water", "air", "earth", "spirit"}
        if beast_type.lower() not in valid_types:
            raise ValueError(f"Invalid beast type: {beast_type}. Valid types are {', '.join(valid_types)}.")

        # Validate HP and MP as integers
        starting_hp = int(starting_hp)
        starting_mp = int(starting_mp)

        # Create the beast dictionary
        mokebeast = {
            "name": name,
            "type": beast_type.lower(),
            "special_move": special_move,
            "starting_hp": starting_hp,
            "starting_mp": starting_mp
        }

        # Add the beast to the Mokédex
        mokédex.append(mokebeast)

        # Show confirmation with color
        color = colors.get(mokebeast["type"], colors["default"])
        print(color + f"Added {mokebeast['name']} to your Mokédex!" + colors["default"])

    except ValueError as ve:
        print(f"\033[31mError: {ve}\033[0m")  # Display error message in red
    except Exception as e:
        print(f"\033[31mAn unexpected error occurred: {e}\033[0m")

    # Ask if the user wants to add another beast
    again = input("Again? y/n > ").strip().lower()
    if again != 'y':
        break

# Output the full Mokédex
prettyPrint(mokédex)
