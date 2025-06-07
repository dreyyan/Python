def dictCharacterCount(string) -> None:
    characterCount = {}

    for c in string:
        c = c.lower() # converts uppercase -> lowercase
        if c not in characterCount:
            characterCount[c] = 1
        else:
            characterCount[c] += 1

    for key, value in characterCount.items():
        print(f"{key}: {value}")

dictCharacterCount("onomatopoeia")
