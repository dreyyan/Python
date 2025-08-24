def check_key_value(dct, key) -> None:
    try:
        value: int = dct[key] 
    except KeyError as e:
        print(f"ERROR: {e} key does not exist")
    else:
        print(value)

check_key_value({'a': 1, 'b': 2, 'c': 3}, 'd')
check_key_value({'a': 1, 'b': 2, 'c': 3}, 'a')
