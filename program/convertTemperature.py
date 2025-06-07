# PROBLEM: Program a temperature converter that allows the user to convert a temperature in any
# unit and convert it to the desired temperature
import os, time

# FUNCTION: Delay output
def delay(s):
    time.sleep(s)

# FUNCTION: Display line format
def display_format(length):
    for _ in range(length):
        print('-', end="")
    print()

# FUNCTION: Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# FUNCTION: Convert temperature
def temperature_converter():
    while True:
        try:
            clear_screen()
            # Prompt user to select the temperature unit to convert
            print("[ TEMPERATURE CONVERTER ]")
            display_format(25)
            print("1. Celsius [°C]")
            print("2. Fahrenheit [°F]")
            print("3. Kelvin [°K]")
            display_format(25)
            temperature_unit = int(input("Temperature: ").strip())
        except ValueError:
            print("Invalid input, please enter a valid choice(1-3).")
            delay(2)
        else:
            if temperature_unit not in range(1, 4):  # If invalid temperature choice
                print("Invalid input, please enter a valid choice(1-3).")
                delay(2)
            else:
                break

    while True:
        try:
            clear_screen()
            # Prompt user to select the temperature unit to convert to
            print("[ TEMPERATURE CONVERTER ]")
            display_format(25)
            print("1. Celsius [°C]")
            print("2. Fahrenheit [°F]")
            print("3. Kelvin [°K]")
            display_format(25)
            convert_temperature = int(input("Convert to: ").strip())
        except ValueError:
            print("Invalid input, please enter a valid choice(1-3).")
            delay(2)
        else:
            if convert_temperature not in range(1, 4):  # If invalid temperature choice
                print("Invalid input, please enter a valid choice(1-3).")
                delay(2)
            elif temperature_unit == convert_temperature:  # If unit and temperature to convert to are the same
                print("Temperature unit & temperature to convert to cannot be the same.")
                delay(2)
            else:
                break

    # Set name of temperature
    if temperature_unit == 1:
        temperature_unit_name = "°C"
    elif temperature_unit == 2:
        temperature_unit_name = "°F"
    else:
        temperature_unit_name = "°K"

    if convert_temperature == 1:
        temperature_unit_to_convert = "°C"
    elif convert_temperature == 2:
        temperature_unit_to_convert = "°F"
    else:
        temperature_unit_to_convert = "°K"

    while True:
        try:
            clear_screen()
            # Prompt user to enter the temperature
            temperature = float(input(f"Enter temperature[{temperature_unit_name}]: ").strip())
        except ValueError:
            print("Invalid temperature, please enter a valid value.")
            delay(2)
        else:
            break

    result = 0  # To store the result

    if convert_temperature == 1:  # Convert to Celsius
        if temperature_unit == 2:  # using Fahrenheit
            result = (temperature - 32) * 5 / 9
        elif temperature_unit == 3:  # using Kelvin
            result = temperature - 273.15
    elif convert_temperature == 2:  # Convert to Fahrenheit
        if temperature_unit == 1:  # using Celsius
            result = (temperature * 1.8) + 32
        elif temperature_unit == 3:  # using Kelvin
            result = (temperature - 273.15) * (9 / 5) + 32
    elif convert_temperature == 3:  # Convert to Kelvin
        if temperature_unit == 1:  # using Celsius
            result = (temperature - 32) * (5 / 9) + 273.15
        elif temperature_unit == 2:  # using Fahrenheit
            result = temperature + 273.15

    # Round value up to two decimal places
    result = round(result, 2)
    # Display results
    clear_screen()
    print(f"{temperature}{temperature_unit_name} => {result}{temperature_unit_to_convert}")

    while True:
        # Prompt user to convert again
        choice = input("Convert again[y/n]?: ").lower().strip()
        if choice == 'y':
            temperature_converter()
        elif choice == 'n':
            print("Exiting program...")
            delay(2)
        else:
            print("Invalid choice, please enter 'y' to convert again or 'n' to exit the program.")
            delay(2)

temperature_converter() # Test
