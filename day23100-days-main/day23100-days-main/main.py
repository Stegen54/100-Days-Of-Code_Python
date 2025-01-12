def login():
  # Define correct username and password
  correct_username = "onyeali54"
  correct_password = "whatAmazingHairYouHave"

  while True:  # Infinite loop to keep prompting the user until they log in successfully
      # Prompt the user for their username and password
      username = input("What is your username?: ")
      password = input("What is your password?: ")

      # Check if the username and password are correct
      if username == correct_username and password == correct_password:
          print("Welcome to Replit!")
          break  # Exit the loop when the correct details are provided
      else:
          print("Whoops! I don't recognize that username or password. Try again!")

# Call the login subroutine
login()
