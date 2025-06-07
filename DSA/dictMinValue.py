def minValue(dct) -> None:
    minValueKey = min(dct, key=dct.get)
    print(minValueKey)

dct = {'a': 1, 'b': 5, 'c': 10}
minValue(dct)
