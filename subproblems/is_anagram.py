def is_anagram(str1, str2) -> bool:
    first_word_count = {}
    second_word_count = {}

    for c in str1:
        if c not in first_word_count:
            first_word_count[c] = 1
        else:
            first_word_count[c] += 1

    
    for c in str2:
        if c not in second_word_count:
            second_word_count[c] = 1
        else:
            second_word_count[c] += 1

    return True if first_word_count == second_word_count else False

print(is_anagram("lion", "nilo"))
