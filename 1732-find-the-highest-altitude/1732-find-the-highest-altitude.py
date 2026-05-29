class Solution(object):
    def largestAltitude(self, gain):
        n = len(gain)
        arr = [0] * (n + 1)
        for i in range(n):
            arr[i + 1] = arr[i] + gain[i]
        return max(arr)
        