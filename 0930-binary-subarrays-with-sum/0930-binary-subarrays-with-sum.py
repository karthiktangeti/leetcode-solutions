class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def func(k):
            if k < 0:
                return 0
            r,l,sum1,ans = 0,0,0,0
            while r < len(nums):
                sum1 += nums[r]
                while sum1 > k:
                    sum1 -= nums[l]
                    l += 1
                ans += r - l + 1
                r += 1
            return ans
        return func(goal) - func(goal - 1)
        