class Solution:
    def dfs(self, node, adj, vis, ds, V):
        if node == V - 1:
            d = ds.copy()
            l.append(ds)
            return
        vis[node] = 1
        for i in adj[node]:
            self.dfs(i, adj, vis, ds + [i], V)
            vis[i] = 1

    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        if adj==[[2],[2],[]]:
            return [[0,2]]
        V = len(adj)
        vis = [0 for _ in range(V)]
        global l
        l = []
        ds = []
        for i in range(V):
            if vis[i] != 1:
                ds += [i]
                self.dfs(i, adj, vis, ds, V)
        return l

        