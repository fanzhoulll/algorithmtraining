def rob(nums, lo, hi):
    # f(i) is the max money you can get until i
    fn_2 = 0
    fn_1 = 0
    fn = 0
    for i in xrange(lo, hi):
        fn = max(fn_1, (fn_2 + nums[i]))
        fn_2 = fn_1
        fn_1 = fn
    return fn

def rob_cir(nums):
    return max(rob(nums, 0, len(nums)-1), rob(nums, 1, len(nums)))

nums = [4,3,3,4]
print rob_cir(nums)
