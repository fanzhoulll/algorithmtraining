def maxArea(height):
    '''
    Key is to keep prune impossible branches
    Also, very like the 3-sum problem before. Use two pointers, one scan from left
    to right, another from right to left.
    '''
    i = 0
    maxarea = 0
    j = len(height) - 1
    while i < len(height):
        while (i < j):
            area = min(height[i], height[j])*(j-i)
            maxarea = max(maxarea, area)
            if (height[j] >= height[i]):
                break
            # height[i]*(j-i-1) is the max size between i and j-1
            elif (area > height[i]*(j-i-1)):
                break
            j -= 1
        i += 1
        while (i < len(height)) and (height[i] <= height[i-1]):
            i += 1
    return maxarea

def maxAreaSample(height):
    '''
    While above algorithm get rid of many unnecessary branch, it is still a O(n^2)
    This approach is O(n).
    '''
    i = 0
    j = len(height)-1
    maxarea = 0
    while i < j:
        area = min(height[i], height[j])*(j-i)
        maxarea = max(maxarea, area)
        if (height[i] < height[j]):
            # Should move i
            i += 1
            while (i < j) and (height[i] <= height[i-1]):
                i += 1
        else:
            # Should move j
            j -= 1
            while (i < j) and (height[j] <= height[j+1]):
                j -= 1
    return maxarea


S = range(15, 0, -1)
print S
print maxAreaSample(S)
