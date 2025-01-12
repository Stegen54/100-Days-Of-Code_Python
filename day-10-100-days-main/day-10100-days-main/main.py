# Step 1: Get the original bill amount
myBill = float(input("What was the bill?: "))

# Step 2: Ask the user for the tip percentage
tipPercentage = float(input("What percentage tip would you like to leave?: "))

# Step 3: Calculate the tip and add it to the original bill
tipAmount = (tipPercentage / 100) * myBill
totalBill = myBill + tipAmount

# Step 4: Ask how many people are splitting the bill
numberOfPeople = int(input("How many people are splitting the bill?: "))

# Step 5: Calculate the amount each person owes
amountPerPerson = totalBill / numberOfPeople

# Step 6: Round the result to 2 decimal places
amountPerPerson = round(amountPerPerson, 2)

# Output the result
print(f"Each person owes: ${amountPerPerson}")




Built my own tip calculator! Time to put it to the test at a restaurant 🍕 !  Day 10 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python