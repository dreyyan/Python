def return_duplicate_elements(arr1, arr2):
    sets = set()
    for i in arr1:
        for j in arr2:
            if i == j:
                sets.add(i)
    print(sets)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 4, 6, 8, 10]
return_duplicate_elements(arr1, arr2)