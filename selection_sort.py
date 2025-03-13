def selection_sort(array):
    for i in range(0, len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        temp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = temp

    print(f'Selection Sort:\n{array}')

array = [4, 9, 5, 1, 7, 8, 6, 3, 2]
selection_sort(array)