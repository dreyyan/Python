def isAnagram(str1, str2) -> bool:
    firstWordCount = {}
    secondWordCount = {}

    for c in str1:
        if c not in firstWordCount:
            firstWordCount[c] = 1
        else:
            firstWordCount[c] += 1

    
    for c in str2:
        if c not in secondWordCount:
            secondWordCount[c] = 1
        else:
            secondWordCount[c] += 1

    return True if firstWordCount == secondWordCount else False

print(isAnagram("lion", "nilo"))
