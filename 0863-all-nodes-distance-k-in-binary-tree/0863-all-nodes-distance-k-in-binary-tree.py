# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        parent = {}
        def build(node,par):
            if not node:
                return 
            parent[node] = par
            build(node.left,node)
            build(node.right,node)
        build(root,None)
        ans = []
        visited = set()
        def dfs(node,dist):
            if not node or node in visited:
                return
            visited.add(node)
            if dist == k:
                ans.append(node.val)
            dfs(node.left,dist + 1)
            dfs(node.right,dist + 1)
            dfs(parent[node],dist + 1)
        dfs(target,0)
        return ans
        