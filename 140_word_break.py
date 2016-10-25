def wordBreak(s, wordDict):
    # leetcode
    # f[i] = or(f[j]) for j<i and s[j, i] is a word
    # init: f[0] = True
    # return f[n-1]
    if not s or not wordDict:
        return False
    n = len(s)
    f = [False]*(n+1)
    f[0] = True
    maxlen = max(len(s) for s in wordDict)
    for i in xrange(1, n+1):
        for j in xrange(i, max(i-maxlen-1, -1), -1):
            # j: first j char can be coded
            # j+1 - i is also a word i = 1->n
            if (f[j] and (s[j:i] in wordDict)):
                f[i] = True
                break
    return f[n]

def wordBreak2(s, wordDict):
    if not s or not wordDict:
        return False
    n = len(s)
    f = [False]*n
    maxlen = max(len(s) for s in wordDict)
    for i in xrange(n):
        for j in xrange(i-maxlen, i+1):
            if ((j < 0) and (s[:i+1] in wordDict)) or (j>=0 and f[j] and (s[j+1:i+1] in wordDict)):
                f[i] = True
                break
    return f[n-1]


s = "ab"
wordDict = ["a", "b"]
print wordBreak2(s, wordDict)
