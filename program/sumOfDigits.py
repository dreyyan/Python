def sumOfDigits(string) -> int:
    sum = 0

    for i in string:
        sum += int(i)

    return sum

print(sumOfDigits("12345"))

