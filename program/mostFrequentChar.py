# PROBLEM: Given a string input from the user, display the most frequent character from the string
user_input = input("Enter a string: ") # Prompt user to enter a string

stored_characters = {} # Store each character as the key and their frequency as the value using a dictionary

for c in user_input: # Iterate through each character
    if c not in stored_characters: # If character doesn't exist in the dictionary
        stored_characters[c] = 1 # Set the character's count to 1
    else: stored_characters[c] += 1 # Else, increment its count

print("Character Frequencies:") # Display output by key-value
for key, value in stored_characters.items():
    print(f'{key}: {value}')