# Solution 1_learn from discussion

def combinationSum_1(candidates, target):
    candidates.sort()
    results = []
    combinationSum_rec([], candidates, target, 0, results)
    return results

def combinationSum_rec_1(soFar, candidates, target, start, results):
    if (target > 0):
        for i in xrange(start, len(candidates)):
            if candidates[i] > target:
                break
            soFar.append(candidates[i])
            combinationSum_rec_1(soFar, candidates, target-candidates[i], i, results)
            #print soFar
            # Find solution or not find solution, in either case, try alternative
            soFar.pop()
    else:
        # target cannot be smaller than 0
        results.append(soFar[:])

# Solution 2: come up by myself

def combinationSum(candidates, target):
        candidates.sort()
        results = []
        combinationSum_rec([], candidates, target, results)
        return results

def combinationSum_rec(soFar, rest, target, results):
    if target > 0:
        for i in rest:
            if i > target:
                break
            combinationSum_rec(soFar+[i], rest, target-i, results)
            # Pruning explored branches
            rest = rest[1:]
    else:
        results.append(soFar)

candidates = [2,3,6,7]
target = 7
#combinationsum(candidates, target)
for result in combinationSum(candidates, target):
    print result
