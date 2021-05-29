adj =  [[0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0]]

#sometimes dfs cant access all nodes for that only if we start dfs from that left node then psbl
#so we'll use visited and nonvisited array for that

# row ke har 1st elem then uske 1st elem ke corresponding elem fir agar wo elem 1 hua to chk if it is in row ka 1st elem contiue

def printDFSwVis(adj,current,visited):
	if current in visited:
		return
	visited.add(current)
	print(current)
	for j in range(len(adj[0])):
		if adj[current][j]==1:
			printDFSwVis(adj,j,visited)

# printDFSwVis(adj,0,set())

nv = [x for x in range(len(adj))]
def printDFSwvnnonv(adj,curr,vis,nvis):
	if curr in vis:
		return
	vis.add(curr)
	if curr in nvis:
		nvis.remove(curr)
	print(curr)
	for j in range(len(adj[0])):
		if adj[curr][j]==1:
			printDFSwvnnonv(adj,j,vis,nvis)
# nv = list(nv)
# while len(nv)!=0:
# 	printDFSwvnnonv(adj,nv[0],set(),nv)

def printBFS(adj,current):
	q = [current]
	visited = set([current])
	while len(q)>0:
		c = q.pop(0)
		print(c)
		for j in range(len(adj[0])):
			if adj[c][j]==1 and j not in visited:
				visited.add(j)
				q.append(j)

# printBFS(adj,0)


def detectCycleinUndir(adj,current):
	q = [current]
	visited = set([current])
	while len(q)>0:
		c = q.pop(0)
		for j in range(len(adj[0])):
			if adj[c][j]==1 and j not in visited:
				visited.add(j)
				q.append(j)
			elif adj[c][j]==1 and j in visited:
				print('GOT cycle from',c,'to',j)
detectCycleinUndir(adj,0)


##   adjacency matrix
#    selfEdge parellelEdge directedGraph visited(option to reach all part of graph)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = []
        selfEdge = False
        pE = False
        direc = False
        for i in range(len(graph)):
            if i in graph[i]:
                selfEdge = True
            
            s = graph[i]
            if len(list(s))!=len(s):
                pE = True
            
            for j in graph[i]:
                if not i in graph[j]:
                    direc = True
                if j not in v:
                    v.append(j)
        print("selfED",selfEdge)
        print("pE",pE)
        print("directed",direc)
        print("v",v)

