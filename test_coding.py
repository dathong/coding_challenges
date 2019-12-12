import numpy as np

def rod_cutting(arr):
	n = len(arr)
	dp = [0 for x in range(n+1)]
	dp[0] = 0
	# dp[1] = arr[0]
	for i in range(1,n + 1):
		rod = []
		for j in range(i):
			rod.append(arr[j] + dp[i - j - 1])
		dp[i] = max(rod)
	return dp


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(rod_cutting(arr))