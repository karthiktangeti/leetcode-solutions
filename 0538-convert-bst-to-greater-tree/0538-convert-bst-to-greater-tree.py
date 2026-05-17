# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        self.total = 0
        def dfs(node):
            if not node:
                return
            dfs(node.right)

            self.total += node.val

            node.val = self.total

            dfs(node.left)
        dfs(root)
        return root
        