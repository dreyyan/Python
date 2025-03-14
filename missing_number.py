# PROBLEM: Given an array of N-1 integers(1 to N), find the missing number
integers = [8, 1, 5, 9, 4, 2, 3, 7] # List that stores a number list
N = len(integers) - 1 # To store the max range
missing_numbers = [] # To store missing numbers

for i in range(1, N + 1): # Iterate from 1 to N
    if i not in integers: # If number is not found
        missing_numbers.append(i) # Add to missing numbers

if len(missing_numbers) == 1: # If list of missing numbers has only one number
    print(f"The missing number is {missing_numbers}")  # Display the missing number
else:
    print(f"The missing numbers are {missing_numbers}") # Display the missing numbers