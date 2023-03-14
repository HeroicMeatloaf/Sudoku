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
		if 0 not in row:
			print(f'This row is filled in, moving on to {rowindex+2}')
			continue

		# Take copy of grid. List of all numbers not in row.
		prevGrid = [row[:] for row in grid]
		numbers = [x for x in range(1,10) if x not in row]

		print(f'All numbers available: {numbers}')
		

		for colindex, col in enumerate(row):
			
			print(f'Starting col {colindex + 1}: {col}')

			if grid[rowindex][colindex]:
				# Number already present. Continue to next column.

				print('This number is already filled in moving to next column')
				print(sep)
				continue

			
			#attempted = []
			

			while True:

				numLength = len(numbers)
				print(f'List of numbers: {numbers}')

				if numLength == 0:

					print('NumLength = 0. No more numbers to try')
					print('Back tracking to previous grid:')
					board.printGrid(prevGrid)

					grid = solver(prevGrid)
					return grid

				#print(f'Attempted numbers{attempted}')

				guess = random.choice(numbers)
				print(f'Attempting {guess} at {rowindex},{colindex}')
				grid[rowindex][colindex] = guess

				if checker.checkNum(grid, rowindex, colindex):
					# Passes - Break out of while loop and move to next column
					# Reset list of numbers based on what's in row

					print(f'{guess} at {rowindex},{colindex} passes')
					print(sep)
					numbers = [x for x in range(1,10) if x not in row]
					break
				else:
					#fails - add guess to list of attempted. Fall of end of while loop and try again
					print(f'{guess} at {rowindex},{colindex} fails')
					print(sep)
					numbers.pop(numbers.index(guess))
					#attempted.append(guess)
					
	return grid
					
					

if __name__ == '__main__':

	file = open('output.txt', 'w')
	sys.stdout = file

	grid = board.fillGrid()
	board.removeCells(grid, 30)
	grid = solver(grid)
	board.printGrid(grid)

