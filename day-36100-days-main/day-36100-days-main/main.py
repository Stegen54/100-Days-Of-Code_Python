# Start with a blank list to store names
names_list = []

def add_name():
    while True:
        # Ask for first and last name separately
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()

        # Capitalize the first and last name
        tidy_first_name = first_name.capitalize()
        tidy_last_name = last_name.capitalize()

        # Combine into a full name using f-strings
        full_name = f"{tidy_first_name} {tidy_last_name}"

        # Check for duplicates and add to the list if it's new
        if full_name not in names_list:
            names_list.append(full_name)
            print("Updated list of names:", names_list)
        else:
            print(f"{full_name} is already in the list. Try again!")

# Run the subroutine
add_name()
