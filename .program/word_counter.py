# PROBLEM: Given a string input from the user, count & display the # of words in the input
input_sentence = input("Enter a sentence: ").strip() # Remove leading/trailing whitespaces

if input_sentence: # If input sentence is not empty
    word_counter = len(input_sentence.split()) # Split input into words in a list
else:
    word_counter = 0 # Set counter to 0 if no words were inputted

print(f"There are {word_counter } word/s in the sentence.") # Display Result