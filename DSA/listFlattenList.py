def listFlattenList(nums):
    newList = [] # To store the flattened list

    for i in nums:
        if isinstance(i, list):
            listFlattenList(i)
        else:
            newList.append(i)
    
    # Display flattened list
    for i in newList:
        print(i, end=' ')
    

listFlattenList([[[1, 2], 3], [4, 5]])
