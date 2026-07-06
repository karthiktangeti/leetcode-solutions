class Solution(object):
    def halvesAreAlike(self, s):
        n = len(s)
        mid = n // 2
        a = s[:mid]
        b = s[mid:]
        vol = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c = 0
        for i in a:
            if i in vol:
                c += 1
        c1 = 0
        for i in b:
            if i in vol:
                c1 += 1
        if a != b and c == c1:
            return True
        return False

        