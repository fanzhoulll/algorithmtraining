def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    sum_values = [[0 for i in xrange(n)] for j in xrange(m)]
    sum_values[0][0] = grid[0][0]
    for i in xrange(1, m):
        sum_values[i][0] = sum_values[i-1][0] + grid[i][0]
    for j in xrange(1, n):
        sum_values[0][j] = sum_values[0][j-1] + grid[0][j]
    for i in xrange(1, m):
        for j in xrange(1, n):
            sum_values[i][j] = grid[i][j] + min(sum_values[i-1][j], sum_values[i][j-1])
    return sum_values[m-1][n-1]

print  minPathSum([[0]])
