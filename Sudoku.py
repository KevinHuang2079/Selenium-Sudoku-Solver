# sudoku_board = [
#   [0, 7, 0, 0, 8, 0, 6, 1, 5],
#   [2, 5, 3, 1, 0, 4, 0, 0, 0],
#   [6, 0, 0, 0, 9, 5, 0, 2, 0],
#   [0, 6, 7, 0, 0, 0, 0, 0, 1],
#   [0, 0, 5, 0, 0, 8, 7, 6, 4],
#   [3, 0, 0, 9, 7, 0, 0, 0, 2],
#   [0, 9, 0, 4, 5, 7, 0, 0, 0],
#   [5, 8, 2, 0, 3, 0, 9, 0, 0],
#   [0, 0, 0, 0, 0, 0, 1, 5, 6]
# ]
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
                return (i,j) 


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
    emptyPosition = findEmpty(board)
    if emptyPosition is None:
        return True
    else:
        emptyRow, emptyColumn = emptyPosition

    for i in range(1, 10):
        if isValidPlacement(board, i, emptyRow, emptyColumn):
            board[emptyRow][emptyColumn] = i
            print("Placing", i, "at", emptyRow, emptyColumn)
            if solveBoard(board):
                return True
            
            else:
                print("Backtracking from", i, "at", emptyRow, emptyColumn)
                board[emptyRow][emptyColumn] = 0

    return False


# printBoard(sudoku_board)
# solveBoard(sudoku_board)
# print("---------------------")
# printBoard(sudoku_board)
