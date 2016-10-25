def minCut(s):
    if not s:
        return 0
    n = len(s)
    min_cut = range(n)
    pal = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        # f[i] = min(f[j-1]) + 1 if j != 0 and j<=i and nums[j,i] is palidrone
        # f[i] = 0 if j == 0 and nums[j,i] is palidrone
        for j in xrange(i+1):
            if s[i] == s[j] and ((j+1 > i-1) or pal[j+1][i-1]):
                pal[j][i] = True
                if not j:
                    min_cut[i] = 0
                else:
                    min_cut[i] = min(min_cut[i], min_cut[j-1]+1)
    return min_cut[n-1]

s = "a"
print minCut(s)
