"""
Purpose of this module is to export functions used in checking cells of
Sudoku board

Functions exported:

valid(board, row, col) - Returns list of valid numbers for given cell
checkNum(board, row, col) - Checks validity of number at given cell
"""

def valid(board, row, col):
    """
    Returns a list of valid numbers given a position on board

    Parameters
    ----------
    board: list
        The board to be checked

    row: int
        The row number

    col: int
        The column number
    
    Returns
    -------
    validNumbers: list
        A list of validNumbers at the requested position

    """

    invalidNumbers = {}
    rowNums = set(board[row][:col] + board[row][col + 1:])
    colNums = set([rows[col] for rows in board][:row] + [rows[col] for rows in board][row + 1:])


    boxNums = []
    y = row // 3
    x = col // 3

    if y == 0:
        boxNums.extend((board[0], board[1], board[2]))

    elif y == 1:
        boxNums.extend((board[3], board[4], board[5]))

    else:
        boxNums.extend((board[6], board[7], board[8]))

    if x == 0:
        boxNums = [row[:3] for row in boxNums]

    elif x == 1:
        boxNums = [row[3:6] for row in boxNums]

    else:
        boxNums = [row[6:] for row in boxNums]

    boxNums = [item for row in boxNums for item in row]
    boxNums.remove(board[row][col])
    boxNums = set(boxNums)

    invalidNumbers = rowNums | colNums | boxNums

    validNumbers = [num for num in range(1,10) if num not in invalidNumbers]

    return validNumbers

# Runs invalid to get the list of invalid numbers and then checks to see if number at board[row][col] is in that list
def checkNum(board, row, col):
    """
    Checks a number at a given postion and returns a boolean indicating whether or
    not the number is valid. Uses valid to first get list of valic number and then
    checks to see if the number at the given position in valid

    Parameters
    ----------
    board: list
        The board to be checked

    row: int
        The row number

    col: int
        The column number
    
    Returns
    -------
    boolean
        True if valid, False if not valid

    """

    validNumbers = valid(board, row, col)

    if board[row][col] in validNumbers:
        return True
    else:
        return False

if __name__ == '__main__':

    puzzle = [[7, 2, 8, 9, 4, 3, 5, 6, 1],
              [4, 1, 5, 6, 7, 0, 8, 2, 9],
              [9, 0, 0, 2, 8, 5, 3, 7, 4],
              [8, 4, 7, 3, 9, 2, 6, 1, 0],
              [1, 0, 2, 8, 0, 0, 0, 0, 0],
              [0, 0, 6, 7, 0, 1, 0, 0, 2],
              [5, 0, 3, 4, 2, 6, 7, 9, 8],
              [2, 0, 0, 5, 3, 0, 0, 4, 6],
              [6, 8, 4, 1, 0, 0, 2, 5, 0]]

    
    

    print(valid(puzzle, 2, 1))
    print(checkNum(puzzle, 2, 1))

    puzzle[2][1] = 6
    print(valid(puzzle, 2, 1))
    print(checkNum(puzzle, 2, 1))

    puzzle[2][2] = 6
    print(valid(puzzle, 2, 1))
    print(checkNum(puzzle, 2, 1))
