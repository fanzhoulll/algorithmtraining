result = []

# DFS
def permute(nums):
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
        return # backtracking
    for i in xrange(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


S = [1, 2, 3]
for i in permute(S):
    print i
