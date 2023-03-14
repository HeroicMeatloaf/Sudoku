#Methods for checking numbers

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