def dict_frequency_counter(list):
    dict = {}
    for i in list:
        dict[i] = dict.get(i, 0) + 1
    print(dict)
test_list = [1, 2, 2, 3, 4, 4, 5]
dict_frequency_counter(test_list)

"""
dict = {}
key_list = set()
for i in list:
    key_list.add(i)
print(key_list)

for i in key_list:
    counter = 0
    for j in list:
        if i == j:
            counter += 1
    dict.update({i: counter})
print(dict)
"""
