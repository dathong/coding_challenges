import numpy as np

def max_square(M):
	m = len(M)
	n = len(M[0])

	dp = [[0 for j in range(n)] for i in range(m)]

	if M[0][0] == 1:
		dp[0][0] = 1

	for i in range(1,m):
		for j in range(1,n):
			if M[i][j] != 1:
				continue
			dp[i][j] = min(dp[i - 1][j],dp[i][j - 1]) + 1

	print('dp = ',np.array(dp))
	return dp

# Driver Program 
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
  
print(max_square(M))
