class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        adj = [[] for i in range(n)]
        inorder = [0 for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            inorder[v] += 1
        res = []
        for i in range(len(inorder)):
            if inorder[i] == 0:
                res.append(i)
        return res
            
        