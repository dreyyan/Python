def disjoint_set(s1, s2):
    set_list = s1 & s2

    if len(set_list) == 0:
        print("There are no common elements.")
    else:
        print(f'There are {len(set_list)} common elmeents: ')
        print(set_list)


set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
disjoint_set(set1, set2)
