def most_frequent_character(string: str):
    character_count={}

    for c in string:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1

    most_frequent:str = max(character_count, key=character_count.get) # type: ignore
    return most_frequent

print(most_frequent_character('onomatopoeia'))
