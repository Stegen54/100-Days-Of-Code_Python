# Define the number of seconds in a minute, minutes in an hour, etc.
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_normal_year = 365
days_in_leap_year = 366

# Calculate seconds in a normal year
seconds_in_normal_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_normal_year


# Calculate seconds in a leap year
seconds_in_leap_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_leap_year

# Ask the user if it's a leap year
is_leap_year = input("Is it a leap year? (yes/no): ").strip().lower()

# Determine the number of seconds based on whether it's a leap year
if is_leap_year == "yes":
    print(f"There are {seconds_in_leap_year} seconds in a leap year.")
else:
    print(f"There are {seconds_in_normal_year} seconds in a normal year.")

