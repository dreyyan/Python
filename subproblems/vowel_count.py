def vowel_count(string: str) -> int:
    vowels=['a', 'e', 'i', 'o', 'u']
    vowel_count=0

    for c in string:
        if c in vowels:
            vowel_count+=1
    
    return vowel_count
print(vowel_count("onomatopoeia"))