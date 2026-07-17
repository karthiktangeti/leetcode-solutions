from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix =[]
        mx = 0
        for x in nums:
            mx = max(mx,x)
            prefix.append(gcd(x,mx))
        
        prefix.sort()
        l = 0
        r = len(prefix) - 1
        ans = 0
        while l < r:
            ans += gcd(prefix[l],prefix[r])
            l += 1
            r -= 1
        return ans
        