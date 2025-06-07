def maxValue(dct) -> None:
    maxValueKey = max(dct, key=dct.get)
    print(maxValueKey)

dct = {'a': 1, 'b': 5, 'c': 10}
maxValue(dct)

