class Disjoint:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self,u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return True
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return False 
class Solution(object):
    def makeConnected(self, n, connections):
        ds = Disjoint(n)
        extra = 0
        for u,v in connections:
            if ds.union(u,v):
                extra += 1
        connect = 0
        for i in range(n):
            if ds.find(i) == i:
                connect += 1
        if extra >= connect - 1:
            return connect - 1
        return -1


        