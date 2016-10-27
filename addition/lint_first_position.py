def binarySearchSuckHelper(nums, target, lo, hi):
    if lo > hi:
        return -1
    m = lo + (hi-lo)/2
    medium = nums[m]
    if target > medium:
        return binarySearchHelper(nums, target, m+1, hi)
    elif target < medium:
        return binarySearchHelper(nums, target, lo, m-1)
    else:
        # Worst case gonna spend O(n) time
        for i in xrange(m, -1, -1):
            if target != nums[i]:
                return i+1 # Not good way
        return 0


def binarySearch_suck(nums, target):
    if not nums:
        return -1
    return binarySearchHelper(nums, target, 0, len(nums)-1)

def binarySearch(nums, target):
    if not nums:
        return -1
    lo = 0
    hi = len(nums) - 1
    while (lo <= hi):
        m = lo + (hi - lo)/2
        if target < nums[m]:
            hi = m - 1
        elif target > nums[m]:
            lo = m + 1
        else:
            hi = m - 1
    if nums[lo] == target:
        return lo
    else:
        return -1

nums = [4,4,4,4]
print binarySearch(nums, 1)
