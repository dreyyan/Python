print("Prime or Composite")

number = int(input("Enter Number: "))
divisor = number - 1

while True:
    if number == 1:
        print("1 is Prime")
        break

    if divisor == 1:
        print(str(number) + " is Prime")
        break

    if number % divisor != 0:
        divisor -= 1

    else:
        print(str(number) + " is Composite")
        break