def climbStairs(n):
    # fn_2 = f(n-2), fn_1 = f(n-1), n = 3,4...
    if not n:
        return 0
    fn_2 = 0
    fn_1 = 1
    fn = 0
    for i in xrange(1, n+1):
        fn = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = fn
    return fn

print climbStairs(5)
