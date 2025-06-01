# PROBLEM: Given a dictionary of characters-value, determine the key with the lowest value
key_values = {'a': 3, 'b': 9, 'c': 1, 'd': 7, 'e': 5} # Dictionary of key-values
min_value = key_values['a'] # To keep track of the least value in the dictionary
min_key = '' # To store the key with the minimum value
for key, value in key_values.items():
    if value < min_value: # If value is lesser than the current minimum value
        min_value = value # Set minimum value to current value
        min_key = key # Set minimum key

print(f"Key '{min_key}' has the minimum value of {min_value}") # Display results