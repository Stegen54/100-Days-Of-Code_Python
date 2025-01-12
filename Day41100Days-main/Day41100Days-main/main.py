# Initializing an empty dictionary with the required keys
website_info = {
    "name": None,
    "URL": None,
    "description": None,
    "rating": None,
}

# Getting all inputs in one line using the split function
print("🌟 Website Rating 🌟")
user_input = input(
    "Enter the website details (name, URL, description, rating out of 5) separated by commas:\n"
)

# Splitting the input and storing in the dictionary
details = user_input.split(",")
keys = list(website_info.keys())

for i in range(len(keys)):
    website_info[keys[i]] = details[i].strip()

# Outputting the entire dictionary
print("\nWebsite Information:")
for key, value in website_info.items():
    print(f"{key.capitalize()}: {value}")
