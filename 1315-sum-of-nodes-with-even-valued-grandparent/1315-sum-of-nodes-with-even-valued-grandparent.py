# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,parent,grandparent):
            if not root:
                return 
            if grandparent is not None and grandparent % 2 == 0:
                self.ans += root.val
            dfs(root.left,root.val,parent)
            dfs(root.right,root.val,parent)
        dfs(root,None,None)
        return self.ans
        