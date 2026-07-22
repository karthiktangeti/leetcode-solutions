# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        self.i = 0
        def dfs(low,high):
            if self.i == len(preorder):
                return None
            if preorder[self.i] < low or preorder[self.i] > high:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = dfs(low,root.val)
            root.right = dfs(root.val,high)
            return root
        return dfs(float("-inf"),float("inf"))
        