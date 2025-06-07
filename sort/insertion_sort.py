def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j > -1 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    print(f'Insertion Sort:\n{array}')

array = [4, 9, 5, 1, 7, 8, 6, 3, 2]
insertion_sort(array)