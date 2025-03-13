print("Temperature Converter")

while True:
    choice = input("Convert [C]elsius or [F]ahrenheit: ")

    if choice.lower() == 'c':
        celsius = float(input("Enter Temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(str(celsius) + "C = " + str(fahrenheit) + "F")
        break

    elif choice.lower() == 'f':
        fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(str(fahrenheit) + "F = " + str(celsius) + "C")
        break

    else:
        print("Invalid Input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")