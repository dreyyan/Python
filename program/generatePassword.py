import random
import string

def generatePassword(length, uppercaseCount, lowercaseCount, digitCount, characterCount) -> str:
    random.seed() # opt.: to sync random behavior
    word: str = ""

    # generate uppercase letters
    for _ in range(uppercaseCount):
        word += random.choice(string.ascii_uppercase)

    # generate lowercase characters
    for _ in range(lowercaseCount):
        word += random.choice(string.ascii_lowercase)
    
    # generate digits
    for _ in range(digitCount):
        word += random.choice(string.digits)

    # generate punctuations
    for _ in range(characterCount):
        word += random.choice(string.punctuation)

    return word

print(generatePassword(10, 3, 4, 2, 1))
