class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        l = nums[0]
        r = nums[-1]
        ans = []
        for i in range(l,r + 1):
            if i not in nums:
                ans.append(i)
        return ans