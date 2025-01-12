def colorChange(color):
    """
    Returns the ANSI escape code for the given color name.
    """
    colors = {
        "red": "\033[31m",
        "white": "\033[0m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "green": "\033[32m",
        "purple": "\033[35m",
    }
    return colors.get(color, "\033[0m")  # Default to white if color not found

# Title Section
title = (
    f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= "
    f"{colorChange('yellow')}Music App "
    f"{colorChange('blue')}={colorChange('white')}={colorChange('red')}="
)

print(f"        {title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

# Navigation Buttons
prev = "prev"
next = "next"
pause = "pause"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")

# Spacer
print("\n\n")

# Welcome Section
print(f"{colorChange('white')}{'WELCOME TO':^35}")
print(f"{colorChange('blue')}{'--  ARMBOOK  --':^35}")
print(f"{colorChange('yellow')}{'Definitely not a rip off':>35}")
print(f"{colorChange('yellow')}{'a certain other social':>35}")
print(f"{colorChange('yellow')}{'networking site':>35}")
print(f"{colorChange('red')}{'Honest.':^35}")

# User Input Section
username = input(f"{colorChange('white')}{'Username: ':^35}")
password = input(f"{colorChange('white')}{'Password: ':^35}")
