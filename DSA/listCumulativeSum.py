def cumulative_sum(arr):
    new_list = []
    sum = 0
    for i in arr:
        sum += i
        new_list.append(sum)
    print(new_list)


test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cumulative_sum(test_arr)
