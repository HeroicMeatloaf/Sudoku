# Standard library imports
from tkinter import *

# Local application imports
# import Sudoku.src.board as board 

root = Tk()
root.title("Sudoku")
root.geometry("324x550")

label = Label(root, text = "Fill in numbers").grid(row = 0, column = 1, columnspan = 10)

errLabel = Label(root, text = "", fg = "red")
errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

solvedLabel = Label(root, text = "", fg = "green")
solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

cells = {}

def drawCell(row, col, bgcolor):

	e = Entry(root, width = 5, bg = bgcolor, justify = "center", )
	e.grid(row = row + 1, column = col + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
	cells[(row + 1, col + 1)] = e

def draw9x9():
	for i in range(0, 81):

		row = i // 9
		col = i % 9

		if ((row // 3) % 2 == 0 and (col // 3) % 2 == 0) or ((row // 3) % 2 == 1 and (col // 3) % 2 == 1):
			color =  "#D0ffff"
		else:
			color = "#ffffd0"

		drawCell(row, col, color)

# Blue: color =  "#D0ffff"
# Yellow: color = "#ffffd0"

draw9x9()
root.mainloop()
