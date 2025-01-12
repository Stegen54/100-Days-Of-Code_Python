from colorama import Fore, Style, init
# Initialize colorama for color formatting
init(autoreset=True)

print(Fore.YELLOW + Style.BRIGHT + "\nWelcome to the One Piece Fan Finder!")
print("Let's see if you're a real fan of the Pirate King's adventure!\n")

# Question 1
answer1 = input(
    Fore.CYAN +
    "First question: What is the name of Luffy's ship? ").strip().lower()
if answer1 == "going merry" or answer1 == "thousand sunny":
    print(Fore.GREEN + "\nCorrect! You know your ships!\n")

    # Question 2
    answer2 = input(Fore.CYAN +
                    "Who trained Zoro in swordsmanship? ").strip().lower()
    if answer2 == "mihawk" or answer2 == "dracule mihawk":
        print(Fore.GREEN + "\nNice! You know Zoro’s master!\n")

        # Question 3
        answer3 = input(Fore.CYAN +
                        "Which Devil Fruit did Luffy eat? ").strip().lower()
        if answer3 == "gum-gum fruit" or answer3 == "gomu gomu no mi":
            print(Fore.GREEN + "\nImpressive! You know your Devil Fruits!\n")

            # Question 4
            answer4 = input(Fore.CYAN +
                            "Who is the navigator of the Straw Hat Pirates? "
                            ).strip().lower()
            if answer4 == "nami":
                print(Fore.GREEN +
                      "\nGood going! You know the Straw Hat crew!\n")

                # Question 5
                answer5 = input(
                    Fore.CYAN +
                    "What's the bounty on Luffy's head after the Dressrosa arc? "
                ).strip()
                if answer5 == "500 million" or answer5 == "500,000,000":
                    print(Fore.GREEN +
                          "\nWell done! You know Luffy's bounty!\n")

                    # Question 6
                    answer6 = input(
                        Fore.CYAN +
                        "Final question: Where did Luffy meet Sanji? ").strip(
                        ).lower()
                    if answer6 == "baratie":
                        print(Fore.YELLOW + Style.BRIGHT +
                              "\nCongratulations! You're a real fan! 🏴‍☠️")
                    else:
                        print(
                            Fore.RED +
                            "\nFake fan alert! Real fans know where Sanji joined!\n"
                        )
                else:
                    print(
                        Fore.RED +
                        "\nOof! Real fans know Luffy's bounty like the back of their hand!\n"
                    )
            else:
                print(Fore.RED +
                      "\nCome on! Any fan knows the Straw Hat navigator.\n")
        else:
            print(
                Fore.RED +
                "\nHmm, seems like you don't know who trained Zoro. Fake fan spotted!\n"
            )
    else:
        print(
            Fore.RED +
            "\nGoing Merry and Thousand Sunny are the only ships for Luffy. Fake fan!\n"
        )
else:
    print(
        Fore.RED +
        "\nGoing Merry and Thousand Sunny are the only ships for Luffy. Fake fan!\n"
    )
