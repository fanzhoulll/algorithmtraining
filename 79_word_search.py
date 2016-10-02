def exist_rec(board, word, i, j):
    for row in board:
        print row
    print "--------------------"
    if not word:
         return True
    if (i < 0) or (j < 0) or (i == len(board)) or (j == len(board[0])) or (board[i][j] != word[0]):
        return False
    backup = board[i][j]
    board[i] = board[i][:j] + '*' + board[i][j+1:]
    if (exist_rec(board, word[1:], i-1, j) or exist_rec(board, word[1:], i+1, j) \
     or  exist_rec(board, word[1:], i, j-1) or  exist_rec(board, word[1:], i, j+1)):
     return True
    board[i] = board[i][:j] + backup + board[i][j+1:]
    return False

def exist(board, word):
    for i in xrange(0, len(board)):
        for j in xrange(0, len(board[0])):
            if exist_rec(board, word, i, j):
                return True
    return False

board = ["ABCE","SFCS","ADEE"]
word = "ABCCED"
print exist(board, word)
