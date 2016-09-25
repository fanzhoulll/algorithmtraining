from sets import Set

def permuteUnique(nums):
    results = [[]]
    for num in nums:
        newresults = []
        for result in results:
            for i in xrange(len(result) + 1):
                newresults.append(result[:i] + [num] + result[i:])
                if i < len(result) and num == result[i]:
                    break
        results = newresults
    return results

def permutation_nodup(S):
    results = []
    permutation_nodup_rec([], S, results)
    return results

def permutation_nodup_rec(soFar, rest, results):
    if not rest:
        results.append(soFar)
    seen = Set()
    for i in xrange(len(rest)):
        if rest[i] not in seen:
            seen.add(rest[i])
            remaining = rest[:i] + rest[i+1:]
            permutation_nodup_rec(soFar + [rest[i]], remaining, results)

S = [3,2,1,2]
for result in permuteUnique(S):
    print result
