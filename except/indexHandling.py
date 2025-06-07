def checkIndexValue(lst, index) -> None:
    try:
        value: int = lst[index] 
    except IndexError as e:
        print(f"ERROR: {e}")
    else:
        print(value)

checkIndexValue(['apple', 'banana', 'cherry'], 3)
checkIndexValue(['apple', 'banana', 'cherry'], 0)
