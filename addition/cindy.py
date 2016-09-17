def isSolved(board):
    numBoards = len(board)
    numMarbles = numBoards/2
    for i in xrange(numMarbles):
        if (board[i] != 2) or (board[numBoards - 1 - i] != 1):
            return False
    return True

def tryMove(i, board):
    if not board[i]:
        return False
    elif board[i] == 1:
        if (i < len(board) - 2) and (not board[i+2]):
            # Move to two squres right
            board[i+2] = 1
            board[i] = 0
            return True
        elif (i < len(board) - 1) and (not board[i+1]):
            # Move to one square right
            board[i+1] = 1
            board[i] = 0
            return True
    else:
        if (i >= 2) and (not board[i-2]):
            # Move to two squares left
            board[i-2] = 2
            board[i] = 0
            return True
        elif (i >= 1) and (not board[i-1]):
            # Move to one square left
            board[i-1] = 2
            board[i] = 0
            return True

def solvable_bug1(board):
    if isSolved(board):
        return True
    for i in range(len(board)):
        # In canMove(i, board), board has already been new board !
        if (tryMove(i, board)):
            # Bugs happen here
            return solvable(board)
            # It does not work out, you have to recover board !
    return False

def solvable_bug2(board):
    if isSolved(board):
        return True
    for i in xrange(len(board)):
        # In canMove(i, board), board has already been new board !
        print i, board
        oldboard = board[:]
        if (tryMove(i, board)):
            if solvable_bug2(board):
                print board
                return True
        # Recover board !
        board = oldboard[:]
    return False

def canMove(i, board):
    if not board[i]:
        return False
    elif board[i] == 1:
        if (i < len(board) - 2) and (not board[i+2]):
            return True
        elif (i < len(board) - 1) and (not board[i+1]):
            return True
    else:
        if (i >= 2) and (not board[i-2]):
            return True
        elif (i >= 1) and (not board[i-1]):
            return True
    return False

def makeMove(i, board):
    newBoard = board[:]
    if newBoard[i] == 1:
        if (i < len(newBoard) - 2) and (not newBoard[i+2]):
            newBoard[i+2] = 1
            newBoard[i] = 0
        elif (i < len(newBoard) - 1) and (not newBoard[i+1]):
            newBoard[i+1] = 1
            newBoard[i] = 0
    else:
        if (i >= 2) and (not newBoard[i-2]):
            newBoard[i-2] = 2
            newBoard[i] = 0
        elif (i >= 1) and (not newBoard[i-1]):
            newBoard[i-1] = 2
            newBoard[i] = 0
    return newBoard

def solvable(board):
    if isSolved(board):
        return True
    for i in xrange(len(board)):
        # In canMove(i, board), board has already been new board !
        print i, board
        if (canMove(i, board)):
            newboard = makeMove(i, board)
            if solvable(newboard):
                print newboard
                return True
    return False


board = [1, 1,0, 2,2]
print solvable_bug2(board)
