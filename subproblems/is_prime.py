def is_prime(num):
    i = num - 1

    while i > 1:
       if num % i == 0:
           return False
       i -= 1

    return True

print(is_prime(2))
print(is_prime(6))