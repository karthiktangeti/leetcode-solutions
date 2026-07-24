class Solution(object):
    def gardenNoAdj(self, n, paths):
        adj = [[] for i in range(n + 1)]
        for u,v in paths:
            adj[u].append(v)
            adj[v].append(u)
        flower = [0] * (n + 1)
        for i in range(1,n + 1):
            used = set()

            for nei in adj[i]:
                if flower[nei] != 0:
                    used.add(flower[nei])
            for flow in range(1,n + 1):
                if flow not in used:
                    flower[i] = flow
                    break
        return flower[1:] 












