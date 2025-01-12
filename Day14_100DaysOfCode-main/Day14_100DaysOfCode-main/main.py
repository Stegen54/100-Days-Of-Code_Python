from getpass import getpass as input

# Welcome message
print("🎮 Welcome to the Ultimate Rock, Paper, Scissors Battle! 🎮")
print("Player 1 and Player 2, get ready to fight! 💥💥")
print(
    "Each player will choose: R for Rock 🪨, P for Paper 📄, or S for Scissors ✂️"
)
print("Let's see who will emerge victorious! 💪👑\n")

# Player 1 Input
player_1 = input("Player 1, make your choice (R, P, or S): ").upper()
# Player 2 Input
player_2 = input("Player 2, make your choice (R, P, or S): ").upper()

# Check if the players made valid choices
valid_choices = ['R', 'P', 'S']
if player_1 not in valid_choices or player_2 not in valid_choices:
    print("❌ Invalid choice! Please use only R, P, or S. ❌")
else:
    # Display the choices
    print(f"\nPlayer 1 chose: {player_1}")
    print(f"Player 2 chose: {player_2}\n")

    # Determine the winner
    if player_1 == player_2:
        print("It's a tie! 😱 Both chose the same!")
    elif (player_1 == 'R' and player_2 == 'S') or (
            player_1 == 'P' and player_2 == 'R') or (player_1 == 'S'
                                                     and player_2 == 'P'):
        print("Player 1 wins! 🎉🎉 Rock, Paper, Scissors Master! 🏆")
    else:
        print("Player 2 wins! 🎉🎉 You are the Ultimate Fighter! 🏆")

# Closing message
print("\nThanks for playing! Hope you had a blast! 💥💥")
