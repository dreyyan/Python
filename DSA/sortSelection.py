def selectionSort(arr) -> list:
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr

arr = [8, 1, 4, 2, 7, 6, 9, 5, 3]
sorted: list = selectionSort(arr)
print(sorted)
