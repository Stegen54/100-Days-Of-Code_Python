import datetime
import os

# Initialize a database to store tweets as a dictionary
database = {}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_tweet():
    """Prompt the user to input a tweet and store it in the database."""
    tweet = input("Enter your tweet: ")
    if tweet:
        timestamp = datetime.datetime.now()
        database[timestamp] = tweet
        print("Tweet added successfully!\n")
    else:
        print("Tweet cannot be empty.\n")

def view_tweets():
    """Display tweets in reverse chronological order, 10 at a time."""
    if not database:
        print("No tweets to display.\n")
        return

    sorted_tweets = sorted(database.items(), key=lambda x: x[0], reverse=True)
    total_tweets = len(sorted_tweets)
    start_index = 0

    while start_index < total_tweets:
        clear_console()
        print("Your Tweets (Most Recent First):\n")
        for i in range(start_index, min(start_index + 10, total_tweets)):
            timestamp, tweet = sorted_tweets[i]
            print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {tweet}")

        start_index += 10
        if start_index < total_tweets:
            more = input("\nShow next 10 tweets? (yes or no): ").strip().lower()
            if more != 'yes':
                break
        else:
            print("\nEnd of tweets.")


def main_menu():
    """Main menu to navigate the program."""
    while True:
        print("\nWelcome to Twitter for One!")
        print("1. Add a tweet")
        print("2. View tweets")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            add_tweet()
        elif choice == '2':
            view_tweets()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
