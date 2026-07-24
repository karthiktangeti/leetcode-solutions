class Solution(object):
    def findJudge(self, n, trust):
        adj = [[] for i in range(n + 1)]
        for u,v in trust:
            adj[u].append(v)
        inoder = [0] * (n + 1) 
        for i in range(1,n + 1):
            for ad in adj[i]:
                inoder[ad] += 1
        for i in range(1,n +1):
            if inoder[i] == n - 1 and len(adj[i]) == 0:
                return i
        return -1

        