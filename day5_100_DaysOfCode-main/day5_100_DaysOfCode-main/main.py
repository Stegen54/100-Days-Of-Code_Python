# Which Anime Character Are You? Game

print("Welcome to 'Which Anime Character Are You?' game!")
print()
print(
    "Answer the following questions to find out which anime character matches your personality."
)
print()

# Initialize variables for scoring
naruto_score = 0
luffy_score = 0
goku_score = 0
eren_score = 0

# Question 1
print("Question 1: What's your goal in life?")
print("A. To become stronger and protect my friends and family")
print("B. To be free and explore the world")
print("C. To push my limits and become the strongest")
print("D. To fight for freedom and justice")
answer1 = input("Choose A, B, C, or D: ").upper()

if answer1 == "A":
    naruto_score += 1
elif answer1 == "B":
    luffy_score += 1
elif answer1 == "C":
    goku_score += 1
elif answer1 == "D":
    eren_score += 1

# Question 2
print("\nQuestion 2: What's your best trait?")
print("A. Loyalty")
print("B. Adventurous")
print("C. Determination")
print("D. Fearlessness")
answer2 = input("Choose A, B, C, or D: ").upper()

if answer2 == "A":
    naruto_score += 1
elif answer2 == "B":
    luffy_score += 1
elif answer2 == "C":
    goku_score += 1
elif answer2 == "D":
    eren_score += 1

# Question 3
print("\nQuestion 3: How do you handle a tough situation?")
print("A. I face it head-on with determination")
print("B. I rely on my friends and teamwork")
print("C. I keep my cool and use my strength to overcome it")
print("D. I analyze and try to find a strategic way out")
answer3 = input("Choose A, B, C, or D: ").upper()

if answer3 == "A":
    naruto_score += 1
elif answer3 == "B":
    luffy_score += 1
elif answer3 == "C":
    goku_score += 1
elif answer3 == "D":
    eren_score += 1

# Question 4
print("\nQuestion 4: What's your favorite thing to do in your free time?")
print("A. Training to become stronger")
print("B. Eating or hanging out with friends")
print("C. Going on an adventure")
print("D. Planning my next move")
answer4 = input("Choose A, B, C, or D: ").upper()

if answer4 == "A":
    goku_score += 1
elif answer4 == "B":
    naruto_score += 1
elif answer4 == "C":
    luffy_score += 1
elif answer4 == "D":
    eren_score += 1

# Calculate Results
print("\nCalculating your result...\n")

if naruto_score >= max(luffy_score, goku_score, eren_score):
    print(
        "You're most like Naruto Uzumaki! You are loyal, determined, and always fight for your friends!"
    )
elif luffy_score >= max(naruto_score, goku_score, eren_score):
    print(
        "You're most like Monkey D. Luffy! You are adventurous, carefree, and love exploring the world with your friends."
    )
elif goku_score >= max(naruto_score, luffy_score, eren_score):
    print(
        "You're most like Goku! You are always striving to become stronger and never back down from a challenge."
    )
elif eren_score >= max(naruto_score, luffy_score, goku_score):
    print(
        "You're most like Eren Yeager! You are fearless, strategic, and always willing to fight for justice and freedom."
    )
else:
    print(
        "You have a unique personality that blends elements from multiple characters!"
    )
