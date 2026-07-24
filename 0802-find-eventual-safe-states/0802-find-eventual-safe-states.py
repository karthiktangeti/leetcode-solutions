class Solution(object):
    def eventualSafeNodes(self, graph):
        def dfs(node,path,visited,safe):
            visited[node] = 1
            path[node] = 1
            for adj in graph[node]:
                if visited[adj] == 0:
                    if dfs(adj,path,visited,safe):
                        return True
                elif path[adj] == 1:
                    return True
            path[node] = 0
            safe[node] = 1
            return False
                
        n  = len(graph)
        path = [0] * n
        safe = [0] * n
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                dfs(i,path,visited,safe)
        result = []
        for i in range(len(safe)):
            if safe[i] == 1:
                result.append(i)
        return result

        