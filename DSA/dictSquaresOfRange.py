def squareOfIntegers(maxRange) -> None:
    numSquares = {}

    for i in range(1, maxRange + 1):
        numSquares[i] = pow(i, 2)

    for key, value in numSquares.items():
        print(f"{key}^2 = {value}")

squareOfIntegers(5)
