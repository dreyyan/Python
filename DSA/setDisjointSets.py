def disjointSets(set1, set2) -> None:
    disjointSet = set1 & set2

    if len(disjointSet) == 0:
        print("There are no common elements.")
    else:
        print(f'There are {len(set_list)} common elmeents: ')
        print(disjointSet)


set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
disjointSets(set1, set2)
