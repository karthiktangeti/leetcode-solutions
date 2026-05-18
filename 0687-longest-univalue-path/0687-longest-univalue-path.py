# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            leftpath = 0
            rightpath = 0
            if node.left and node.left.val == node.val:
                leftpath  = left + 1
            if node.right and node.right.val == node.val:
                rightpath = right + 1
            self.ans = max(self.ans,leftpath + rightpath)
            return max(leftpath,rightpath)
        dfs(root)
        return self.ans
        