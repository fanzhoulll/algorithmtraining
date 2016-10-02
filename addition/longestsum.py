def maxsequencesum(x):
    maxsofar = 0
    maxending = 0
    for i in xrange(len(x)):
        maxending = max(maxending+x[i], 0)
        maxsofar = max(maxsofar, maxending)
    return maxsofar

x = [1,5,-10,2,-1,6]
print maxsequencesum(x)
