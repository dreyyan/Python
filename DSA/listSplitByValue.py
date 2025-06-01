def listSplitByValue(nums, target):
    parentList = [] # to store sublists
    subList = [] # to store numbers
    i = 0

    while i < len(nums):
        if nums[i] == target:
            parentList.append(subList) # add sublist to the parent list
            subList = [] # reset sublist
            i += 1
        else:
            subList.append(nums[i]) # add element to the sublist
            i += 1

    if subList: # add remaining elements to the sublist
        parentList.append(subList)

    print(parentList) # Display new list

listSplitByValue([1, 2, 0, 3, 4, 0, 5], 0)
