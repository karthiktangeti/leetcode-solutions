class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        co = {}
        for i in s1:
            co[i] = co.get(i,0) + 1
        
        window = {}
        l = 0
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i],0) + 1
            if i - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if i - l + 1 == len(s1):
                if co == window:
                    return True
        return False