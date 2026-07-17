# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.ans = 0
        def dfs(root,depth):
            if not root:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = root.val
            elif depth == self.max_depth:
                self.ans += root.val
            dfs(root.left,depth + 1)
            dfs(root.right,depth + 1)
        dfs(root,0)
        return self.ans
        