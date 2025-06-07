def invertKeyValue(dct) -> None:
    invertedDct = {}

    for i, j in dct.items():
        invertedDct[j] = i

    for key, value in invertedDct.items():
        print(f"{key}: {value}")

dct = {1:'a',2:'b',3:'c'}
invertKeyValue(dct)
