class Solution(object):
    def maximalNetworkRank(self, n, roads):
        degree = [0] * n
        graph = [set() for i in range(n)]
        for u,v in roads:
            degree[u] += 1
            degree[v] += 1
            graph[v].add(u)
            graph[u].add(v)
        res = 0
        for u in range(n):
            for v in range(u + 1,n):
                total = degree[u] + degree[v]
                if u in graph[v]:
                    total -= 1
                res = max(total,res)
        return res
        