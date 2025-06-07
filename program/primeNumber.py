def isPrime(num):
    i = num - 1

    while i > 1:
       if num % i == 0:
           return False
       i -= 1

    return True

print(f"2 is {'' if isPrime(2) else 'not '}prime.")
print(f"6 is {'' if isPrime(6) else 'not '}prime.")
