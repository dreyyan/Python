# PROBLEM: Given a list of elements, count & display the count of each element
elements = [1, 2, 2, 3, 4, 4, 5] # List of elements
stored_elements = {}  # Store each element as the key and their frequency as the value using a dictionary
for i in elements: # Iterate elements in the list
    stored_elements[i] = stored_elements.get(i, 0) + 1 # Set/increment word frequency

print("Element count:") # Display element & element count
for key, value in stored_elements.items():
    print(f"{key}: {value}")