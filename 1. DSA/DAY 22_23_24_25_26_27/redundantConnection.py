class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def findCycle(u,v):
            uP = find(u)
            vP = find(v)
            if uP==vP:
                return True
            parent[vP] = uP
            return False
        
        def find(u):
            if parent[u]==-1:
                return u
            return find(parent[u])
        
        parent = [-1]*(len(edges)+1)
        for edge in edges:
            if findCycle(edge[0],edge[1]):
                return edge
        return edge[0]
        