# 1 2 3 4 5 6 7 8 9; 3; 20

# Here is another idea
def combinationSum_rec_own(k, n, start, soFar, results):
    #print soFar, start
    total_num = len(soFar)
    total_value = sum(soFar)
    # One result find
    if total_num == k and total_value == n:
        results.append(soFar[:])
        return
    # No result find
    if (total_num > k) or (start > 9) or (total_value > n) or ((k-total_num)*9 < n-total_value):
        return
    for i in xrange(start, 10):
        soFar.append(i)
        combinationSum_rec_own(k, n, i+1, soFar, results)
        soFar.pop()

def combinationSum3_own(k, n):
    nums = range(1,10)
    results = []
    combinationSum_rec_own(k, n, 1, [], results)
    return results

def combinationSum3_rec(soFar, nums, start, left, target, results):
    if left > 0 and target > 0:
        for i in xrange(start, len(nums)):
            # Prune !
            if (nums[i] > target):
                break
            if (nums[i] + (left-1)*nums[-1] < target):
                continue
            soFar.append(nums[i])
            combinationSum3_rec(soFar, nums, i+1, left-1, target-nums[i], results)
            soFar.pop()
    elif (not left) and (not target):
        results.append(soFar[:])


def combinationSum3(k, n):
    nums = range(1,10)
    results = []
    combinationSum3_rec([], nums, 0, k, n, results)
    return results

for result in combinationSum3_own(3, 20):
    print result
