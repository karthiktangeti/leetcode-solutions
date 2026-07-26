from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for i in range(n)]
        for e,d,c in flights:
            adj[e].append([d,c])
        dist = [float("inf") for i in range(n)]
        dist[src] = 0
        queue = deque()
        queue.append([0,src,0])
        while queue:
            step,node,cost = queue.popleft()
            if step > k:
                continue
            for nei,c in adj[node]:
                
                
                new_cost = cost + c
                if new_cost < dist[nei]:
                    new_step = step + 1
                    
                    dist[nei] = new_cost
                    queue.append([new_step,nei,new_cost])
        if dist[dst] == float("inf"):
            return -1
        return dist[dst]
        