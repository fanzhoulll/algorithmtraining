def uniquePaths(m, n):
    pathes = [[0 for j in xrange(n)] for i in xrange(m)]
    for i in xrange(m):
        pathes[i][0] = 1
    for j in xrange(n):
        pathes[0][j] = 1
    for i in xrange(1, m):
        for j in xrange(1, n):
            pathes[i][j] = pathes[i-1][j] + pathes[i][j-1]
    return pathes[m-1][n-1]

print uniquePaths(4,4)
