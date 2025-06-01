def listSum(nums):
    sum = 0

    for i in nums: 
        sum += i # Add number to sum
    return sum

print(f"sum = {listSum([1, 2, 3, 4, 5])}")
