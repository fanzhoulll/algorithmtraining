def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid:
        return
    nRow = len(obstacleGrid)
    nColumn = len(obstacleGrid[0])
    pathes = [[0 for i in xrange(nColumn)] for j in xrange(nRow)]
    for i in xrange(nRow):
        if obstacleGrid[i][0] != 1:
            pathes[i][0] = 1
        else:
            break
    for j in xrange(nColumn):
        if obstacleGrid[0][j] != 1:
            pathes[0][j] = 1
        else:
            break
    for i in xrange(1, nRow):
        for j in xrange(1, nColumn):
            if obstacleGrid[i][j] != 1:
                pathes[i][j] = pathes[i-1][j] + pathes[i][j-1]
    return pathes[nRow-1][nColumn-1]

arr = [[0,0,0],[0,1,0],[0,0,0]]
print uniquePathsWithObstacles(arr)
