# Generates a random board

# Standard library imports
import random
import sys

# Local application imports
import Sudoku.src.checker as checker

sep = '\n' +  ('-' * 20) + '\n'

global prevBoard

def printboard(board):
    for row in board:
        print(row)
   
def fillboard(board = []): 
    if not board:
        # If board is empty initialize it
        # print(f'board does not exist. Must initialize.')
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
        board = [row[:] for row in board]

    # print(sep)
    # printboard(board)
    # print(sep)

    for position in range(0, 81):

        row = position // 9
        col = position % 9
   
        if board[row][col]:
            # Non zero number. Move on to next column
            continue
        

        # Recalculate numbers based on what's in row
        numbers = checker.valid(board, row, col)
        random.shuffle(numbers)
   
        # print(f'Current numbers to pick from: {numbers}')
        # print(sep)

        for num in numbers:
            board[row][col] = num
            board = fillboard(board)

            if complete(board):
                return board
            else:
                board[row][col] = 0

        return board

        
    return board
                
# prevBoard = [row[:] for row in board]  

def removeCells(board, num):
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

def countZeros(board):

    zeros = 0

    for rowindex, row in enumerate(board):
        for colindex, col in enumerate(row):
            if board[rowindex][colindex] == 0:
                zeros += 1
    return zeros

def complete(board):
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





    


