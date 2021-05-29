heights =  [[0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0]]

l = len(heights)
visited = [False]*l
dist = [999999999999]*l
dist[0] = 0
for i in range(l):
    mind = 999999999999
    x = -1
    for j in range(l):
        if not visited[j] and dist[j] < mind:
            x = j
            mind = dist[j]
    visited[x] = True
            
    for j in range(l):
        if not visited[j] and dist[i]!=999999999999 and heights[i][j]>0:
            dist[j] = min(dist[j],dist[x]+heights[x][j])
print(dist)