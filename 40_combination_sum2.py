from sets import Set

def combinationsum(candidates, target):
    candidates.sort()
    results = []
    combinationSum_rec([], candidates, target, results)
    return results

def combinationSum_rec(soFar, rest, target, results):
    # Very similar to the non-repetitive recursive problem, it is a shame that
    # I have considered this for such a long time !!
    if target > 0:
        seen = Set()
        for i in xrange(len(rest)):
            # How to avoid repetitive here ?
            if rest[i] not in seen:
                seen.add(rest[i])
                if rest[i] > target:
                    break
                combinationSum_rec(soFar + [rest[i]], rest[i+1:], target-rest[i], results)
            # Keep pruning
            # print soFar, rest, target

    elif not target:
        results.append(soFar)

candidates = [10,1,2,7,6,1,5]
target = 8
for result in combinationsum(candidates, target):
    print result
