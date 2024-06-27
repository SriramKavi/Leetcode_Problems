class Solution:
    def findCenter(self, edges: List[List[int]]) -> int: 
        V = len(edges) + 1 
        adj = [[] for _ in range(V + 1)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        m = -1
        p = 0
        print(adj)
        for i in range(len(adj)):
            if len(adj[i]) > m:
                m = len(adj[i])
                p = i
        return p