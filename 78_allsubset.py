def subset(arr):
    results = []
    subsetRec([], arr, results)
    return results

def subsetRec(soFar, rest, results):
    if not rest:
        # Get current subset
        results.append(soFar)
        return
    subsetRec(soFar + [rest[0]], rest[1:], results)
    subsetRec(soFar, rest[1:], results)

arr = [1,2,3]
for result in subset(arr):
    print result
