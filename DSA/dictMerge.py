def mergeDict(dct1, dct2) -> None:
    dct1.update(dct2)
    print(dct1)

dct1 = {'a': 1, 'b': 2}
dct2 = {'c': 3, 'd': 4}
mergeDict(dct1, dct2)
