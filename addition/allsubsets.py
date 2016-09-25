def subset(arr):
    subsetRec([], arr)

def subsetRec(soFar, rest):
    if not rest:
        # Get current subset
        print soFar
        return
    subsetRec(soFar + [rest[0]], rest[1:])
    subsetRec(soFar, rest[1:])

arr = [1,2,3]
subset(arr)
