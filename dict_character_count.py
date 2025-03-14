# PROBLEM: Given a string input from the user, display the frequency of all characters from the string
user_input = input("Enter a string: ") # Prompt user to enter a string

stored_characters = {} # Store each character as the key and their frequency as the value using a dictionary

for c in user_input: # Iterate through each character
    if not c.isalpha(): # If character is not a letter
        continue # Skip character
    if c.lower() not in stored_characters: # If character doesn't exist in the dictionary
        stored_characters[c.lower()] = 1 # Set the character's count to 1
    else: stored_characters[c.lower()] += 1 # Else, increment its count

highest_frequency_character = '' # To store the character /w the highest frequency
highest_frequency = 0 # To store the highest frequency

for key, value in stored_characters.items():
    if value > highest_frequency: # If the character's frequency is greater than the current highest frequency
        highest_frequency_character = key # Store character with current highest frequency
        highest_frequency = value # Store value of highest frequency
print(f'The letter {highest_frequency_character} appeared the most({highest_frequency}) number of times') # Display character with most frequent count