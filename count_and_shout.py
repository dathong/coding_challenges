def count_and_shout(n):
	res = ['1','11']
	if n == 2:
		return res
	for i in range(2,n):
		s = res[i - 1]
		print('s = ',s)

		count = 1
		next_s = ""
		for j in range(len(s) - 1):
			# print('j = ',j,len(s))
			if s[j+1] == s[j]:
				count+=1
			else:
				next_s += str(count) + str(s[j])
				count = 1

		# print('j = ',j,s[j])
		j+=1
		if s[j] != s[j - 1]:
			next_s+="1" + str(s[j])
		else:
			next_s+=str(count) + str(s[j])

		res.append(next_s)
	return res

print(count_and_shout(9))