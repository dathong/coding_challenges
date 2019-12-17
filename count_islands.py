import numpy as np
import math

count = 0
def count_islands(A):
	visited = [[0 for j in range(len(A[0]))] for i in range(len(A))]
	global count

	def direct(i,j,d):
		if d == "up":
			return i - 1,j
		if d == "down":
			return i + 1,j
		if d == "left":
			return i,j - 1
		if d == "right":
			return i,j + 1


	def process(A,i,j, level):
		global count
		if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or visited[i][j] != 0 or A[i][j] != 'X':
			return
		if level == 0:
			count += 1
		visited[i][j] = 1
		for d in ["up", "down", "left", "right"]:
			x, y = direct(i, j, d)
			process(A, x, y, level + 1)

	for i in range(len(A[0])):
		for j in range(len(A)):
			process(A,i,j,0)

	return count

A = [["X",".",".","X"],
	 [".","X",".","X"],
	 [".","X",".","."],
	 ["X",".",".","X"]]
print(count_islands(A))