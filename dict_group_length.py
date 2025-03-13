def group_length(t1):
    dict = {}
    length = 0
    letter_count = 0
    for i in t1:
        length = len(i)
        if length not in dict:
            dict[length] = [i]
        else:
            dict[length].append(i)
    print(dict)
test_list = ['cat', 'ocean', 'dog', 'river', 'goat']
group_length(test_list)