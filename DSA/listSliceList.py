def sliceList(lst) -> None:
    startList = []
    endList = []
    listSize = len(lst)

    for i in range(listSize):
        if i < listSize // 2:
            startList.append(lst[i])
        else:
            endList.append(lst[i])

    for i in startList:
        print(i, end=' ')

    print()

    for i in endList:
        print(i, end=' ')

sliceList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
