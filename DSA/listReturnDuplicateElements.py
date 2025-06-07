def returnDuplicateElements(lst1, lst2) -> None:
    sets = set(lst1) & set(lst2) # intersection of both sets, returns duplicates
    print(sets)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [2, 4, 6, 8, 10]
returnDuplicateElements(lst1, lst2)
