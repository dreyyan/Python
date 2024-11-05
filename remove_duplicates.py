def remove_duplicates(array):
    tuple = set()
    counter = 0
    while counter < len(array):
        tuple.add(array[counter])
        counter += 1
    print(tuple)

test_arr = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 9, 10]
remove_duplicates(test_arr)