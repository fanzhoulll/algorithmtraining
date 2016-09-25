def countAndSay(n):
    if not n:
        return ''
    nums = '1'
    count = 1
    for i in xrange(1,n):
        newnums = ''
        for j in xrange(len(nums)):
            if (j == len(nums) - 1) or (nums[j] != nums[j+1]):
                newnums += str(count)
                newnums += nums[j]
                count = 1
            else:
                count += 1
        nums = newnums
    return nums

print countAndSay(5)
