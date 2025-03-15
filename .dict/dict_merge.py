def dict_merge(d1, d2):
    d1.update(d2)
    print(d1)
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5}
dict_merge(dict1, dict2)