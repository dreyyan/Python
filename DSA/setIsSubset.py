def isSubset(set1, set2) -> None:
    if set1.issubset(set2):
        print("Set 1 is a subset of Set 2")
    else:
        print("Set 1 is not a subset of Set 2")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
isSubset(set1, set2)
