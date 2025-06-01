print("Factorial Calculator")

number = int(input("Enter a Number: "))
original_number = number

factorial = 1

while True:
    factorial *= number
    number -= 1

    if number == 1:
        print(str(original_number) + "! = " + str(factorial))
        break
