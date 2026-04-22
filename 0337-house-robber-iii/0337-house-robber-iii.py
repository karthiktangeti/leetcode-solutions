class Solution:
    def rob(self, root):
        
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            # if we rob this node
            rob = node.val + left[1] + right[1]

            # if we skip this node
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))