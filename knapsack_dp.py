import numpy as np

def knapSack(W,wt,val,n):
	dp = [[0 for j in range(W + 1)] for i in range(len(wt))]
	print(dp)
	for j in range(W + 1):
		if j >= wt[0]:
			dp[0][j] = val[0]
	# 0 x x x
	# 0 x x x
	# 0 x x x
	for i in range(1,len(wt)): # items
		for j in range(1,W + 1): #weights
			v1,v2= 0,0
			v1 = dp[i - 1][j]
			if j >= wt[i]:
				v2 = dp[i - 1][j - wt[i]] + val[i]
			dp[i][j] = max(v1,v2)

	return np.array(dp)


val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val)
print (knapSack(W , wt , val , n))
