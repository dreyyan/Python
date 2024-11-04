def list_element_swap(list):
    temp = list.pop(2)
    list.append(list[0])
    list[0] = temp
    print(list)

test_array = [1, 2, 3]
list_element_swap(test_array)