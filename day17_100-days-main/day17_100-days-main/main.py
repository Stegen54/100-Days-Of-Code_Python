import random

# Options for Rock, Paper, Scissors
options = ["rock", "paper", "scissors"]

# Initialize scores
player1_score = 0
player2_score = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    print("\nScores: Player 1 = {}, Player 2 = {}".format(player1_score, player2_score))

    # Player choices
    player1 = input("Player 1, enter rock, paper, or scissors: ").lower()
    player2 = random.choice(options)  # Simulate Player 2 as a computer

    if player1 not in options:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue  # Restart the round

    print("Player 2 chose:", player2)

    # Determine the winner of the round
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1

    # Check if anyone has won 3 rounds
    if player1_score == 3:
        print("\nPlayer 1 wins the game!")
        break
    elif player2_score == 3:
        print("\nPlayer 2 wins the game!")
        break

# Final scores
print("\nFinal Scores:")
print("Player 1: {}".format(player1_score))
print("Player 2: {}".format(player2_score))
