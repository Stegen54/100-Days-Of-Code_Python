# 🌟 Contact Card 🌟

# Create an empty dictionary to store the contact details
contact_card = {}

# Gather user input for the contact details
contact_card["name"] = input("Input your name > ").strip()
contact_card["date_of_birth"] = input("Input your date of birth > ").strip()
contact_card["telephone"] = input("Input your telephone number > ").strip()
contact_card["email"] = input("Input your email > ").strip()
contact_card["address"] = input("Input your address > ").strip()

# Print out the details in a nice format
print("\n🌟 Contact Card 🌟")
print(f"Hi {contact_card['name']}.")
print(
    f"Our dictionary says that you were born on {contact_card['date_of_birth']}, "
    f"we can call you on {contact_card['telephone']}, "
    f"email {contact_card['email']}, "
    f"or write to {contact_card['address']}."
)
