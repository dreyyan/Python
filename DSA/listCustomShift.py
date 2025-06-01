def listCustomShift(nums, start, end):
    numToInsert = nums.pop(0) # Pop element to insert
    nums.insert(end, numToInsert) # Insert element to end index

    # Display shifted array
    for i in nums:
        print(i, end=" ")

listCustomShift([1, 2, 3, 4, 5], 0, 3)
