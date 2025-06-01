def listDifference(lst1, lst2):
    # Store different elements unique to lst1 not found in lst2
    differenceList = [i for i in lst1 if i not in lst2]

    # Display different elements
    for i in differenceList:
        print(i, end=' ')

listDifference([1, 2, 3, 4], [2, 4])
