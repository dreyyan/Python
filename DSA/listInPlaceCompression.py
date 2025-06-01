def listInPlaceCompression(nums):
    i = 1

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(nums[i - 1])
        else:
            i += 1

    for i in nums: 
        print(i)
       

listInPlaceCompression([1, 1, 2, 2, 2, 3, 1])
