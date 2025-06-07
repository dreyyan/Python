def removeEmptyList(lst) -> None:
    for i in lst:
        if not i:
            lst.remove(i) # remove element if empty
    print(lst)

lst = [[], 1, 2, [1, 2], []]
removeEmptyList(lst)
