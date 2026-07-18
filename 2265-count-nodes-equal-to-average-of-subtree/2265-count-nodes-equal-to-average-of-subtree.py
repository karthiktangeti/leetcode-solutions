# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return (0,0)
            left_s,left_c = dfs(root.left)
            right_s,right_c = dfs(root.right)
            total_sum = left_s + right_s + root.val
            total_count = left_c + right_c + 1
            average = total_sum // total_count
            if average == root.val:
                self.ans += 1
            return (total_sum,total_count)
        dfs(root)
        return self.ans

        