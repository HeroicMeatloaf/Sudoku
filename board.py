# Generates a random board

import random
import sys
import checker

sep = '\n' +  ('-' * 20) + '\n'

def printGrid(grid):
    for row in grid:
        print(row)
    print(sep)

def fillGrid(grid = []): 
    if not grid:
        grid = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

    for row in range(9):
        numbers = [x for x in range(1, 10)]
        prevGrid = [row[:] for row in grid]
        for col in range(9):
            if grid[row][col]:
                numbers.pop(numbers.index(grid[row][col]))
                continue

            numLength = len(numbers)
            attempted = []

            while True:
                if len(attempted) == numLength:
                    # print('TRIED ALL NUMBERS. RETURNING TO PREVIOUS STATE AND TRYING AGAIN')
                    # print(sep)
                    grid = fillGrid(prevGrid)
                    return grid

                num = random.choice([x for x in numbers if x not in attempted])
                grid[row][col] = num
                
                # print(f'Currenlty trying {num} from {numbers}. This is attempt number {len(attempted) + 1}')
                # print(f'Checking {num} for cell {row}-{col}')
                if checker.checkNum(grid, row, col):
                    # print(f'{num} at ({row}-{col}) is valid')
                    numbers.pop(numbers.index(num))
                    # printGrid(grid)
                    break
                else:
                    attempted.append(num)
                    # print(f'{num} at ({row}-{col}) is not valid')
                    # printGrid(grid)
    return grid

def removeCells(grid, num):
    blanks = 0

    while True:
        if blanks == num:
            break

        else:
            row = random.choice(range(0,9))
            col = random.choice(range(0,9))

            if grid[row][col]:
                grid[row][col] = 0
                blanks += 1

if __name__ == '__main__':

    grid = fillGrid()
    removeCells(grid, 30)
    print(sep)
    printGrid(grid)

    # file = open('output.txt', 'w')

    # sys.stdout = file
    # grid = fillGrid()
    # print(sep)
    # printGrid(grid)
