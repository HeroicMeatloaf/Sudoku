import random
import sys



sep = '\n' +  ('-' * 20) + '\n'

def checkRow(grid, row, col):
    if grid[row][col] in grid[row][:col] + grid[row][col + 1:]:
        # print('checkRow - FAILED')
        return False
    else:
        # print('checkRow - PASSED')
        return True

def checkCol(grid, row, col):
    column = [rows[col] for rows in grid][:row] + [rows[col] for rows in grid][row + 1:]
    if grid[row][col] in column:
        # print('checkCol - FAILED')
        return False
    else:
        # print('checkCol - PASSED')
        return True

def checkBox(grid, row, col):

    box = []
    y = row // 3
    x = col // 3

    if y == 0:
        box.extend((grid[0], grid[1], grid[2]))

    elif y == 1:
        box.extend((grid[3], grid[4], grid[5]))

    else:
        box.extend((grid[6], grid[7], grid[8]))

    if x == 0:
        box = [row[:3] for row in box]

    elif x == 1:
        box = [row[3:6] for row in box]

    else:
        box = [row[6:] for row in box]

    box = [item for row in box for item in row]

    if box.count(grid[row][col]) > 1:
        return False
    else:
        return True

# Runs checkRow(), checkCol(), checkBox() to determine if number is valid. Returns True/False
def checkNum(grid, row, col):
    if checkRow(grid, row, col) and checkCol(grid, row, col) and checkBox(grid, row, col):
        # print('checkNum - PASSED')
        return True
    else:
        # print('checkNum - FAILED')
        return False

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
                if checkNum(grid, row, col):
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

# def fillGrid(grid = []): 
#     if not grid:
#         grid = [[0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0]]

#     for row in range(9):
#         numbers = [x for x in range(1, 10)]
#         for col in range(9):
#             prevGrid = [row[:] for row in grid]
#             numLength = len(numbers)
#             attempted = []

#             while True:
#                 if len(attempted) == numLength:
#                     break
#                 num = random.choice([x for x in numbers if x not in attempted])
#                 grid[row][col] = num
                
#                 print(f'Currenlty trying {num} from {numbers}. This is attempt number {len(attempted) + 1}')
#                 print(f'Checking {num} for cell {row}-{col}')
#                 if checkNum(grid, row, col):
#                     print(f'{num} at ({row}-{col}) is valid', end = sep)
#                     numbers.pop(numbers.index(num))
#                     printGrid(grid)
#                     break
#                 else:
#                     attempted.append(num)
#                     print(f'{num} at ({row}-{col}) is not valid')
#                     printGrid(grid)

#                 if len(attempted) == numLength:
#                     print('TRIED ALL NUMBERS. RETURNING TO PREVIOUS STATE AND TRYING AGAIN')
#                     grid = fillGrid(prevGrid)
#     return grid    

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
