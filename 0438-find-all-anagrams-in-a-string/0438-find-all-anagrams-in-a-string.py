class Solution(object):
    def findAnagrams(self, s, p):
        def func(a,b):
            if len(a) != len(b):
                return False
            for i in a:
                if i not in b or a[i] != b[i]:
                    return False
            return True

        dicia = {}
        dicib = {}
        m = len(p)
        for i in p:
            dicia[i] = dicia.get(i,0) + 1
        
        ans = []
        l = 0
        n = len(s)
        for i in range(n):
            dicib[s[i]] = dicib.get(s[i],0) +1

            if i - l == m:
                val = dicib[s[l]]
                dicib[s[l]] -= 1
                if dicib[s[l]] == 0:
                    del dicib[s[l]]
                l += 1
            if i - l + 1== m:
                if func(dicib,dicia):
                    ans.append(l)
        return ans
            
        