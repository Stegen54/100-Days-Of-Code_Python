print("100 Days of Code QUIZ")
print()

# Fixing missing quotation mark in the string
print("How many can you answer correctly?")

# Fixing variable assignment and using input for first question
ans1 = input("What language are we writing in? ").lower()  # Taking input to allow flexibility in answers

# Checking the answer for question 1
if ans1 == "python":
    print("Correct")
else:
    print("Nope🙈")

# Fixing input statement for second question
ans2 = int(input("Which lesson number is this? "))  # Converting input to integer

# Fixing conditionals and handling the answers correctly
if ans2 > 12:
    print("We're not quite that far yet")
elif ans2 < 12:
    print("We've gone well past that!")
else:
    print("That's right!")


