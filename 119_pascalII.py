def getRow(rowIndex):
    nums = [1]
    for i in xrange(1, rowIndex+1):
        # i >= 2, i is also the # of elements before appending
        nums.append(1)
        for j in reversed(xrange(1, i)):
            nums[j] = nums[j-1] + nums[j]
    return nums

print getRow(3)
