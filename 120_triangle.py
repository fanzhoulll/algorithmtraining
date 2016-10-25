def minimumTotal(triangle):
    # f[i][j] = triangle[i][j] + min(f[i-1][j-1], f[i-1][j])
    if not triangle:
        return
    f = triangle[:]
    for i in xrange(1, len(triangle)):
        for j in xrange(i+1):
            if j == 0:
                f[i][j] = triangle[i][j] + f[i-1][j]
            elif j == i:
                f[i][j] = triangle[i][j] + f[i-1][j-1]
            else:
                f[i][j] = triangle[i][j] + min(f[i-1][j-1], f[i-1][j])
    return min(f[len(triangle)-1])

def minimumTotal_concise(triangle):
    # f(i) = triangle(i)(j) + min(f(i-1),f(i))
    if not triangle:
        return
    f = [triangle[0][0]]
    for i in xrange(1, len(triangle)):
        f.append(f[i-1] + triangle[i][i])
        for j in xrange(i-1, 0, -1):
            f[j] = triangle[i][j] + min(f[j-1], f[j])
        f[0] = f[0] + triangle[i][0]
        print f
    return min(f)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print minimumTotal_concise(triangle)
