def sortList(lst) -> None:
    lst.sort()

    for i in lst:
        print(i, end=' ')

lst = [8, 5, 7, 3, 6, 4, 1, 9, 2]
sortList(lst)
