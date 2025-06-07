def bubbleSort(arr) -> list:
    for i in range(len(arr)):
        for j in range (len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [8, 1, 4, 2, 7, 6, 9, 5, 3]
sorted: list = bubbleSort(arr)
print(sorted)
