def dict_square(n):
    dict = {}
    counter = 1
    while counter <= n:
        dict[counter] = counter * counter
        counter += 1
    print(dict)
dict_square(5)