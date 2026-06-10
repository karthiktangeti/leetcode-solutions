class Solution(object):
    def minFlips(self, a, b, c):
        ans= 0
        while a or b or c:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
            if cbit:
                if abit == 0 and bbit == 0:
                    ans += 1
            else:
                ans += abit + bbit
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return ans
        