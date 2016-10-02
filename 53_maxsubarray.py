def maxSubArray_dp(nums):
    maxending = nums[0]
    maxsofar = nums[0]
    for i in xrange(1, len(nums)):
        maxending = max(maxending+nums[i], nums[i])
        maxsofar = max(maxsofar, maxending)
    return maxsofar

nums = [-1, 1,2,3,-10,5]
print maxSubArray_dp(nums)
