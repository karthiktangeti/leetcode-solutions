class Solution(object):
    def minSetSize(self, arr):
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0) + 1
        counts = sorted(freq.values(),reverse = True)
        remove = 0
        ans = 0
        target = len(arr) // 2
        for c in counts:
            remove += c
            ans += 1
            if remove >= target:
                return ans   