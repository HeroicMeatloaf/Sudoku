"""
This is the main module of the Sudoku project. This module imports checker.py
and board.py to generate a puzzle and puts the puzzle in a tkinter GUI.


updateNumber(num, row, col) - Updates number in puzzle returned from bd.fillboard().
Called when a number is entered into board

generateBaord() - Calls board.fillboard() and board.removeCells() to create a puzzle
and then displays the puzzle on the board

clearBoard() - Clears board
checkBoard() - Checks board
drawCell(row, col, color) - Draws individual cells

"""

# Standard library imports
from tkinter import *

# Local application imports
import board as bd
import checker as chk

root = Tk()
root.title("Sudoku")
root.geometry("324x550")

label = Label(root, text = "Fill in numbers")
label.grid(row = 0, column = 1, columnspan = 10, sticky = "ew")

genBoardBtn = Button(root, text = "Generate Board", command = lambda: generateBaord())
genBoardBtn.grid(row = 10, columnspan = 10, sticky = "ew")

checkBoardBtn = Button(root, text = "Check Board", command = lambda: checkBoard())
checkBoardBtn.grid(row = 11, columnspan = 10, sticky = "ew")

# Initialize cells of board.
cells = {}
puzzle = []

# Colors
blue = "#D0ffff"
yellow = "#ffffd0"
red = "#ffcccb"
green = "#98fb98"
default = "#F0F0F0"

def updateNumber(num, row, col):
	"""
	Updates number in puzzle when a number gets inserted into GUI

    Parameters
    ----------
	num: int
		The number that gets inserted into cell

	row: int
		The row of cell to that was updated

	col: int
		The column of cell that was updated
    
    Returns
    -------
    None

    """

	if num.isdigit() and int(num) in range(1,10):
		label.configure(text = 'Fill in numbers', bg = default)
		puzzle[row][col] = int(num)
	else:
		label.configure(text = 'INVALID NUMBER', bg = red)
		cells[(row, col)].delete(0, END)

	bd.printboard(puzzle)
	print('\n')

def generateBaord():
	"""
	Generates board and displays board in GUI

    Parameters
    ----------
	none
    
    Returns
    -------
    None

    """

	global puzzle

	clearBoard()

	board = bd.fillboard()
	puzzle = bd.removeCells(board, 20)

	for rowindex, row in enumerate(puzzle):
		for colindex, col in enumerate(row):
			cells[(rowindex, colindex)].configure(bg = cells[(rowindex, colindex)].color)
			if col == 0:
				cells[(rowindex, colindex)].insert(0, "")
			else:
				cells[(rowindex, colindex)].insert(0, str(col))
				cells[(rowindex, colindex)].configure(state="readonly")

def clearBoard():
	"""
	Clear board in GUI

    Parameters
    ----------
	none
    
    Returns
    -------
    None

    """
	
	for cell in cells:
		cells[cell].configure(state = "normal")
		cells[cell].delete(0, END)

def checkBoard():
	"""
	Checks board stored in puzzle

    Parameters
    ----------
	none
    
    Returns
    -------
    None

    """

	solved = True
	for rowindex, row in enumerate(puzzle):
		for colindex, col in enumerate(row):
			if not chk.checkNum(puzzle, rowindex, colindex):
				cells[(rowindex, colindex)].configure(bg = red)
				solved = False
			else:
				cells[(rowindex, colindex)].configure(bg = cells[(rowindex, colindex)].color)

	if not solved:
		label.configure(text = 'NOT CORRECT', bg = red)
	else:
		label.configure(text = 'SOLVED', bg = green)


def drawCell(row, col, color):
	"""
	Draws individual cells of board.

    Parameters
    ----------

	row: int
		The row of cell to that was updated

	col: int
		The column of cell that was updated

	color: str
		Hex value of color of cell
    
    Returns
    -------
    None

    """

	cell = Entry(root, width = 5, bg = color, justify = "center", readonlybackground = color)
	cell.grid(row = row + 1, column = col + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
	cell.bind('<Return>', lambda x: updateNumber(cell.get(), row, col)) 
	cell.color = color
	cells[(row, col)] = cell

# Draw board
for num in range(0, 81):

	row = num // 9
	col = num % 9

	if ((row // 3) % 2 == 0 and (col // 3) % 2 == 0) or ((row // 3) % 2 == 1 and (col // 3) % 2 == 1):
		color =  blue
	else:
		color = yellow

	drawCell(row, col, color)

root.mainloop()
