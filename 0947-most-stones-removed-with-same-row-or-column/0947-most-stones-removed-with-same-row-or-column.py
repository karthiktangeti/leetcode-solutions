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
            return 
        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
class Solution(object):
    def removeStones(self, stones):
        n = len(stones)
        de = Disjoint(n)
        for i in range(n):
            for j in range(i + 1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    de.union(i,j)
        compo = 0
        for i in range(n):
            if de.find(i) == i:
                compo += 1
        return n - compo


        