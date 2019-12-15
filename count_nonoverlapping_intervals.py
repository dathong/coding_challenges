def max_disjoint(intervals):
	L = sorted(intervals,key = lambda a: a[1])
	count = 1
	s1 = L[0][0]
	e1 = L[0][1]
	print(s1,e1)
	for i in range(1,len(L)):
		s2 = L[i][0]
		e2 = L[i][1]
		if s2 > e1:
			count+=1
			print(s2,e2)
			s1 = s2
			e1 = e1
	return count

intervals = [(1,4),(2,3),(4,6),(8,9)]
print(max_disjoint(intervals))