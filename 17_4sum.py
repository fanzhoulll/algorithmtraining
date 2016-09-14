# How to improve this solution ?
def fourSum(nums, target):
    solutions = []
    if len(nums) < 4:
        return solutions
    i = 0
    nums.sort()
    n = len(nums)
    print nums
    while (i < (n - 3)):
        # Simple prune algorithm, reduce run time from >1s to 150ms
        sum_max = nums[i] + nums[n-3] + nums[n-2] + nums[n-1]
        sum_min = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
        if (target > sum_max) or (target < sum_min):
            i += 1
            continue
        j = i + 1
        while (j < (n - 2)):
            # Simple prune algorithm
            sum_max = nums[i] + nums[j] + nums[n-2] + nums[n-1]
            sum_min = nums[i] + nums[j] + nums[j+1] + nums[j+2]
            if (target > sum_max) or (target < sum_min):
                j += 1
                continue
            k = j + 1
            u = n - 1
            while (k < u):
                sum_val = nums[i] + nums[j] + nums[k] + nums[u]
                if sum_val == target:
                    solutions.append([nums[i], nums[j], nums[k], nums[u]])
                if (sum_val >= target):
                    u -= 1
                    while (k < u) and (nums[u] == nums[u+1]):
                        u -= 1
                if (sum_val <= target):
                    k += 1
                    while (k < u) and (nums[k] == nums[k-1]):
                        k += 1
            j += 1
            while (j < (n - 2)) and (nums[j] == nums[j-1]):
                j += 1
        i += 1
        while (i < (n - 3)) and (nums[i] == nums[i-1]):
            i += 1
    return solutions


S = [0,1,5,0,1,5,5,-4]
for solution in fourSum(S, 11):
    print solution
