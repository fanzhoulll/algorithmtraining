def get_subset(S):
    subset_rec([],S)

def subset_rec(soFar, rest):
    if not rest:
        print soFar
        return
    print 'Entering subset_rec(soFar+[rest[0]], rest[1:]):  ' + str(soFar) + ',' + str(rest)
    subset_rec(soFar+[rest[0]], rest[1:])
    print 'Entering subset_rec(soFar, rest[1:]): ' + str(soFar) + ',' + str(rest)
    subset_rec(soFar, rest[1:])

S = [1,2,3]
get_subset(S)
