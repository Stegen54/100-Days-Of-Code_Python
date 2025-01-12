import os
import time

listOfEmail = []

def prettyPrint():
    os.system("clear")
    print("listOfEmail")
    print()
    counter = 1
    for email in listOfEmail:
        print(f"{counter}: {email}")
        counter += 1
    time.sleep(1)

def sendSpam():
    for i in range(min(10, len(listOfEmail))):  # Limit to the first 10 emails
        os.system("clear")
        email = listOfEmail[i]
        print(f"""
Dear {email},

It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
""")
        time.sleep(2)  # Pause for 2 seconds
        os.system("clear")

while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2. Remove email\n3. Show emails\n4. Get SPAMMING\n> ")

    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)

    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
        else:
            print("Email not found.")
            time.sleep(1)

    elif menu == "3":
        prettyPrint()

    elif menu == "4":
        if not listOfEmail:
            print("No emails to spam!")
            time.sleep(1)
        else:
            sendSpam()

    else:
        print("Invalid option. Try again.")
        time.sleep(1)

    os.system("clear")
