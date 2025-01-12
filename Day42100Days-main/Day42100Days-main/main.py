# 👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾

# ANSI color codes for different beast types
colors = {
    "fire": "\033[31m",  # Red
    "water": "\033[34m",  # Blue
    "air": "\033[37m",  # White
    "earth": "\033[32m",  # Green
    "spirit": "\033[35m",  # Magenta
    "default": "\033[0m"  # Reset
}

# Welcome message
print(
    "\033[33m👾 Welcome to MokéBeast - The Non-Copyright Generic Beast Battle Game! 👾\033[0m"
)
print("Prepare to create your very own MokéBeast!")

# Input prompt
print(
    "Enter your beast's details in the format: name,type,special move,starting HP,starting MP"
)

# Error handling for input
try:
    user_input = input(
        "> ").strip()  # Strip to remove leading/trailing whitespace
    # Parse inputs using split
    details = user_input.split(
        ",")  # Use split(",") to handle input without spaces

    # Debug: Log what details are received
    # print("\033[36mDEBUG: Details parsed:", details, "\033[0m")

    # Check if the correct number of inputs is provided
    if len(details) != 5:
        raise ValueError(
            f"You must provide exactly 5 details separated by commas. You provided {len(details)}."
        )

    # Unpack the details
    name, beast_type, special_move, starting_hp, starting_mp = [
        item.strip() for item in details
    ]  # Strip extra spaces

    # Validate beast type
    valid_types = {"fire", "water", "air", "earth", "spirit"}
    if beast_type.lower() not in valid_types:
        raise ValueError(
            f"Invalid beast type: {beast_type}. Valid types are {', '.join(valid_types)}."
        )

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

    # Get the color for the beast's type
    color = colors.get(mokebeast["type"], colors["default"])

    # Display the beast's details in the appropriate color
    print(
        color +
        f"Your beast is called {mokebeast['name']}. It is a {mokebeast['type']} beast with a special move of {mokebeast['special_move']}."
        +
        f"\nStarting HP: {mokebeast['starting_hp']}, Starting MP: {mokebeast['starting_mp']}"
        + colors["default"])

except ValueError as ve:
    print(f"\033[31mError: {ve}\033[0m")  # Display error message in red
except Exception as e:
    print(f"\033[31mAn unexpected error occurred: {e}\033[0m")
