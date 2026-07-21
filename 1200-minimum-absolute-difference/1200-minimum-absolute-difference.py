class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float("inf")
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < min_diff:
                min_diff = abs(arr[i] - arr[i + 1])
        res = []
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == min_diff:
                res.append([arr[i],arr[i + 1]]) 
        return res   