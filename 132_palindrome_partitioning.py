def preHandle(s):
    n = len(s)
    palidrome_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        palidrome_matrix[i][i] = 1
        if i < (n - 1):
            palidrome_matrix[i][i+1] = (s[i] == s[i+1])
    for length in xrange(2, n):
        for start in xrange(n-length):
            palidrome_matrix[start][start+length] = \
            palidrome_matrix[start+1][start+length-1] and (s[start] == s[start+length])
    return palidrome_matrix

def minCut(s):
    if not s:
        return 0
    n = len(s)
    f = range(-1, n)
    palidrome_matrix = preHandle(s)
    for i in xrange(1, n+1):
        for j in xrange(i):
            if palidrome_matrix[j][i-1] and (f[j] + 1 < f[i]):
                f[i] = f[j] + 1
    return f[n]

s = 'abaab'
print minCut(s)
# print minCut_easiest(s)
