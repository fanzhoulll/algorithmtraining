def findMin(nums):
    # lo, hi:
    # pivtol must between lo and hi
    # if nums[lo] < nums[hi], return nums[lo], no pivtol
    # elif nums[m] < nums[hi], search in left
    # else search in right
    if not nums:
        return 0
    lo = 0
    hi = len(nums) - 1
    while (lo < hi):
        m = lo + (hi - lo)/2
        if nums[m] > nums[hi]:
            lo = m + 1
        elif nums[m] < nums[hi]:
            hi = m
    return nums[lo]

nums = [6, 7, 8,9, 10,2, 3, 4, 5]
print findMin(nums)
