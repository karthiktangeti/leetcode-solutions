class Solution(object):
    def subarraySum(self, nums, k):
        freq = {0:1}
        ans = 0
        prefix = 0
        for num in nums:
            prefix += num
            if prefix - k in freq:
                ans += freq[prefix - k]
            freq[prefix] = freq.get(prefix,0) + 1
        return ans