def dict_invert(dict):
    inverted_dict = {}
    for i, j in dict.items():
        inverted_dict[j] = i
    print(inverted_dict)
dictionary = {1:'a',2:'b',3:'c'}
dict_invert(dictionary)