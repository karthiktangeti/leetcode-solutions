class Solution(object):
    def minWindow(self, s, t):
        dist = {}
        for i in t:
            dist[i]  = dist.get(i,0) + 1
        r,l,c,min_len,s_i = 0,0,0,float("inf"),-1
        while r < len(s):
            if s[r] in dist:
                if dist[s[r]] > 0:
                    c += 1
                dist[s[r]] -= 1 
            while c == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l +1
                    s_i = l
                if s[l] in dist:
                    dist[s[l]] += 1
                    if dist[s[l]] > 0:
                        c -= 1
                l += 1
            r += 1
        if s_i == -1:
            return ""
        return s[s_i:s_i + min_len]   
                    
                
        