def chunkList(nums, length) -> None:
    parentList, childList = [], []

    for index, num in enumerate(nums): 
        childList.append(num) # add current number to current chunk

        if len(childList) == length: 
           parentList.append(childList) # save chunk to parent list 
           childList = [] # reset chunk
    
    if childList: 
        parentList.append(childList) # add remaining chunk to parent list

    print(parentList) # Print entire list 

chunkList([1, 2, 3, 4, 5, 6, 7, 8], 3)
