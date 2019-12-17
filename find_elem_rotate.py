import numpy as np
import math

def find_pivot(A):
	if len(A) == 1:
		return 0
	l,r = 0,len(A)
	while l < r - 1:
		mid = int((l+r)/2)
		if A[l] < A[mid]:
			l,r = mid,r
		else:
			l,r = l,mid
	return l

def bin_search(A,k):
	if len(A) == 1:
		if A[0] == k:
			return 0
		return -1
	l,r = 0,len(A)
	while l < r:
		mid = int((l + r)/2)
		if A[mid] == k:
			return mid
		elif A[mid] > k:
			l,r = l,mid
		else:
			l,r = mid,r
	if A[l] == k:
		return l
	return -1

def find_elem_rotate(A,k):
	p = find_pivot(A)
	new_A = A[p + 1:] + A[:p+1]
	print("new_A = ",new_A)
	return bin_search(new_A,k)

print(find_pivot([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]))

print(bin_search([1,6,8,10,11,15],11))
print(find_elem_rotate([4, 5, 6, 7, 8, 9, 0, 1, 2, 3],3))