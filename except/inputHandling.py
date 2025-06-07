def inputNumber(num) -> None:
    try:
        value = int(num)
    except ValueError as e:
        print(f"ERROR: {e}")
    else:
        print(f"you chose: {num}")
        
inputNumber("yes")
inputNumber(3.5)
