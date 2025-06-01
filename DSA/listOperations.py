# List Operations
# 1. Syntax
lst = [1, 2, 3, 4, 5]

# 2. Add elements
lst.append(6)           # Add element at the end
lst.insert(1, 1.5)      # Insert at {index}, {element} 

# 3. Remove elements
lst.remove(3)           # Remove element
lst.pop()               # Remove and return last element
lst.pop(1)              # Remove and return last element at {index}

# 4. Access and modify
print(lst[0])           # Access element
lst[1] = 20             # Modify element 
lst.index(20, start=0, end=len(lst)) # Returns first index of specified element

# 5. Other
print(lst.count(2)) 
lst.sort()              
lst.reverse()
lst.extend(range(4, 7)) # Appends 4-6

for i in lst:
    print(i)
