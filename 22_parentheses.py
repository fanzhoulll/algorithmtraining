def generateParenthesis_rec(strlist, left, right, n):
    if len(strlist) == 2*n:
        print strlist
        return
    print strlist
    if (left < n):
        generateParenthesis_rec(strlist+"(", left+1, right, n)
    if (right < left):
        generateParenthesis_rec(strlist+")", left, right+1, n)

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    generateParenthesis_rec("", 0, 0, 3)


generateParenthesis(3)
