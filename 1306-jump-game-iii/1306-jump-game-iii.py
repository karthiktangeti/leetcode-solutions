class Solution(object):
    def canReach(self, arr, start):
        visited = [0] * len(arr)
        def dfs(index):
            if index < 0 or index >= len(arr):
                return False
            if visited[index]:
                return False
            if arr[index] == 0:
                return True
            visited[index] = 1

            right = index + arr[index]
            left = index - arr[index]
            return dfs(left) or dfs(right)
        return dfs(start)
        