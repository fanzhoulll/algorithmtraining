def maxProduct(nums):
    # Very different from 53_maxsubarray_sum !
    #
    maxsofar = nums[0]
    maxending = nums[0]
    minending = maxending
    for i in xrange(1, len(nums)):
        a = maxending*nums[i]
        b = minending*nums[i]
        maxending = max(a, b, nums[i])
        minending = min(a, b, nums[i])
        maxsofar = max(maxending, maxsofar)
    return maxsofar

nums = [-2, -3, 3, 4, -4]
print maxProduct(nums)
