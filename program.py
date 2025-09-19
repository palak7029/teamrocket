# Double Space Detector

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Flag to check if any double space is found
found = False

# Loop through the sentence to check consecutive spaces
for i in range(len(sentence) - 1):
    if sentence[i] == " " and sentence[i+1] == " ":
        print(f"Double space found at position {i}")
        found = True

# If no double space found
if not found:
    print("No double spaces found.")