import numpy as np

def coin_change(arr,n):
	dp = [[0 for j in range(len(arr) + 1)] for i in range(n + 1)]

	for j in range(len(arr) + 1):
		dp[0][j] = 1
	for i in range(1,n + 1):
		for j in range(1,len(arr) + 1):

			x,y = 0,0
			x = dp[i][j - 1]
			if i >= arr[j - 1]:
				y = dp[i - arr[j - 1]][j]
			dp[i][j] = x + y

	print(np.array(dp))
	return np.array(dp)

arr = [1, 2, 3]
m = len(arr)
n = 4
print(coin_change(arr,n))