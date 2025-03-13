def dict_word_frequency_counter(string):
    dict = {}
    word_slice = ""
    for i in string:
        if i == ' ':
            dict[word_slice] = dict.get(word_slice, 0) + 1
            word_slice = ""
            continue
        word_slice += i
    print(dict)
words = "hello world hello world hello "
dict_word_frequency_counter(words)
