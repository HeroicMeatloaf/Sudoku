#Methods to solve board

import random
import sys
import board
import checker

sep = '\n' +  ('-' * 20) + '\n'

def solver(grid):
	print(sep)
	print('Starting Grid')
	board.printGrid(grid)
	print(sep)

	
	for rowindex, row in enumerate(grid):
		print(f'Starting row {rowindex + 1}: {row}')
		prevGrid = [row[:] for row in grid]
		numbers = [x for x in range(1,10)]
		

		for colindex, col in enumerate(row):
			print(f'Starting col {colindex + 1}: {col}')

			if grid[rowindex][colindex]:
				# Number already present. Pop number from list and continue to next column.

				print('This number is already filled in moving to next column')
				print(sep)
				numbers.pop(numbers.index(grid[rowindex][colindex]))
				continue

			numLength = len(numbers)
			attempted = []
			

			while True:

				if numLength == len(attempted):

					print(f'NumLength({numLength}) = Lenght of attempted({len(attempted)})')
					print('Back tracking to previous grid:')
					board.printGrid(prevGrid)

					grid = solver(prevGrid)
					return grid

				print(f'List of numbers: {numbers}')
				print(f'Attempted numbers{attempted}')

				guess = random.choice([x for x in numbers if x not in attempted])
				print(f'Attempting {guess} at {rowindex},{colindex}')
				grid[rowindex][colindex] = guess

				if checker.checkNum(grid, rowindex, colindex):
					#passes - Break out of while loop and move to next column

					print(f'{guess} at {rowindex},{colindex} passes')
					print(sep)
					numbers.pop(numbers.index(guess))
					break
				else:
					#fails - add guess to list of attempted. Fall of end of while loop and try again
					print(f'{guess} at {rowindex},{colindex} fails')
					print(sep)
					attempted.append(guess)
					
	return grid	
					
					

if __name__ == '__main__':

	file = open('output.txt', 'w')
	sys.stdout = file

	grid = board.fillGrid()
	board.removeCells(grid, 30)
	grid = solver(grid)
	board.printGrid(grid)

