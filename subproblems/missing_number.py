def missing_number(lst: list) -> int:
    counter = 0
    lst=sorted(lst)

    for i in range(1, len(lst)):
        if lst[i] != lst[i-1] + 1:
            return lst[i-1] + 1
    
    return -1

print(missing_number([1, 2, 3, 5]))