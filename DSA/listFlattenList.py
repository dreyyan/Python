def flattenList(lst) -> list:
    flattenedList = []

    for i in lst:
        if isinstance(i, list): # recursively add flattened list
            flattenedList.extend(flattenList(i))
        else:
            flattenedList.append(i)

    return flattenedList

lst = [[[1, 2], 3, 4], 5, 6]
print(flattenList(lst))
