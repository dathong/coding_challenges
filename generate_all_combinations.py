def comb(arr):
	if len(arr) == 1:
		return [[arr[0]]]

	res = []
	for i in range(len(arr)):
		for c in comb(arr[:i] + arr[i+1:]):
			res.append([arr[i]] + c)
	return res

arr = [1,2,3,4]
print(comb(arr))
