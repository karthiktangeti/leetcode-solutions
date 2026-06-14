class Solution(object):
    def primePalindrome(self, n):
        def prime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        if 8 <= n <= 11:
            return 11
        x = 1
        while True:
            s = str(x)
            pal = int(s+ s[-2::-1])
            if pal >= n and prime(pal):
                return pal
            x += 1

        