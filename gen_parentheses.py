import numpy as np
import math

def insert_into(s,c,i):
	return s[:i] + c + s[i:]
def gen_parenthese(n):
	if n == 2:
		return ["()"]
	res = set()
	for p in gen_parenthese(n - 2):
		for i in range(len(p) + 1):
			for j in range(i + 1,len(p) + 1):
				s = insert_into(p,"(",i)
				s1 = insert_into(s,")",j)
				res.add(s1)

	return res

print(gen_parenthese(8))