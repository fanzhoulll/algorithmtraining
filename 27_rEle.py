def removeElement(nums, val):
    check = 0
    end = len(nums) - 1
    while check <= end:
        '''
        Invariant:
        nums[0..check-1] not contain val
        nums[end] candidate of the last element
        '''
        if nums[check] == val:
            if nums[end] != val:
                nums[check] = nums[end]
                check += 1
            end -= 1
        else:
            check += 1
    return check

nums = []
print removeElement(nums, 1)
print nums
