def vowelCount(string) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowelCount = 0

    for c in string:
        if c in vowels:
            vowelCount += 1

    return vowelCount

print(vowelCount("onomatopoeia"))
