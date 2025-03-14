# PROBLEM: Given a string input from the user, display the first unique character
user_input = input("Enter a string: ") # Prompt user to enter a string
is_unique = True # To check if character is unique
character_count = {} # To store character frequency

for c in user_input:
    if c not in character_count: # If character does not yet exist in the dictionary
        character_count[c] = 1 # Set its count to 1
    else:
        character_count[c] += 1 # Increment the frequency

for c in user_input:
    if character_count[c] == 1: # If frequency of character is one
        print(f"First unique character: {c}") # Print unique character
        break # Exit the loop