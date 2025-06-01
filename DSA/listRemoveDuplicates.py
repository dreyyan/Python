def listRemoveDuplicates(nums):
    nums.sort() # Sort list for easy removal
    newList = [] # To store the list of first occurence elements

    # Append first occurence elements to the new list
    for i in nums:
        if i not in newList:
            newList.append(i)

    # Display new list
    for i in newList:
        print(i, end=' ')

listRemoveDuplicates([1, 1, 2, 3, 3, 3, 4, 5, 5])
