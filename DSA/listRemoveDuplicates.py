def removeDuplicates(nums) -> None:
    nums.sort() # sort list for easy removal
    newList = []

    for i in nums:
        if i not in newList:
            newList.append(i) # append element if not yet listed

    for i in newList:
        print(i, end=' ')

removeDuplicates([1, 1, 2, 3, 3, 3, 4, 5, 5])
