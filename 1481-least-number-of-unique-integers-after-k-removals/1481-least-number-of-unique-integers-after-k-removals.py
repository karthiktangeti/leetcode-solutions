class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0) + 1
        dist = sorted(freq.values())
        unique = len(dist)
        for c in dist:
            if k >= c:
                k -= c
                unique -= 1
            else:
                break
        return unique

