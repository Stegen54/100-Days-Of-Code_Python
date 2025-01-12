# Step 1: Open and read the high.score file
try:
    with open('high.score', 'r') as file:
        scores = file.readlines()
except FileNotFoundError:
    print("Error: high.score file not found.")
    exit()

# Step 2: Initialize variables to track the leader
current_leader = ""
max_score = 0

# Step 3: Process each line to find the highest score
print("🌟Current Leader🌟")
print("Analyzing high scores......")

for line in scores:
    # Split each line into name and score
    data = line.strip().split()

    # Ensure the line has both name and score
    if len(data) < 2:
        continue

    name = ' '.join(data[:-1])  # Join all parts except the last one as the name
    try:
        score = int(data[-1].replace(',', ''))  # Convert score to integer
    except ValueError:
        print(f"Skipping invalid score entry: {line.strip()}")
        continue

    # Update current leader if this score is the highest
    if score > max_score:
        current_leader = name
        max_score = score

# Step 4: Display the leader
if current_leader:
    print(f"Current leader is {current_leader} with {max_score:,}")
else:
    print("No valid scores found.")
