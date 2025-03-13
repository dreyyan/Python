# Prompt user to input a sentence
input_sentence = input("Enter a sentence: ").strip() # Remove leading/trailing whitespaces

if input_sentence: # If input sentence is not empty
    word_counter = len(input_sentence.split())
else: # Set counter to 0 if no words were inputted
    word_counter = 0

# Display Result
print(f"There are {word_counter } word/s in the sentence.")