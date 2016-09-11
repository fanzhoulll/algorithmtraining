def twoSum(nums, target):
    dic = {}
    for i in xrange(len(nums)):
        v = target - nums[i]
        if v in dic:
            return [i, dic[v]]
        dic[nums[i]] = i

nums = [3,2,4]
target = 6
print twoSum(nums, target)
