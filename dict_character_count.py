def dict_character_count(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    print(dict)
test_word = "hello"
dict_character_count(test_word)