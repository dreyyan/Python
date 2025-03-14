# PROBLEM: Given a string input from the user, reverse the string, replace all vowels with '*',
# and convert all consonants with uppercase
user_input = input("Enter a string: ") # Prompt user to enter a string
user_input = user_input[::-1] # Reverse the string

new_characters = [] # Initialize a list to store transformed characters
for i in range(len(user_input)): # Iterate through the characters
    if user_input[i].lower() in ['a', 'e', 'i', 'o', 'u']: # If character is a vowel
        new_characters.append('*') # Add a '*' to the new input
    elif user_input[i].isalpha(): # Elif character is a consonant
        new_characters.append(user_input[i].upper()) # Add the character's uppercase to the new input
    else: new_characters.append(user_input[i]) # Else(not a letter), add the character

new_input = ''.join(new_characters) # Join strings
print(f'Transformed: {new_input}') # Display transformed string