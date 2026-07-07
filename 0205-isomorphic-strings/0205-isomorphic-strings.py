class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        t1 = {}
        s1 = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in s1:
                if s1[c1] != c2:
                    return False
            else:
                s1[c1] = c2
            if c2 in t1:
                if t1[c2] != c1:
                    return False
            else:
                t1[c2] = c1
        return True

            
            

        