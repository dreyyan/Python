def check_index_value(lst, index) -> None:
    try:
        value: int = lst[index] 
    except IndexError as e:
        print(f"ERROR: {e}")
    else:
        print(value)

check_index_value(['apple', 'banana', 'cherry'], 3)
check_index_value(['apple', 'banana', 'cherry'], 0)
