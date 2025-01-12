import random

# Define the initial cards
cards = {
    "Naruto Uzumaki": {"Intelligence": 70, "Handsomeness": 85, "L33t c0ding skillz": 50, "Baldness level": 0},
    "Sasuke Uchiha": {"Intelligence": 90, "Handsomeness": 95, "L33t c0ding skillz": 80, "Baldness level": 0}
}

def add_card(name, stats):
    cards[name] = stats

def play_game():
    while True:
        print("\n🌟Top Trumps🌟")
        print("Welcome to the Top Trumps 'Most Handsome Anime Characters' Simulator")
        print("Choose your card: 1 - Naruto Uzumaki  2 - Sasuke Uchiha")
        choice = input("> ")
        if choice == "1":
            chosen_card = "Naruto Uzumaki"
        elif choice == "2":
            chosen_card = "Sasuke Uchiha"
        else:
            print("Invalid choice. Try again.")
            continue

        print("Choose your stat:")
        print("1. Intelligence")
        print("2. Handsomeness")
        print("3. L33t c0ding skillz")
        print("4. Baldness level")
        stat_choice = input("> ")
        if stat_choice == "1":
            stat = "Intelligence"
        elif stat_choice == "2":
            stat = "Handsomeness"
        elif stat_choice == "3":
            stat = "L33t c0ding skillz"
        elif stat_choice == "4":
            stat = "Baldness level"
        else:
            print("Invalid choice. Try again.")
            continue

        opponent_card = "Sasuke Uchiha" if chosen_card == "Naruto Uzumaki" else "Naruto Uzumaki"
        print(f"{chosen_card} has a {stat} stat of {cards[chosen_card][stat]}")
        print(f"{opponent_card} has a {stat} stat of {cards[opponent_card][stat]}")

        if cards[chosen_card][stat] > cards[opponent_card][stat]:
            print(f"************* {chosen_card} wins! ********")
        elif cards[chosen_card][stat] < cards[opponent_card][stat]:
            print(f"************* {opponent_card} wins! ********")
        else:
            print("************* It's a tie! ********")

        again = input("Again? y/n > ")
        if again.lower() != "y":
            break

# Example of adding a new card
add_card("Goku", {"Intelligence": 60, "Handsomeness": 90, "L33t c0ding skillz": 70, "Baldness level": 0})

# Start the game
play_game()
