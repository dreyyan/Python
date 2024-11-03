print("Character Frequency")

def character_frequency(word, letter):
    letter_counter = 0

    for char in word.lower():
        if char == letter:
            letter_counter += 1

    print(f'Letter \'{letter}\' has occured in the word \'{word}\' {letter_counter} time/s')

character_frequency("Goose", "g")