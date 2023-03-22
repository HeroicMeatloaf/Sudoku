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

# errLabel = Label(root, text = "", fg = "red")
# errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

# solvedLabel = Label(root, text = "", fg = "green")
# solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

cells = {}

def drawCell(row, col, bgcolor):

	cell = Entry(root, width = 5, bg = bgcolor, justify = "center")
	cell.grid(row = row + 1, column = col + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
	cell.bind('<Return>', lambda x: updateNumber(cell.get(), row, col)) 
	cell.configure({"readonlybackground": bgcolor})
	cells[(row, col)] = cell

def draw9x9():
	for cell in range(0, 81):

		row = cell // 9
		col = cell % 9

		if ((row // 3) % 2 == 0 and (col // 3) % 2 == 0) or ((row // 3) % 2 == 1 and (col // 3) % 2 == 1):
			color =  "#D0ffff"
		else:
			color = "#ffffd0"

		drawCell(row, col, color)

def updateNumber(num, row, col):

	if num.isdigit() and int(num) in range(1,10):
		label.configure(text = 'Fill in numbers', bg="#F0F0F0")
		puzzle[row][col] = int(num)
	else:
		label.configure(text = 'INVALID NUMBER', bg="#ffcccb")
		cells[(row, col)].delete(0, END)

# Blue: color =  "#D0ffff"
# Yellow: color = "#ffffd0"

board = bd.fillboard()
puzzle = bd.removeCells(board, 30)



draw9x9()

for rowindex, row in enumerate(puzzle):
	for colindex, col in enumerate(row):
		if col == 0:
			cells[(rowindex, colindex)].insert(0, "")
		else:
			cells[(rowindex, colindex)].insert(0, str(col))
			cells[(rowindex, colindex)].configure(state="readonly")

root.mainloop()
