class Solution:
    def dfs(self, node, adj, vis, ds, V):
        if node == V - 1:
            if ds[0] == 0:
                d = ds.copy()
                l.append(ds)
            return
        for i in adj[node]:
            if vis[i] != 1:
                vis[i] = 1
                self.dfs(i, adj, vis, ds + [i], V)
                vis[i] = 0

    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        V = len(adj)
        vis = [0 for _ in range(V)]
        global l
        l = []
        ds = []
        self.dfs(0, adj, vis, ds + [0], V)
        return l