from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
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
        