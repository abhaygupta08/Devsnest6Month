graph = [[1],[5],[9],[4],[5,7],[2,6],[],[6],[7],[]]

v = len(graph)

''''##BFS
nv = set([i for i in range(v)])

while len(nv)!=0:
	order = []
	q = [nv.pop()]
			
	while len(q)!=0:
		m = q.pop(0)
		print(m)
		for i in graph[m]:
			if i in nv:
				q.append(i)
				nv.remove(i)'''
def bfs(graph):
	nv = set([i for i in range(v)])
	order = []
	while len(nv)!=0:
		q = [nv.pop()]
		while len(q)!=0:
			m = q.pop(0)
			order.append(m)
			# nv.remove(m)
			for i in graph[m]:
				if i in nv:
					q.append(i)
					nv.remove(i)
	print(order)

def dfs(graph):
	nv = set([i for i in range(len(graph))])
	order = []
	while len(nv)!=0:
		q = [nv.pop()]
		while len(q)!=0:
			m = q.pop()
			order.append(m)
			for i in graph[m]:
				if i in nv:
					q.append(i)
					nv.remove(i)
	print(order)

dfs(graph)