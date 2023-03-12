#Methods to solve board

import random
import board
import checker

def solver(grid):

	prevGrid = [row[:] for row in grid]
	
	for row in grid:
		for col in row:

			numbers = [x for x in range(1,10)]
			attempted = []

			if grid[row][col]:
				numbers.pop(numbers.index(grid[row][col]))
				continue

			while True:
				if len(numbers) = 0:
					#No more numbers to try. Back track and try again
					solver(prevGrid)
				guess = random.choice(x for x in numbers if x not in attempted)
				grid[row][col] = guess

				if checker.checkNum(grid, row, col):
					#passes - Break out of while loop and move to next column
					break
				else:
					#fails - add guess to list of attempted. Fall of end of while loop and try again
					attempted.append(guess)




