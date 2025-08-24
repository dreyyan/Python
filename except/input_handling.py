def input_number(num) -> None:
    try:
        value = int(num)
    except ValueError as e:
        print(f"ERROR: {e}")
    else:
        print(f"you chose: {num}")
        
input_number("yes")
input_number(3.5)
