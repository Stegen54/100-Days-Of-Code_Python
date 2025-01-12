# 30 Days Down
print("30 Days Down")
heading_length = len("30 Days Down")  # Length of the heading for alignment

for day in range(1, 31):  # Loop for 30 days
    response = input(f"Day {day}:\n")  # Prompt the user for their thoughts
    # Restate their response center-aligned under the heading
    print(f"{' ' * heading_length}You thought Day {day} was {response}.")
