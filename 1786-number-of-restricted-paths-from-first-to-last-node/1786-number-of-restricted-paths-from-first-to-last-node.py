import heapq
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        adj = [[] for i in range(n + 1)]
        for u,v,d in edges:
            adj[u].append([v,d])
            adj[v].append([u,d])
        dis = [float("inf") for i in range(n + 1)]
        priority_q = [(0,n)]
        dis[n] = 0
        while priority_q:
            d,node  = heapq.heappop(priority_q)
            if d > dis[node]:
                continue
            for nei,w in adj[node]:
                distance = d + w
                if distance < dis[nei]:
                    dis[nei] = distance
                    heapq.heappush(priority_q,(distance,nei))
        MOD = 10 ** 9 + 7
        memo = [-1] * (n + 1)
        def dfs(node):
            if node == n:
                return 1
            if memo[node] != -1:
                return memo[node]
            path = 0
            for nei,d in adj[node]:
                if dis[nei] < dis[node]:
                    path += dfs(nei)
            memo[node] = path % MOD
            return memo[node]

        return dfs(1)
        
        

                

