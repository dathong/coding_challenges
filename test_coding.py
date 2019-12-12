import numpy as np

def jump(arr):
	n = len(arr)
	dp = [9999 for i in range(n)]

	dp[0] = 0

	for i in range(n):
		for j in range(1,arr[i] + 1):
			if i + j < n:
				dp[i + j] = min(dp[i + j],dp[i] + 1)

	print(dp)



arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(jump(arr))