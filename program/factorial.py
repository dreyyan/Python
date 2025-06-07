def factorial(num) -> int:
    product: int = 1

    while num > 1:
        product *= num
        num -= 1

    return product

print(factorial(5))
