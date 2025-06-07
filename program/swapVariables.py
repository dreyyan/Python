def swapVariables(x, y) -> None:
    x, y = y, x
    print(f"x = {x}, y = {y}")

x, y = 1, 2
swapVariables(x, y)
