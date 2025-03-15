# PROBLEM: Given two string input from the user, determine if they are anagrams
first_word = input("Enter first word: ").lower().strip() # Prompt user to enter the first word
second_word = input("Enter second word: ").lower().strip() # Prompt user to enter the second word

first_character_list = {} # To store the first word's list of characters /w their frequency
second_character_list = {} # To store the second word's list of characters /w their frequency

for c in first_word: # Iterate first word's characters
    if c in first_character_list: # If character already exists in the dictionary
        first_character_list[c] += 1 # Increment character count
    else: # If character doesn't exist in the dictionary
        first_character_list[c] = 1 # Set character count to one

for c in second_word: # Iterate second word's characters
    if c in second_character_list: # If character already exists in the dictionary
        second_character_list[c] += 1 # Increment character count
    else: # If character doesn't exist in the dictionary
        second_character_list[c] = 1 # Set character count to one

are_anagrams = True # To check if both words are anagrams

for (key, value), (key1, value1) in zip(first_character_list.items(), second_character_list.items()):
    if value != value1: # If character frequencies are not equal
        are_anagrams = False # They are not anagrams
        print(f"{first_word} & {second_word} are not anagrams.") # Display result
        break # Exit loop

if are_anagrams: # If both words are anagrams
    print(f"{first_word} & {second_word} are anagrams.")  # Display result