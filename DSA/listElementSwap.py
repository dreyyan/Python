def elementSwap(lst) -> None:
    temp = list.pop(2)
    list.append(list[0])
    list[0] = temp
    print(list)

lst = [1, 2, 3]
elementSwap(lst)
