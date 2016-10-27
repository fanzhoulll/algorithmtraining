def searchInsertHelper(nums, target, lo, hi):
    if lo > hi:
        # Cannot find the num, where is its position ?
        return lo
    m = lo + (hi-lo)/2
    # Could m > len(nums) ?
    if target < nums[m]:
        # Suppose to be in range [lo, m-1]
        return searchInsertHelper(nums, target, lo, m-1)
    elif target > nums[m]:
        # Suppose to be in range [m+1, hi]
        return searchInsertHelper(nums, target, m+1, hi)
    else:
        return m


def searchInsert_rec(nums, target):
    if not nums:
        return 0
    return searchInsertHelper(nums, target, 0, len(nums)-1)

def searchInsert(nums, target):
    if not nums:
        return 0
    lo = 0
    hi = len(nums) - 1
    while (lo <= hi):
        m = lo + (hi - lo)/2
        if target < nums[m]:
            hi = m - 1
        elif target > nums[m]:
            lo = m + 1
        else:
            return m
    return lo


nums = [1,2,3]
print searchInsert(nums, 7)
