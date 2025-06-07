def findMissingNumber(nums) -> int:
    nums.sort() # to easily determine the missing number
    
    if nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        if nums[i] - 1 != nums[i - 1]:
            return nums[i] - 1
    return -1
                
result = findMissingNumber([9, 4, 2, 6, 7, 1, 5, 3])
print(f"result: {result if result != -1 else 'none'}")
