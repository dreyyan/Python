def bubble_sort(array):
    temp = 0
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            while array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print(f'Bubble Sort:\n{array}')

array = [4, 9, 5, 1, 7, 8, 6, 3, 2]
bubble_sort(array)