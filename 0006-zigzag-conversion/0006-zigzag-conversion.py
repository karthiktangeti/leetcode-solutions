class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [""] * numRows
        d = -1
        c = 0
        for i in s:
            res[c] += i
            if c == 0:
                d = 1
            if c == numRows - 1:
                d = -1
            c +=  d
        return "".join(res)

        
        