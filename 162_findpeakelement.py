def findPeakElement_lint(nums):
    if len(nums) < 3:
        return -1
    lo = 0
    hi = len(nums) - 1
    while (lo <= hi - 2):
        m = lo + (hi - lo)/2
        if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
            # Found a peak
            return m
        elif nums[m] < nums[hi - 1]:
            # find in right
            lo = m
        elif nums[m] < nums[lo + 1]:
            # find in left
            hi = m
        else:

    return -1

def findPeakElement_leet(nums):
    if not nums:
        return -1
    n = len(nums)
    lo = 0
    hi = n - 1
    while ():
        m = lo + (hi - lo)/2
        if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
            # Found a peak
            return m
        elif nums[m] <= nums[hi - 1]:
            # find in right
            lo = m
        else:
            # find in left
            hi = m
    return -1


nums = [1,2,3,4,5,2,1]
print findPeakElement_lint(nums)
