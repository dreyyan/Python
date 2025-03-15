# PROBLEM: Given a string input from the user, count & display the # of vowels in the string
vowel_list = ['a', 'e', 'i', 'o', 'u'] # To store the list of vowels
string_input = input("Enter a word/sentence: ") # Prompt user to input a word/sentence

vowel_counter = 0 # To store how many vowels are in the user's input

for c in string_input: # Iterate through each character in the input
    for vowel in vowel_list: # Iterate through vowel list
        if c == vowel: # If character is a vowel
            vowel_counter += 1 # Increment the vowel counter

print("# of Vowels: " + str(vowel_counter)) # Display # of vowels found