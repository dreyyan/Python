def is_capitalized(word):
    for char in word:
        if char.isupper():
            print(f'{word} is capitalized')
            break
        else:
            print(f'{word} is not capitalized')
            break

is_capitalized("Tree")