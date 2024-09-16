# Problem 8: Local Maximums
'''
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

def local_maximums(grid):
	pass

  ================================================================

    1.	Questions:
	•	Will the grid always be at least 3x3?
	•	How should we handle edge cases where the grid has fewer than 3 rows or columns?
	2.	Explanation:
For each position in the reduced grid, I need to find the maximum value in the corresponding 3x3 subgrid from the original grid.
	3.	Pseudocode:
	•	Initialize an empty result grid.
	•	For each possible 3x3 subgrid in the original grid, find the maximum value.
	•	Store this value in the corresponding position of the result grid.
	•	Return the result grid.
	4.	Python Implementation:  

'''

def local_maximums(grid):
    n = len(grid)
    result = []
    
    for i in range(1, n - 1):
        row = []
        for j in range(1, n - 1):
            # Find the maximum in the 3x3 grid centered around grid[i][j]
            max_val = max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                          grid[i][j-1], grid[i][j], grid[i][j+1],
                          grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])
            row.append(max_val)
        result.append(row)
    
    return result

# Example usage:
grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(local_maximums(grid1))  # Output: [[9, 9], [8, 6]]
print(local_maximums(grid2))  # Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]