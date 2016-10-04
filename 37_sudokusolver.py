from sets import Set

def getEmptyCell(board):
    for i in xrange(9):
        for j in xrange(9):
            # You should choose next cell heuristically;
            if board[i][j] == '.':
                return [i, j, (3*i%3 + j%3)]

def solveSudoku_dfs(board, avaRows, avaColumns, avaBoxes):
    [row, column, box] = getEmptyCell(board)
    if not pos:
        # Find a new solution
        return board
    avaNums = avaRows[row].intersection(avaColumns[column]).intersection(avaBoxes[box])
    if not avaNums:
        # Cannot find any number that satisfy, return
        return
    for num in avaNums:
        # CoverWithNum
        board[row][column] = str(num)
        # Backtracking
        solveSudoku_dfs(board, avaRows[row].remove(num), \
            avaColumns[column].remove(num), avaBoxes[box].remove(num))
        # UnCoverWithNum
        board[row][column] = '.'

def solveSudoku(board):
    avaRows = {}
    avaColumns = {}
    avaBoxes = {}
    for i in xrange(9):
        avaRows[i] = Set(list(1, 10))
        avaColumns[i] = Set(list(1, 10))
        avaBoxes[i] = Set(list(1, 10))
    for i in xrange(9):
        for j in xrange(9):
            if board[i][j] != '.':
                avaRows[i].remove(i)
                avaColumns[i].remove(j)
                avaBoxes[i].remove(3*i%3 + j%3)
    solveSudoku_dfs(board, avaRows, avaColumns, avaBoxes):
