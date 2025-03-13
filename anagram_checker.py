print("Anagram Checker")

def anagram_checker(first_word, second_word):
    valid_letters = 0

    for i in first_word:
        for j in second_word:
            if i == j:
                valid_letters += 1
                break

    if valid_letters != len(first_word):
        print(first_word + " and " + second_word + " are not anagrams.")
    else:
        print(first_word + " and " + second_word + " are anagrams.")


anagram_checker("vase", "save")