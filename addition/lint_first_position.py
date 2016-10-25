def binarySearchHelper(nums, target, lo, hi):
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


def binarySearch(nums, target):
    if not nums:
        return -1
    return binarySearchHelper(nums, target, 0, len(nums)-1)

nums = [1,1,1,1,1,4,4,5,7,7,8,9,9,10]
print binarySearch(nums, 1)
