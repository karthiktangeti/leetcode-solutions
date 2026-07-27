import sys
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        adj = [[sys.maxsize for i in range(n)] for i in range(n)]
        for u,v,w in edges:
            adj[u][v] = w
            adj[v][u] = w
        for i in range(n):
            adj[i][i] = 0
        for v in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][v] != sys.maxsize and adj[v][j] != sys.maxsize:
                        adj[i][j] = min(adj[i][j],adj[i][v] + adj[v][j])
        mini = n
        city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if adj[i][j] <= distanceThreshold:
                    count += 1
            if count <=  mini:
                mini = count
                city = i
        return city

                













