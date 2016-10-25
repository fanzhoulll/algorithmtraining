def isInterleave(s1, s2, s3):
    # Initial
    # f[i][j] = f[i-1][j] & s3[i+j-1] == s1[i-1] or
    # f[i][j-1] & s3[i+j-1] == s1[j-1]
    # return f[len(s1)][len(s2)]
    row = len(s2)
    col = len(s1)
    if len(s3) != row + col:
        return False
    f = [[False for i in xrange(col+1)] for j in xrange(row+1)]
    f[0][0] = True
    for i in xrange(row):
        if s3[i] == s2[i]:
            f[i+1][0] = True
        else:
            break
    for j in xrange(col):
        if s3[j] == s1[j]:
            f[0][j+1] = True
        else:
            break
    for i in xrange(1, row+1):
        for j in xrange(1, col+1):
            f[i][j] = (f[i-1][j] and s3[i+j-1] == s2[i-1]) or \
            (f[i][j-1] and s3[i+j-1] == s1[j-1])
    return f[row][col]

s1 = "a"
s2 = ""
s3 = "c"
print  isInterleave(s1, s2, s3)
