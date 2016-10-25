from sets import Set

def getEmptyCell(board):
    for i in xrange(9):
        for j in xrange(9):
            # You should choose next cell heuristically;
            if board[i][j] == '.':
                return [i, j, (3*(i/3) + j/3)]
    return [-1, -1, -1]

def solveSudoku_dfs(board, avaRows, avaColumns, avaBoxes):
    [row, column, box] = getEmptyCell(board)
    if row == -1:
        # Find a new solution
        return True
    avaNums = avaRows[row].intersection(avaColumns[column]).intersection(avaBoxes[box])
    if not avaNums:
        # Cannot find any number that satisfy, return
        return False
    for num in avaNums:
        # CoverWithNum
        board[row] = board[row][:column] + num + board[row][column+1:]
        avaRows[row].remove(num)
        avaColumns[column].remove(num)
        avaBoxes[box].remove(num)
        # Backtracking
        if solveSudoku_dfs(board, avaRows, avaColumns, avaBoxes):
            return True
        else:
        # UnCoverWithNum
            board[row] = board[row][:column] + '.' + board[row][column+1:]
            avaRows[row].add(num)
            avaColumns[column].add(num)
            avaBoxes[box].add(num)

def solveSudoku_myown(board):
    avaRows = {}
    avaColumns = {}
    avaBoxes = {}
    for i in xrange(9):
        avaRows[i] = Set(map(str, range(1, 10)))
        avaColumns[i] = Set(map(str, range(1, 10)))
        avaBoxes[i] = Set(map(str, range(1, 10)))
    for i in xrange(9):
        for j in xrange(9):
            if board[i][j] != '.':
                avaRows[i].remove(board[i][j])
                avaColumns[j].remove(board[i][j])
                avaBoxes[3*(i/3) + j/3].remove(board[i][j])
    solveSudoku_dfs(board, avaRows, avaColumns, avaBoxes)

def isValid(board, i, j, k):
    # No k at i's row, j's column and 3*(i/3) + j/3's box !
    for x in xrange(9):
        if (board[i][x] == k) or (board[x][j] == k) or (board[3*(i/3) + x/3][3*(j/3) + x%3] == k):
            return False
    return True

def solve(board):
    for i in xrange(9):
        for j in xrange(9):
            if board[i][j] == '.':
                for k in xrange(9):
                    if isValid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if solve(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True

def solveSudoku(board):
    if (not board) or (len(board) != 9) or (len(board[0]) != 9):
        return;
    for row in xrange(9):
        board[row] = list(board[row])
    solve(board)
    for row in xrange(9):
        board[row] = ''.join(board[row])


board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
solveSudoku_myown(board)
for row in board:
    print row
