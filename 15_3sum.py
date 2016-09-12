def twosum(nums, sum_val):
    '''
    In nums, find two elements added up to be sum_val
    '''
    solutions = []
    seen_nums = {}
    for num in nums:
        target = sum_val - num
        if (target in seen_nums):
            if  not seen_nums[target]:
                solutions.append([num, target])
                # True target already used, no need to worry about it later
                seen_nums[target] = True
        else:
            # False means the num has not appeared in the solution
            # already finded
            seen_nums[num] = False
    return solutions

def threesum(nums):
    '''
    My own solution, pretty dumb. Use hast table instead of the property
    of sorted array to achieve O(n) two_sum. Also, cannot guarantee the
    output is sorted (extra work required).
    '''
    solutions = []
    # Sort so that same values are put together
    nums.sort()
    for i in xrange(len(nums)):
        # Do not handle repetitive elements
        if ((i == 0) or (nums[i] != nums[i-1])):
            for sub_solution in twosum(nums[i+1:], -nums[i]):
                sub_solution.append(nums[i])
                solutions.append(sub_solution)
    return solutions

def threeSum_sample(nums):
    """
    A much better solution.
    """
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    i = 0
    while (i < (len(nums) - 2)):
        # Search solution for nums[i], nums[i+1, len(nums)-1]
        j = i + 1
        k = len(nums) - 1
        while (j < k):
            sum_val = nums[i] + nums[j] + nums[k]
            if (sum_val == 0):
                # i < j < k
                result.append([nums[i], nums[j], nums[k]])
            # Highlight: continues reduce k or increase i to avoid repetitive solution
            if (sum_val >= 0):
                k -= 1
                while ((j < k) and (nums[k] == nums[k+1])):
                    k -= 1
            if (sum_val <= 0):
                j += 1
                while ((j < k) and (nums[j] == nums[j-1])):
                    j += 1
        i += 1
        while ((nums[i] == nums[i-1]) and (i < (len(nums) - 2))):
            i += 1
    return result

S = [-1,0,1,2,-1,-4]
for solution in threeSum_sample(S):
    print solution
