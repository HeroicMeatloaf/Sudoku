#Methods for checking numbers

sep = '\n' +  ('-' * 20) + '\n'

def valid(board, row, col):
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

    boxNums = set([item for row in boxNums for item in row])

    invalidNumbers = rowNums | colNums | boxNums

    validNumbers = [num for num in range(1,10) if num not in invalidNumbers]

    return validNumbers


# Runs invalid to get the list of invalid numbers and then checks to see if number at board[row][col] is in that list
def checkNum(board, row, col):

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