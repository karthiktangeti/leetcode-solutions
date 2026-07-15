class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(n,m):
            if m == 0:
                return n
            return gcd(m,n % m)
        odd = 0
        even = 0
        for i in range(1,2 * n + 1):
            if i % 2 == 0:
                even += i
            else:
                odd += i
        return gcd(even,odd)

        
        