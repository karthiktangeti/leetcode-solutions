class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def func(k):
            if k < 0:
                return 0
            r = 0
            l = 0
            count = 0
            ans = 0
            while r < len(nums):
                if nums[r] % 2 == 1:
                    count += 1
                while count > k:
                    if nums[l] % 2 == 1:
                        count -= 1
                    l += 1
                ans += r - l + 1
                r += 1
            return ans
        return func(k) - func(k - 1)
        