def rob(nums):
    # f(i) is the max money you can get until i
    fn_2 = 0
    fn_1 = 0
    fn = 0
    for i in xrange(len(nums)):
        fn = max(fn_1, (fn_2 + nums[i]))
        fn_2 = fn_1
        fn_1 = fn
    return fn

nums = [4,3,3,4]
print rob(nums)
