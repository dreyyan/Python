def unique_set_elements(list):
    set_list = set()
    for i in list:
        set_list.add(i)
    print(set_list)

list_arr = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5]
unique_set_elements(list_arr)