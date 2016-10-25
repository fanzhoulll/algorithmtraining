def maxSubArray_dp(nums):
    # F(i) = max sub array until i and contains i
    # F(i) = max[F(i-1) + nums[i], nums[i]]
    # max sub array = max(F(1), F(2)...F(3))
    maxending = nums[0]
    maxsofar = nums[0]
    for i in xrange(1, len(nums)):
        maxending = max(maxending+nums[i], nums[i])
        maxsofar = max(maxsofar, maxending)
    return maxsofar

nums = [-1, 5, 5]
print maxSubArray_dp(nums)
