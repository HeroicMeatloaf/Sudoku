# Local application imports
import Sudoku.src.board as board

# Initialize variables
# Number of test to run
# Current test number initialized to 0
# Number of fails initialized to 0
tests = 1000
testNum = 0
fails = 0

while testNum < tests:

	testNum += 1
	try:
		grid = board.fillboard()
		puzzle = board.removeCells(grid, 30)
		solvedPuzzle = board.fillboard(puzzle)
	except :
		fails += 1 

print(f'Number of fails {fails}')
print(f'Percentage of fails {(fails/tests) * 100}')