indent = ""
# DFS
def permute(nums):
    '''
    Backtracking algorithm
    '''
    solutions = []
    solve_rec([], nums, solutions)
    return solutions

def solve_rec(soFar, rest, solutions):
    enter(soFar)
    if not rest:
        solutions.append(soFar) # backtracking
    for i in xrange(len(rest)):
        remaining = rest[:i]+rest[i+1:]
        solve_rec(soFar+[rest[i]], remaining, solutions)


S = [1, 2, 3]
permute(S)
#for i in permute(S):
    #print i
