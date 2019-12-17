import numpy as np

def find_courses(courses):
	print('build graph')
	G = {}
	for c in courses:
		if c[0] not in G:
			G[c[0]] = []
		if c[1] not in G:
			G[c[1]] = [c[0]]
		else:
			G[c[1]].append(c[0])
	print("G = ",G)

	print('---reverse----')
	G_r = {}
	for u in G:
		if u not in G_r:
			G_r[u] = []
		for v in G[u]:
			if v not in G_r:
				G_r[v] = [u]
			else:
				G_r[v].append(u)
	print("G_r = ",G_r)

	print('----dfs----')
	visited = set()
	def dfs(G,u):
		if len(G[u]) == 0:
			print(u)
			visited.add(u)
			return
		for v in G[u]:
			if v not in visited:
				dfs(G,v)
		print(u)
		visited.add(u)

	print('----bfs----')

	def bfs(G,u):
		visited = set()
		queue = []
		queue.append(u)
		visited.add(u)
		while len(queue) > 0:
			u = queue.pop(0)
			print('u = ',u)
			for v in G[u]:
				if v not in visited:
					queue.append(v)
					visited.add(v)
	print('----test----')
	for u in G:
		if len(G[u]) == 0:
			bfs(G_r,u)

	bfs(G_r, 2)



courses = [[1,2],[2,3],[2,4],[2,8],[4,9]]
print(find_courses(courses))