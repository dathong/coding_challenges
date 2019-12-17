import numpy as np
import math

def max_sum(A):
	if len(A) == 1:
		return A[0]
	curr_sum = A[0]
	max_sum = A[0]
	l, r = 0,1
	la, ra = l,r 
	while r < len(A):
		curr_sum+=A[r]
		if curr_sum > max_sum:
			max_sum = curr_sum
			la, ra = l,r
		r+=1
		if curr_sum < 0:
			curr_sum = 0
			l=r
	return A[la:ra + 1]

print(max_sum([1,-2,4,7,2,-1,3,-4,-8]))