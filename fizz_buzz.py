def fizz_buzz(range):
    for i in range:
        if i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizz_buzz(range(1, 11))