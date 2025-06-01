# PROBLEM: Given an integer, display the squares of numbers 1 to n
numbers = {} # Store each integer as key and their squares as the value
while True:
    max_range = int(input("Enter an integer[n > 0]: ").strip()) # Prompt user to enter the max range
    if max_range < 1:  # If max range is a non-positive integer
        print("Invalid max range, please enter a value greater than 0.")
    else:
        break

for i in range(1, max_range + 1):
    numbers[i] = i * i # Store integers & their squares

print("Squares:") # Display integers and their squares
for key, value in numbers.items():
    print(f"{key} => {value}")