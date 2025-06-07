# Brute force
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target: # If target is the sum of the two numbers, return the indices
#                 return i, j

# Optimized
def twoSum(nums, target) -> None:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen: # If difference is found in the hash map, return the indices of the difference and i
            return seen[diff], i
        seen[num] = i # Else, add the number to the list of seen numbers
        
print(f"{twoSum([2, 7, 11, 15], 9)}")
