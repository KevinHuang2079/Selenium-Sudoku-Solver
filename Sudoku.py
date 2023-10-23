sudoku_board = [
  [3, 2, 1, 0, 0, 7, 9, 0, 6],
  [0, 4, 0, 9, 0, 1, 0, 0, 0],
  [9, 0, 0, 4, 2, 6, 0, 3, 0],
  [0, 5, 2, 0, 7, 0, 1, 0, 0],
  [0, 8, 0, 2, 4, 0, 7, 0, 0],
  [0, 0, 7, 0, 0, 0, 3, 8, 2],
  [7, 0, 9, 8, 0, 0, 0, 5, 0],
  [2, 0, 0, 7, 5, 4, 0, 0, 0],
  [0, 1, 4, 0, 9, 0, 0, 0, 8]
]

def printBoard(board):
    for i in range(len(board)):
        if(i % 3 == 0 and i != 0):
            print("- - - - - - - - - - -")

        for j in range(len(board)):
            if(j % 3 == 0 and j != 0):
                print("| ", end = "")

            if (j == len(board) - 1):
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end = "")

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 0):
                return (i,j) #tuple (row, column)


    return None


def isValidPlacement(board, num, row, column):
    # Check if number is in the same 3x3 box
    boxStartRow = 3 * (row // 3)
    boxStartCol = 3 * (column // 3)
    for i in range(boxStartRow, boxStartRow + 3):
        for j in range(boxStartCol, boxStartCol + 3):
            if board[i][j] == num and (i, j) != (row, column):
                return False

    # Check if number is in the same row
    for i in range(9):
        if board[row][i] == num and i != column:
            return False

    # Check if number is in the same column
    for i in range(9):
        if board[i][column] == num and i != row:
            return False

    return True

def solveBoard(board):
    return solveBoardHelper(board)


def solveBoardHelper(board):
    emptyPosition = findEmpty(board)
    if emptyPosition is None:
        return True
    else:
        emptyRow, emptyColumn = emptyPosition

    for i in range(1, 10):
        if isValidPlacement(board, i, emptyRow, emptyColumn):
            board[emptyRow][emptyColumn] = i
            print("Placing", i, "at", emptyRow, emptyColumn)
            if solveBoardHelper(board):
                return True
            
            print("Backtracking from", i, "at", emptyRow, emptyColumn)
            board[emptyRow][emptyColumn] = 0

    return False



printBoard(sudoku_board)
solveBoard(sudoku_board)
print("---------------------")
printBoard(sudoku_board)
