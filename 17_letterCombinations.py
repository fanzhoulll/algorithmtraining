def letterCombinations(digits):
    if not digits:
        return []
    results = []
    candidates = []
    charlist = [' ', '*', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    for i in digits:
        candidates.append(charlist[int(i)])
    letterCombinations_rec('', candidates, results)
    return results

def letterCombinations_rec(soFar, rest, results):
    if not rest:
        results.append(soFar)
        return
    for j in xrange(len(rest[0])):
        remaining = rest[1:]
        letterCombinations_rec(soFar+rest[0][j], remaining, results)

print letterCombinations('')
