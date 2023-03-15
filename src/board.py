# Generates a random board

import random
import sys
import checker

sep = '\n' +  ('-' * 20) + '\n'

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
            print(f'This row is already filled in. Moving on to row number {rowindex + 1}')
            # This row has already been filled in. Move on to next row
            continue

        # Take a copy of current board before any changes are made.
        prevboard = [row[:] for row in board]

        for colindex, col in enumerate(row):
            # For every column in row
            print(f'Starting column {colindex}. Current number: {col}')

            if board[rowindex][colindex]:
                # Non zero number. Move on to next column
                print(f'Filled in. Moving on to next column {colindex + 1}')
                continue
            
            # Initialize attempted to be an empty list
            attempted = []

            while True:
                # Recalculate numbers based on what's in row
                numbers = [x for x in range(1,10) if x not in checker.invalid(board, rowindex, colindex) and x not in attempted]
                print(f'Current numbers to pick from: {numbers}')

                if len(numbers) == 0:
                    # Ran out of numbers to pick from. Back track to previous board
                    print(f'Ran out of valid options. Reverting back to previous board')
                    printboard(prevboard)
                    print(sep)
                    board = fillboard(prevboard)
                    return board

                # Pick number at random from list of available numbers
                # Assign that number to current location in board
                num = random.choice(numbers)
                board[rowindex][colindex] = num

                print(f'Trying number {num} at {rowindex},{colindex}')
                
                # Check to see if number passes
                if checker.checkNum(board, rowindex, colindex):
                    # Passes - pop number from numbers and break out of while loop.
                    # Should move on to next position in row
                    print(f'{num} passes checks. Moving on to next position')
                    print(sep)
                    printboard(board)
                    print(sep)
                    break
                else:
                    # Fails - pop number from numbers and stay in while loop.
                    # Should stay on current position in row
                    print(f'{num} fails checks. Picking a new number')
                    print(sep)
                    board[rowindex][colindex] = 0
                    attempted.append(num)

        # Row complete
        print(f'Row {rowindex + 1} is complete.', 'FINISHED SOLVING' if rowindex == 8 else f'Moving on to row {rowindex + 2}')  
        print(sep)

    return board

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




    


