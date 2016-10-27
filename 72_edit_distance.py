def minDistance(word1, word2):
    row = len(word1)
    col = len(word2)
    f = [[0 for i in xrange(col+1)] for j in xrange(row+1)]
    for i in xrange(row+1):
        f[i][0] = i
    for j in xrange(col+1):
        f[0][j] = j
    for i in xrange(1, row+1):
        for j in xrange(1, col+1):
            if word1[i-1] == word2[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i][j-1]) + 1
    return f[row][col]

word1 = "a"
word2 = ""
print minDistance(word1, word2)
