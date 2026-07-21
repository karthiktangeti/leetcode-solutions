class Solution(object):
    def canBeEqual(self, target, arr):
        n = len(arr)
        target.sort()
        arr.sort()
        for i in range(n):
            if arr[i] != target[i]:
                return False
        return True

        