# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = deque([root])
        while queue:
            level = list(queue)
            queue.clear()
            level_sum = 0
            for node in level:
                if node.left:
                    level_sum += node.left.val
                    queue.append(node.left)
                if node.right:
                    level_sum += node.right.val
                    queue.append(node.right)
            for node in level:
                sibling_sum =0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                if node.left:
                    node.left.val = level_sum - sibling_sum
                if node.right:
                    node.right.val = level_sum - sibling_sum
        return root
                
