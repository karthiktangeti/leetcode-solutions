# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        parent = {}
        def dfs(node,depth,par):
            if not node:
                return 
            parent[node.val] = [depth,par]
            dfs(node.left,depth + 1,node)
            dfs(node.right,depth + 1,node)
        dfs(root,0,None)
        a,b = parent[x]
        c,d = parent[y]
        if a == c and b.val != d.val:
            return True
        return False       