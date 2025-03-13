def dict_min_value(d1):
    min_value = 0
    counter = 0
    for i in d1.values():
        if counter == 0:
            min_value = i
            counter += 1
        if min_value > i:
            min_value = i
    for i in d1.keys():
        if d1[i] == min_value:
            print(f'Key \'{i}\' has the minimum value of {min_value}')
dict = {'a': 3, 'b': 9, 'c': 1, 'd': 7, 'e': 5}
dict_min_value(dict)