import numpy as np


def find_triplet(A):
	max_so_far = A[0]
	count = 1
	for e in A:
		if e > max_so_far:
			max_so_far = e
			count+=1
	return (count >= 3)

print(find_triplet([4,3,2,1,1,9]))