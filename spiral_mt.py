import numpy as np

def spiral(n):

	visited = [[0 for j in range(n)] for i in range(n)]
	M = [[0 for j in range(n)] for i in range(n)]

	i,j = 0,0

	count = 1
	visited[i][j] = 1
	M[i][j] = count
	while count < 20:
		while True:
			i,j = i, j + 1
			if j >= n or visited[i][j] == 1:
				break
			count+=1
			M[i][j] = count
			visited[i][j] = 1
		j-=1
		while True:
			i,j = i + 1,j
			if i >= n or visited[i][j] == 1:
				break
			count+=1
			M[i][j] = count
			visited[i][j] = 1
		i-=1
		while True:
			i,j = i, j - 1

			if j < 0 or visited[i][j] == 1:
				break
			count+=1
			M[i][j] = count
			visited[i][j] = 1
		j+=1
		while True:
			i,j = i - 1,j
			if i < 0 or visited[i][j] == 1:
				break
			count+=1
			M[i][j] = count
			visited[i][j] = 1
		i+=1
		# break
	return np.array(M)

print(spiral(5))