def factorial(n):
  # Base case: if n is 1, return 1
  if n == 1:
      print("1", end="")  # Print the last part of the workings
      return 1
  else:
      print(f"{n} * ", end="")  # Print the current number and multiplication sign
      return n * factorial(n - 1)

# User interaction
print("🌟 Factorial Finder 🌟")
number = int(input("Input a number > "))

if number < 1:
  print("Please enter a positive integer.")
else:
  print("Workings: ", end="")
  result = factorial(number)
  print(f"\nThe factorial of {number} is {result}.")
