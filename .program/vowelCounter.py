def vowelCounter(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0

    for c in word.lower():
        if c in vowels:
            vowelCount += 1

    return vowelCount
print(f"Onomatopoeia has {vowelCounter('Onomatopoeia')} vowel/s.")
