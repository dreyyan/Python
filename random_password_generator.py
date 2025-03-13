import random
import string
print("Random Password Generator")

def random_password_generator(length, uppercase_count, lowercase_count, digit_count, character_count):
    random.seed()
    word = ""

    # Uppercase Letters
    for _ in range(uppercase_count):
        word += random.choice(string.ascii_uppercase)

    # Lowercase Letters
    for _ in range(lowercase_count):
        word += random.choice(string.ascii_lowercase)

    # Digits
    for _ in range(digit_count):
        word += random.choice(string.digits)

    # Characters
    for _ in range(character_count):
        word += random.choice(string.punctuation)

    print("Random Password: " + word)

random_password_generator(10, 3, 4, 2, 1)