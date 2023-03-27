"""
Purpose of this module is to export functions used in generating and
solving sudoku boards.

Functions exported:

printboard(board) - Prints board
fillboard(board = []) - Fills/solves board depending on usage
removeCells(board, num) - Removes specified number of cells from board
complete(board) - Checks if board is filled out

"""

# Standard library imports
import random
import sys

# Local application imports
import checker

def printboard(board):
    """
    Prints board in a readable manner by putting each row in a separate
    line.

    Parameters
    ----------
    board: list
        The board to be printed. Should be a 2-D list
    
    Returns
    -------
    None

    """

    for row in board:
        print(row)
   
def fillboard(board = []): 
    """
    Generates a full board or solves puzzle depending on usage.

    Parameters
    ----------
    board: list, optional
        The board to be solved if used. If omitted, one will be 
        initialized and used to generate a new puzzle.

    Returns:
    board: list
        Filled with non zero values.

    """
    if not board:
        # If board is empty initialize it
        board = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]]
    else:
        # Take copy
        board = [row[:] for row in board]

    # Loop through each of the 81 positions
    for position in range(0, 81):

        # Get row and col
        row = position // 9
        col = position % 9
   
        if board[row][col]:
            # Non zero number. Move on to next column
            continue
        
        # Recalculate numbers based on valid numbers
        numbers = checker.valid(board, row, col)
        random.shuffle(numbers)

        for num in numbers:
            board[row][col] = num
            board = fillboard(board)

            if complete(board):
                return board
            else:
                board[row][col] = 0

        return board
        
    return board
            
def removeCells(board, num):
    """
    Removes specified number of cells from board

    Parameters
    ----------
    board: list
        The board from which cells will be removed

    num: int
        The number of cells to be removed

    Returns:
    board: list
        With the specified number of cells removed and replaced by 0
        
    """

    #Take copy of board
    board = [row[:] for row in board]

    blanks = 0
    
    positions = list(range(0, 81))
    
    while blanks < num:
        
        position = random.choice(positions)
        
        board[position // 9][position % 9] = 0
        positions.remove(position)
        blanks += 1

    return board

def complete(board):
    """
    Checks if the board is filled in with nonzero numbers.
    Doesnt neccessarily check for correctness.

    Parameters
    ----------
    board: list
        The board to be checked

    Returns:
    bool
        The boolean value indicating if the board is/isnt complete
        
    """
    for row in board:
        if 0 in row:
            return False

    return True

if __name__ == '__main__':
    file = open('output.txt', 'w')
    sys.stdout = file

    filledBoard = fillboard()
    puzzle = removeCells(filledBoard, 70)
    solvedPuzzle = fillboard(puzzle)
    

    # Generate board
    print('GENERATE FULL BOARD')  
    print(sep)
    printboard(filledBoard)
    print(sep)

    # Generate puzzle
    print('PUZZLE')   
    print(sep)
    printboard(puzzle)
    print(sep)
    print(countZeros(puzzle))

    # Solve puzzle
    print('SOLVED PUZZLE')
    print(sep)
    printboard(solvedPuzzle)
    print(sep)
