class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        color = [-1]*(N+1)
        
        def bipartite(adj,N,node,color):
            q = [node]
            color[node] = 1
            while len(q)!=0:
                current = q.pop(0)
                for ele in adj[current]:
                    if color[current]==color[ele]:
                        return False
                    if color[ele]==-1:
                        color[ele] = 1- color[current]
                        q.append(ele)
            return True
        for i in range(N):
            if color[i]==-1:
                if not bipartite(graph,N,i,color):
                    return False
        return True
        