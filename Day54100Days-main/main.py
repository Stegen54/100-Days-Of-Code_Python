import csv

# Initialize total earnings
total_earnings = 0

# Read the CSV file and calculate total earnings
with open("Day54Totals.csv", 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Convert 'Cost' and 'Quantity' values to their respective types
        cost = float(row['Cost'])
        quantity = int(row['Quantity'])
        # Calculate total for each item and add it to total earnings
        total_earnings += cost * quantity

# Print the result
print(f"🌟Shop $$ Tracker🌟\nYour shop took £{total_earnings:,.2f} pounds today.")
