def nextPermutation_noInplace(nums):
    if len(nums) <= 1:
        return nums
    i = len(nums) - 1
    while i >= 1:
        if nums[i-1] < nums[i]:
            for j in reversed(xrange(len(nums))):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
            return nums[:i] + list(reversed(nums[i:]))
        i -= 1
    return nums[::-1]

def reverse(nums, start, end):
    i = start
    j = end
    while (i <= j):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def nextPermutation(nums):
    n = len(nums)
    if n <= 1:
        return
    i = n - 1
    while i >= 1:
        if nums[i-1] < nums[i]:
            for j in reversed(xrange(len(nums))):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
            reverse(nums, i, n-1)
            return
        i -= 1
    reverse(nums, 0, n-1)
    return


S = [2,1,0,0,0]
nextPermutation(S)
print S
