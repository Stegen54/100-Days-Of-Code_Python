import requests, json

result = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})

data = json.loads(result.text)
print(data['joke'])



def get_joke():
    result = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    data = json.loads(result.text)
    return data['joke']

def save_joke(joke, filename="saved_jokes.txt"):
    with open(filename, 'a') as f:
        f.write(joke + '\n')
    print("Joke saved!")

def load_jokes(filename="saved_jokes.txt"):
    try:
        with open(filename, 'r') as f:
            jokes = f.readlines()
        return [joke.strip() for joke in jokes]
    except FileNotFoundError:
        return []

while True:
    print("\nOptions:")
    print("1. Get a new joke")
    print("2. Save the current joke")
    print("3. Load saved jokes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        joke = get_joke()
        print(joke)
        current_joke = joke  # Store the current joke
    elif choice == '2':
        try:
            save_joke(current_joke)
        except NameError:
            print("No joke to save. Get a joke first.")
    elif choice == '3':
        saved_jokes = load_jokes()
        if saved_jokes:
            print("\nSaved Jokes:")
            for i, joke in enumerate(saved_jokes):
                print(f"{i+1}. {joke}")
        else:
            print("No jokes saved yet.")
    elif choice == '4':
        break
    else:
        print("\033[91mInvalid choice. Please try again.\033[0m")  # Red color for error message