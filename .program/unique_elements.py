# PROBLEM: Given a list of integers, return the unique elements found on the list
number_list = [1, 1, 2, 3, 4, 4, 4, 5, 5] # List of integers
unique_elements = set() # To store unique elements

unique_elements.update(number_list) # Insert elements to the set
print(f"Unique elements: {unique_elements}") # Display unique elements