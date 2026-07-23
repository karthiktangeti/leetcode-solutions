class Solution(object):
    def dfs(self,i,visited,graph,color):
        visited[i] = color
        for j in graph[i]:
            if visited[j] != -1:
                if visited[j] == color:
                    return False
            else:
                ans = self.dfs(j,visited,graph,1-color)
                if ans == False:
                    return False 
    def isBipartite(self, graph):
        total = len(graph)
        visited = [-1] * total
        for i in range(0,total):
            if visited[i] == -1:
                ans = self.dfs(i,visited,graph,0)
                if ans == False:
                    return False
        return True
        