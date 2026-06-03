class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def func(k):
            r,l,ans = 0,0,0
            dist = {}
            while r < len(nums):
                dist[nums[r]] = dist.get(nums[r],0) + 1
                while len(dist) > k:
                    dist[nums[l]] -= 1
                    if dist[nums[l]] == 0:
                        del dist[nums[l]]
                    l += 1
                ans += r - l + 1
                r += 1
            return ans
        return func(k) - func(k - 1)
                

        