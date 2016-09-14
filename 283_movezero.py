def moveZeros(nums):
    if not nums:
        return []
    firstzero = -1
    check = 0
    while check < len(nums):
        '''
        Invariant:
        nums[0,firstzero-1] non-zero element, nums[firstzero, check-1] all zero
        '''
        if nums[check]:
            if firstzero >= 0:
                nums[firstzero] = nums[check]
                nums[check] = 0
                firstzero += 1
        elif firstzero < 0:
            firstzero = check
        check += 1
    return nums

def moveZero_sample(nums):
    j = 0
    for i in nums:
        if i:
            nums[j] = i
            j += 1
    for j in xrange(j, len(nums)):
        nums[j] = 0
    return nums

S = [0, 0, 0, 1, 1]
print moveZero_sample(S)
