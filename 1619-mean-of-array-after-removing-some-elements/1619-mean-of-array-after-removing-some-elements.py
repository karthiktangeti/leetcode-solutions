class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        remove = n // 20
        total = sum(arr[remove:n - remove])
        return total / float(n - 2 * remove)
        