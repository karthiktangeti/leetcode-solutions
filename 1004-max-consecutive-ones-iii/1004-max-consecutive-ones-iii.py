class Solution(object):
    def longestOnes(self, nums, k):
        maxi,l,r,zero = 0,0,0,0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                zero += 1
            if zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            
            maxi = max(maxi,r-l+1)
            r += 1
        return maxi
