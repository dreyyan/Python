def listMaximumMinimum(nums):
    min, max = 0, 0

    # Sort the list to easily determine min/max number
    nums.sort()

    # Set min/max number
    min = nums[0]
    max = nums[len(nums) - 1]

    # Display output
    print(f"min = {min}")
    print(f"max = {max}")
    
listMaximumMinimum([2, 4, 5, 3, 1])
