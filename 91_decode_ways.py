def numDecodings_notconcise(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    if s[0] == '0':
        return 0
    res = [1]
    if len(s) >= 2:
        if s[1] != '0':
            if int(s[0]+s[1]) <= 26:
                res.append(2)
            else:
                res.append(1)
        else:
            if s[0] <= '2':
                res.append(1)
            else:
                return 0
    for i in range(2, len(s)):
        if (s[i] > '0') and (s[i-1] > '0'):
            if int(s[i-1]+s[i]) <= 26:
                res.append(res[i-2] + res[i-1])
            else:
                res.append(res[i-1])
        elif s[i-1] > '0':
            if s[i-1] <= '2':
                res.append(res[i-2])
            else:
                return 0
        elif s[i] > '0':
            res.append(res[i-1])
        else:
            return 0
    return res[-1]

def valid(a, b=''):
    if not b:
        return a != '0'
    return (a == '1') or (a == '2') and (b <= '6')

def numDecoding(s):
    n = len(s)
    if (not n) or (s[0] == '0'):
        return 0
    if n == 1:
        return 1
    fn_1 = 1
    fn_2 = 1
    for i in xrange(1, n):
        fn = 0
        if not valid(s[i]) and not valid(s[i-1], s[i]):
            return 0
        if valid(s[i]):
            fn = fn_1
        if valid(s[i-1], s[i]):
            fn += fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn

print numDecoding('27')
