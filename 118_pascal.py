def generate(numRows):
    if not numRows:
        return
    nums = [[1]]
    for i in xrange(1, numRows):
        'numRows >= 2'
        newnums = [1]
        n = len(nums[i-1])
        for j in xrange(n):
            if j == n-1:
                newnums.append(1)
            else:
                newnums.append(nums[i-1][j] + nums[i-1][j+1])
        nums.append(newnums)
    return nums

for row in generate(5):
    print row
