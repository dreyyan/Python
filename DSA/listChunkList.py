def listChunkList(nums, length):
    parentList = [] # To store sublists
    childList = [] # To store numbers

    for index, num in enumerate(nums): # Iterate over list
        childList.append(num) # Add number to child list

        if len(childList) == length: # If child list length is the same
           parentList.append(childList) # Add child list
           childList = [] # Reset child list
    
    if childList: # If there are remaining numbers in the child list
        parentList.append(childList) # Add them to the parent list
    print(parentList) # Print entire list 
listChunkList([1, 2, 3, 4, 5, 6, 7, 8], 3)
