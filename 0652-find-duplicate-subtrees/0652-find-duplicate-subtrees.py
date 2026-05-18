# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = {}
        res = []
        def dfs(node):
            if not node:
                return "#"
            left = dfs(node.left)
            right = dfs(node.right)

            serial = str(node.val) + "," + left + "," + right
            count[serial]  = count.get(serial,0) +1
            if count[serial] == 2:
                res.append(node)
            return serial
        dfs(root)
        return res
        