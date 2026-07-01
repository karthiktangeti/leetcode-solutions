# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result= []
        if root:
            result += self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        return result
        