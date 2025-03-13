def tuple_occurences_count(tup, element):
    count = 0
    for i in tup:
        if element == i:
            count += 1
    print(f'{element} occured {count} times')

tuple_test = (1, "Tree", 1, 65.3, False, "Word")
tuple_occurences_count(tuple_test, 1)