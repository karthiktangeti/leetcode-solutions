class Solution(object):
    def xorQueries(self, arr, queries):
        nums = []
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1] ^ i)
        for l,r in queries:
            nums.append(prefix[r + 1] ^ prefix[l])

        return nums