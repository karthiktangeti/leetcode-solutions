class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        # ans = float("-inf")
        # k = 0
        # while k < n: 
        #     sum1 = 0
        #     for i in range(n):
        #         sum1 += i * nums[i]
        #     if sum1 > ans:
        #         ans = sum1
        #     last = nums[-1]
        #     for j in range(n - 1,0 ,-1):
        #         nums[j] = nums[j - 1]
        #     nums[0] = last
        #     k += 1
        # return ans 
        f = 0
        total = sum(nums)
        for i in range(n):
            f += i * nums[i]
        ans = f
        for i in range(1,n):
            f = f + total - n * nums[n - i]
            ans = max(ans,f)
        return ans