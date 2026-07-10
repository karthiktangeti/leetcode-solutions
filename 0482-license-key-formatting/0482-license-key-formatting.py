class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        c = 0
        for i in reversed(s):
            if i == "-":
                continue
            if c == k:
                res.append("-")
                c = 0
            res.append(i.upper())
            c += 1
            
        return "".join(reversed(res))
        