import numpy as np

def lcs(X,Y):
	m = len(X)
	n = len(Y)

	dp = [[0 for y in range(n)] for x in range(m)]

	if Y[0] in X:
		for x in range(m):
			dp[x][0] = 1

	if X[0] in Y:
		for y in range(n):
			dp[0][y] = 1


	for i in range(1,m):
		for j in range(1,n):
			if X[i] == Y[j]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
	return np.array(dp)


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y) )
