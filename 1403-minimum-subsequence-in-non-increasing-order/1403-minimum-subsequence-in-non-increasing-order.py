class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse = True)
        curr = 0
        total = sum(nums)
        ans = []
        for num in nums:
            curr += num
            ans.append(num)
            if curr > total - curr:
                return ans

        