# PROBLEM: Given a string input from the user, count & display the # of words in the sentence
user_input = input("Enter a sentence: ").lower().strip() # Prompt user to enter a sentence
words = {} # To store the words
current_word = "" # To store current word

for c in user_input: # Iterate characters in the sentence
    if c == ' ': # If character is a whitespace
        words[current_word] = words.get(current_word, 0) + 1 # Set/increment word frequency
        current_word = "" # Reset current word
        continue # Skip iteration
    current_word += c # Adds character to the current word

if current_word: # Count the last word(if any)
    words[current_word] = words.get(current_word, 0) + 1

print(f"# of word/s: {len(words)}") # Display result