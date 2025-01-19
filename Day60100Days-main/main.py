from datetime import datetime

# Display a welcome message
print("🌟 Event Countdown Timer 🌟")

# Prompt the user for event details
event_name = input("Input the event > ")
event_year = int(input("Input the year > "))
event_month = int(input("Input the month > "))
event_day = int(input("Input the day > "))

# Get today's date
today = datetime.today()
event_date = datetime(event_year, event_month, event_day)

# Calculate the difference in days
days_difference = (event_date - today).days

# Display the appropriate message
if days_difference == 0:
    print(f"🎉🎉 {event_name} is today! 🎉🎉")
elif days_difference > 0:
    print(f"⏳ {event_name} is in {days_difference} day(s).")
else:
    print(f"😢 {event_name} was {abs(days_difference)} day(s) ago.")
