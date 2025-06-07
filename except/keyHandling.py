def checkKeyValue(dct, key) -> None:
    try:
        value: int = dct[key] 
    except KeyError as e:
        print(f"ERROR: {e} key does not exist")
    else:
        print(value)

checkKeyValue({'a': 1, 'b': 2, 'c': 3}, 'd')
checkKeyValue({'a': 1, 'b': 2, 'c': 3}, 'a')
