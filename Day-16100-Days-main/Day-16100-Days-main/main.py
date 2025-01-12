print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1  # Keeps track of attempts

while True:
    # Prompt the user to guess the missing word
    lyrics = input("We don't talk about ______. ").strip()
    # Check if the user guessed correctly
    if lyrics.lower() == "bruno":
        print("You got it!")
        break
    else:
        print("Nope! Try again!")
        counter += 1

print("Thanks for playing!")
print("You got the correct lyrics in", counter, "attempt(s).")
