def threeSumClosest(nums, target):
    if len(nums) < 3:
        return []
    nums.sort()
    closest_dist = -1
    i = 0
    while (i < (len(nums) - 2)):
        # Search solution for nums[i], nums[i+1, len(nums)-1]
        j = i + 1
        k = len(nums) - 1
        while (j < k):
            sum_val = nums[i] + nums[j] + nums[k]
            diff = sum_val - target
            if (closest_dist == -1) or (abs(diff) < closest_dist):
                closest_dist = abs(diff)
                closest_val = sum_val
            if (diff == 0):
                # i < j < k
                return closest_val
            elif (diff > 0):
                k -= 1
                while (j < k) and (nums[k] == nums[k+1]):
                    k -= 1
            else:
                j += 1
                while (j < k) and (nums[j] == nums[j-1]):
                    j += 1
        i += 1
    return closest_val


S = [0,1,1,1]
print threeSumClosest(S, -100)
