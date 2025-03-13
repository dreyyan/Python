def dict_max_value(d1):
    current_value = 0
    counter = 0
    max_value = 0
    for i in d1.values():
        if max_value < i:
            max_value = i
    for j in d1.keys():
        if d1[j] == max_value:
            print(f'Key \'{j}\' has the max value of {max_value}')
            break
dict1 = {'a':1, 'b':3, 'c':7, 'd':2, 'e':5}
dict_max_value(dict1)