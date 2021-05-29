## -- Bellman Ford Algorithm

'''
Bruteforce Approach 
-ve Wt Also OKK
Source-Source cycle with +ve path sum is allowed
'''
adj = [[None, 5, 2, None, None],
       [None, None, 1, None, None],
       [None, None, None, -1, -1],
       [None, None, None, None, None],
       [3, None, None, 2, None]]

l = len(adj)
inf = 999999999999
dist = [inf]*l 
dist[0] = 0

for i in range(l-1):
	edgeUpdated = False
	for nodeFrom in range(l):
		for nodeTo in range(l):
			if adj[nodeFrom][nodeTo] and dist[nodeFrom]!=inf and dist[nodeTo] > (dist[nodeFrom] + adj[nodeFrom][nodeTo]):
				dist[nodeTo] = dist[nodeFrom] + adj[nodeFrom][nodeTo]
				edgeUpdated = True
	if not edgeUpdated:
		break

print(dist)