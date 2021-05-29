graph = [
[1,2],
[0,3,4],
[0,4],
[1,4,5],
[1,2,3,5],
[3,4]
]

def printDFS(current,v):
	if current in v:
		return
	v.append(current)
	print(current)
	for i in graph[current]:
		printDFS(i,v)
# printDFS(current,list())

dirGraph = [
[1,2],
[3],
[],
[4,5],
[2,3,5],
[]
]

v = list()
def dirprintDFS(current):
	if current in v:
		return
	v.append(current)
	print(current)
	for i in dirGraph[current]:
		dirprintDFS(i)

dirprintDFS(0)
print(v)