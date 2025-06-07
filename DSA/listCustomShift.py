def customShift(nums, start, end) -> None:
    numToInsert = nums.pop(0) # pop element to insert
    nums.insert(end, numToInsert) # insert element to end index

    for i in nums:
        print(i, end=" ")

customShift([1, 2, 3, 4, 5], 0, 3)
