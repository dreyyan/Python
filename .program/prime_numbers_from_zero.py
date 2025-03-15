def prime_numbers_from_zero(number):
    array = []
    while i > number:
        i = number - 1
        if i % number == 0:
            array.append(i)

prime_numbers_from_zero(20)