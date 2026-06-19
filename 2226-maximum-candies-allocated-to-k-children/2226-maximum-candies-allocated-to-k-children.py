class Solution(object):
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0
        l = 1
        r = max(candies)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for c in candies:
                count += c // mid

            if count >= k:
                ans  = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
       
                

        