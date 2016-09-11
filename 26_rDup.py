def removeDuplicates(nums):
    '''
    Pretty bad algorithm, every del takes O(n), so total takes O(n^2)
    '''
    if not nums:
        return 0
    prev = nums[0]
    index = 1
    while index < len(nums):
        if (nums[index] == prev):
            del nums[index]
        else:
            prev = nums[index]
            index += 1
    return len(nums)


def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    prev = nums[0]
    check = 1
    inorder = 0
    while check < len(nums):
        '''
        Invariant:
        arr[0..inorder] inorder array without duplicate elements
        arr[inorder+1..check-1] duplicate elements
        arr[check] element to be checked
        '''
        if (nums[check] != prev):
            prev = nums[check]
            inorder += 1
            nums[inorder] = prev
        check += 1
    return inorder+1


nums = [1]
total =  removeDuplicates2(nums)
print nums,total
