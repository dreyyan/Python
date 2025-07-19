def sum_of_digits(string: str) -> int:
    digit_sum=0
    for digit in string:
        digit_sum+=int(digit) 
    return digit_sum
print(sum_of_digits("15342"))