# Generates a random board

import random
import sys
import checker

sep = '\n' +  ('-' * 20) + '\n'

def printGrid(grid):
    for row in grid:
        print(row)
   
def fillGrid(grid = []): 
    if not grid:
        # If grid is empty initialize it
        print(f'Grid does not exist. Must initialize.')
        grid = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

        print(sep)
        printGrid(grid)
        print(sep)

    for rowindex, row in enumerate(grid):
        # For every (0, [0,0,0,0,0,0,0,0,0])

        print(f'Starting row {rowindex}')

        if 0 not in row:
            print(f'This row is already filled in. Moving on to row number {rowindex + 1}')
            # This row has already been filled in. Move on to next row
            continue

        # Take a copy of current grid before any changes are made.
        prevGrid = [row[:] for row in grid]

        for colindex, col in enumerate(row):
            # For every column in row
            print(f'Starting column {colindex}. Current number: {col}')

            if grid[rowindex][colindex]:
                # Non zero number. Move on to next column
                print(f'Filled in. Moving on to next column {colindex + 1}')
                continue
            
            # Initialize attempted to be an empty list
            attempted = []

            while True:
                # Recalculate numbers based on what's in row
                numbers = [x for x in range(1,10) if x not in row and x not in attempted]
                print(f'Current numbers to pick from: {numbers}')

                if len(numbers) == 0:
                    # Ran out of numbers to pick from. Back track to previous grid
                    print(f'Ran out of valid options. Reverting back to previous grid')
                    printGrid(prevGrid)
                    print(sep)
                    grid = fillGrid(prevGrid)
                    return grid

                # Pick number at random from list of available numbers
                # Assign that number to current location in grid
                num = random.choice(numbers)
                grid[rowindex][colindex] = num

                print(f'Trying number {num} at {rowindex},{colindex}')
                
                # Check to see if number passes
                if checker.checkNum(grid, rowindex, colindex):
                    # Passes - pop number from numbers and break out of while loop.
                    # Should move on to next position in row
                    print(f'{num} passes checks. Moving on to next position')
                    print(sep)
                    printGrid(grid)
                    print(sep)
                    break
                else:
                    # Fails - pop number from numbers and stay in while loop.
                    # Should stay on current position in row
                    print(f'{num} fails checks. Picking a new number')
                    print(sep)
                    grid[rowindex][colindex] = 0
                    attempted.append(num)

        # Row complete
        print(f'Row {rowindex} is complete.', 'FINISHED SOLVING' if rowindex == 8 else f'Moving on to row {rowindex}')  
        print(sep)

    return grid

def removeCells(grid, num):
    #Take copy of grid
    grid = [row[:] for row in grid]

    blanks = 0
    print(f'Beginning with {blanks} blanks. Entering while loop.')

    while True:
        print(f'Current blanks: {blanks}')

        # Check to see if we have desired blanks
        if blanks == num:
            print(f'blanks{blanks} = num{num}. Breaking out of while loop. Falling off end of function')
            break
        
        # Pick random cell from grid
        row = random.choice(range(0,9))
        col = random.choice(range(0,9))

        print(f'Chosen cell: {row},{col}.')
        print(f'Current number in cell: {grid[row][col]}')

        if grid[row][col]:
            print('Current number is non zero. Making it zero and adding one to blanks')
            grid[row][col] = 0
            blanks += 1

        print(sep)
        printGrid(grid)
        print(sep)

    return grid


if __name__ == '__main__':
    file = open('output.txt', 'w')
    sys.stdout = file

    # Generate board
    print('BEGIN GENERATING PUZZLE')
    grid = fillGrid()
    print(sep)

    # Remove cells
    print('BEGIN REMOVING CELLS')
    puzzle = removeCells(grid, 30)
    print(sep)

    # Solve board
    print('BEGIN SOLVING')
    solvedPuzzle = fillGrid(puzzle)

    print(sep)
    print('FILLED PUZZLE')
    print(sep)
    printGrid(grid)
    print(sep)

    print('INITIAL PUZZLE')
    print(sep)
    printGrid(puzzle)
    print(sep)

    print('SOLVED PUZZLE')
    print(sep)
    printGrid(solvedPuzzle)
    print(sep)
