def maximalSqaure(matrix):
    m = len(matrix)
    n = len(matrix[0])
    results = [[0 for i in xrange(n)] for j in xrange(m)]
    maxlen = 0
    for i in xrange(1, m):
        for j in xrange(1, n):
            if matrix[i-1][j-1] == '1':
                results[i][j] = min(results[i-1][j], results[i][j-1],\
                results[i-1][j-1]) + 1
                maxlen = max(maxlen, results[i][j])
    return maxlen**2

matrix = ["1111","1111","1111","1111"]
print maximalSqaure(matrix)
