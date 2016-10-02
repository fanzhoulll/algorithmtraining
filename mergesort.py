def merge(nums1, m, nums2, n):
    last = m+n-1
    i = m-1
    for j in xrange(n-1, -1, -1):
        while i>=0 and nums2[j] < nums1[i]:
            nums1[last] = nums1[i]
            last -= 1
            i -= 1
        nums1[last] = nums2[j]
        last -= 1

def merge2(num1, m, nums2, n):
    last = m + n - 1
    i = m - 1
    j = n - 1
    while (i >= 0 and j >= 0):
        if nums2[j] > nums1[i]:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1
        else:
            nums1[last] = nums1[i]
            last -= 1
            i -= 1
    while j >= 0:
        nums1[last] = nums2[j]
        last -= 1
        j -= 1

nums1 = [2, 0]
nums2 = [1]
m = 1
n = 1
merge2(nums1, m, nums2, n)
for i in nums1:
    print i
