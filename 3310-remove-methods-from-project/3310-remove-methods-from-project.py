class Solution(object):
    def remainingMethods(self, n, k, invocations):
        adj = [[] for i in range(n)]
        for u,v in invocations:
            adj[u].append(v)
        supu = [False] * n
        def dfs(k):
            supu[k] = True
            for nei in adj[k]:
                if not supu[nei]:
                    dfs(nei)
            
        dfs(k)
        for u,v in invocations:
            if not supu[u] and supu[v]:
                return list(range(n))
        res = []
        for i in range(n):
            if not supu[i]:
                res.append(i)
        return res

        