import numpy as np

def lis(arr):
	res = []

	n = len(arr)
	res = [0 for x in range(n)]
	print("res = ", res, n)
	res[0] = 1
	for i in range(n):
		for j in range(i):
			if arr[i] >= arr[j]:
				res[i] = max(res[i],res[j] + 1)
	return res



arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
# n = 4
print(lis(arr))
