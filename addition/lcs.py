def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    f = [[0 for i in xrange(n1+1)] for j in xrange(n2+1)]
    for i in xrange(1, n2+1):
        for j in xrange(1, n1+1):
            if s2[i-1] == s1[j-1]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
    return f[n2][n1]


s1 = 'abcde'
s2 = 'bcd'
print lcs(s1, s2)
