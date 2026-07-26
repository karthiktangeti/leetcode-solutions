import sys
import heapq
class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10 ** 9 + 7
        adj = [[] for i in range(n)]
        for s,e,w in roads:
            adj[s].append([e,w])
            adj[e].append([s,w])
        distance = [sys.maxsize for i in range(n)]
        distance[0] = 0
        ways = [0 for i in range(n)]
        ways[0] = 1
        priority_queue = [[0,0]]
        while priority_queue:
            dist,node = heapq.heappop(priority_queue)
            for nei,wig in adj[node]:
                new_d = dist + wig
                if new_d < distance[nei]:
                    distance[nei] = new_d
                    heapq.heappush(priority_queue,(new_d,nei))
                    ways[nei] = ways[node]
                elif new_d == distance[nei]:
                    ways[nei] += ways[node]
        return ways[n - 1] % MOD


        
        