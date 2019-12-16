import numpy as np
import math

def count_bit(n):
	res = [0,1]
	curr_log = 2
	for i in range(2,n + 1):
		log_i = math.log10(i) / math.log10(2)
		if (math.ceil(log_i) == math.floor(log_i)):
			x = 1
			curr_log = i
		else:
			x = 1 + res[i - curr_log]
		res.append(x)
	return res

print(count_bit(2))