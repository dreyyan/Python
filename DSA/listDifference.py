def difference(lst1, lst2) -> None:
    # store different elements unique to lst1 not found in lst2
    differenceList = [i for i in lst1 if i not in lst2]

    for i in differenceList:
        print(i, end=' ')

difference([1, 2, 3, 4], [2, 4])
