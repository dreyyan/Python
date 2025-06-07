def replaceAllOccurences(nums, target, value) -> None:
    i = 0

    while i < len(nums):
        if nums[i] == target:
            nums[i] = value # replace all instances of the target to a value
        i += 1

    for i in nums:
        print(i, end=' ')

replaceAllOccurences([1, 2, 3, 2, 1], 2, 10)
