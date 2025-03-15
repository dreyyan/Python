def is_subset(s1, s2):
    if s1.issubset(s2):
        print("Set 1 is a subset of Set 2")
    else:
        print("Set 1 is not a subset of Set 2")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset(set1, set2)