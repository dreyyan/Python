def concatenate_tuple(t1, t2):
    new_tuple = tuple(t1 + t2)
    print(new_tuple)


tup1 = (True, "Apple", 50.1)
tup2 = ("House", 2, False)
concatenate_tuple(tup1, tup2)