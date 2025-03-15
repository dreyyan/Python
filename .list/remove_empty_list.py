def remove_empty_list(list):
    for i in list:
        if not i:
            list.remove(i)
    print(list)

arr = [[], 1, 2, [1, 2], []]
remove_empty_list(arr)