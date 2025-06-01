import math

def returnSqrts(nums):
    sqrtList = []

    for i in range(len(nums)):
        sqrtList.append(math.sqrt(nums[i]))

    return sqrtList

sqrtList = returnSqrts([1, 2, 3, 4, 5])

for i in sqrtList:
    print(i)
