class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a % b)
        a = min(nums)
        b = max(nums)
        return gcd(a,b)
        