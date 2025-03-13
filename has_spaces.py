def has_spaces(word):
    has_space = False
    for char in word:
        if char == '':
            print(f'{word} has spaces')
            return

    print(f'{word} has no spaces')

has_spaces("tre e")
# fix