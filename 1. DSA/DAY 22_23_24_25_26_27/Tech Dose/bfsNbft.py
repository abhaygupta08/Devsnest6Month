graph = [
[1,2],
[0,3,4],
[0,4],
[1,4,5],
[1,2,3,5],
[3,4]
]

visited = [0]*(len(graph))
def printBFS(current):
	q = [current]
	visited[current] = 1
	while len(q)!=0:
		current = q.pop(0)
		print(current)
		for i in graph[current]:
			if visited[i]==0:
				q.append(i)
				visited[i]=1
printBFS(0)