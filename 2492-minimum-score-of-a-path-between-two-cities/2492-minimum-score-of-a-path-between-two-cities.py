class Solution(object):
    def minScore(self, n, roads):
        adj = [[] for i in range(n + 1)]
        visited  = [False] * (n + 1)
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        self.ans = float("inf")
        def dfs(node):
            visited[node] = True
            for u,w in adj[node]:
                self.ans = min(self.ans,w)
                if not visited[u]:
                    dfs(u)    
        dfs(1)  
        return self.ans