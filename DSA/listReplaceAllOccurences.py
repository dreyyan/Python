def listReplaceAllOccurences(nums, target, value):
    i = 0

    while i < len(nums):
        if nums[i] == target:
            nums[i] = value
        i += 1

    for i in nums:
        print(i, end=' ')

listReplaceAllOccurences([1, 2, 3, 2, 1], 2, 10)
