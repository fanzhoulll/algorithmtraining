def twosum(nums, sum_val):
    solutions = []
    seen_nums = {}
    for num in nums:
        target = sum_val - num
        if target in seen_nums:
            solutions.append([num, target])
            del seen_nums[target]
        else:
            seen_nums[num] = 0
    return solutions

def threesum(nums):
    solutions = []
    nums.sort()
    for i in xrange(len(nums)):
        if ((i == 0) or (nums[i] != nums[i-1])):
            for sub_solution in twosum(nums[i+1:], -nums[i]):
                sub_solution.append(nums[i])
                solutions.append(sub_solution)
    return solutions


S = [-1, 0, 1, -1, 0, 1, 2, 3, -1, -2]
for solution in threesum(S):
    print solution
