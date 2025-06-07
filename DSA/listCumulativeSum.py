def cumulativeSum(nums) -> None:
    newList = []
    sum = 0

    for i in nums:
        sum += i # add sum cumulatively
        newList.append(sum)

    print(newList)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cumulativeSum(nums)
