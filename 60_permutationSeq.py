import math

def getPermutation(n, k):
    return getPermutationRec(math.factorial(n-1), k-1, '', ''.join(map(str, range(1, n+1))))

def getPermutationRec(fac, k, soFar, rest):
    if len(rest) <= 1:
        return soFar + rest[0]
    newCharIndex = k/fac
    newChar = rest[newCharIndex]
    remaining = rest[:newCharIndex] + rest[newCharIndex+1:]
    return getPermutationRec(fac/(len(rest)-1), k%fac, soFar + newChar, remaining)

print getPermutation(1,1)
