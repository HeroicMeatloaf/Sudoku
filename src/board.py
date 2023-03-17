# Generates a random board

import random
import sys
import checker

sep = '\n' +  ('-' * 20) + '\n'

global prevBoard

def printboard(board):
    for row in board:
        print(row)
   
def fillboard(board = []): 
    if not board:
        # If board is empty initialize it
        print(f'board does not exist. Must initialize.')
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

    print(sep)
    printboard(board)
    print(sep)

    for rowindex, row in enumerate(board):
        # For every (0, [0,0,0,0,0,0,0,0,0])

        print(f'Starting row {rowindex + 1}')

        if 0 not in row:
            print(f'This row is already filled in. Moving on to row number {rowindex + 2}')
            print(sep)
            # This row has already been filled in. Move on to next row
            continue

        for colindex, col in enumerate(row):
            
            prevBoard = [row[:] for row in board]
            # For every column in row
            print(f'Starting column {colindex}. Current number: {col}')
            print(sep)


            if board[rowindex][colindex]:
                # Non zero number. Move on to next column
                print(f'Filled in. Moving on to next column {colindex + 1}')
                print(sep)
                continue
            

            # Recalculate numbers based on what's in row
            numbers = checker.valid(board, rowindex, colindex)
            random.shuffle(numbers)


        
            # print(f'Current numbers to pick from: {numbers}')
            
            while numbers:
                number = random.choice(numbers)
                board[rowindex][colindex] = number
                numbers.remove(number)
                board = fillboard(board)
                

                board[rowindex][colindex] = 0
            return board
            
            

            print(sep)
            printboard(board)
            print(sep)
                
    
                           
    

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

if __name__ == '__main__':
    file = open('output.txt', 'w')
    sys.stdout = file

    # Generate board
    print('GENERATE FULL BOARD')
    filledBoard = fillboard()

    # Generate puzzle
    print('GENERATE PUZZLE')
    puzzle = removeCells(filledBoard, 30)
    print(countZeros(puzzle))

    # Solve Puzzle
    print('SOLVE PUZZLE')
    solvedPuzzle = fillboard(puzzle)

    print(sep)
    printboard(filledBoard)
    print(sep)

    printboard(puzzle)
    print(sep)

    printboard(solvedPuzzle)




    


